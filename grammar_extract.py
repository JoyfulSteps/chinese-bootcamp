#!/usr/bin/env python3
"""
grammar_extract.py
------------------
Trích xuất toàn bộ nội dung ngữ pháp từ các bài học trong
chinese-bootcamp để chuẩn bị đưa vào Anki.

Cấu trúc output: grammar_output/
    ├── grammar_cards.tsv       ← Import vào Anki (tab-separated)
    ├── grammar_cards.json      ← Full data để debug / tái sử dụng
    └── grammar_preview.md      ← Xem trước nhanh toàn bộ thẻ

Cách dùng:
    python grammar_extract.py

Tác giả: Auto-generated for chinese-bootcamp project
"""

import re
import json
import csv
import os
import sys
import hashlib
from pathlib import Path
from dataclasses import dataclass, field, asdict
from typing import Optional

# Fix Unicode output on Windows
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


# ─── Config ──────────────────────────────────────────────────────────────────

BASE_DIR = Path(__file__).parent
WEEK_DIRS = sorted(BASE_DIR.glob("week*/"))
OUTPUT_DIR = BASE_DIR / "grammar_output"

# Các file cần bỏ qua
SKIP_FILES = {
    "07_day7_review.md", "07_day7_assessment.md",
    "07_day7_hsk1_mock.md", "07_day7_hsk2_mock.md",
    "07_day7_graduation.md", "07_day7_hsk3_mini.md",
}

# ─── Data Model ──────────────────────────────────────────────────────────────

@dataclass
class GrammarCard:
    """Một thẻ Anki ngữ pháp."""
    note_id: str           # MD5 hash để dedup trong Anki
    day: str               # "Day 5"
    week: str              # "Week 1"
    day_num: int           # 5
    week_num: int          # 1
    grammar_name: str      # "想 vs 要"
    grammar_meaning: str   # "Muốn (mức độ khác nhau)"
    pattern: str           # "想 + V = muốn nhẹ | 要 + V = muốn mạnh"
    examples: str          # Full ví dụ text
    notes: str             # Lưu ý, phân biệt
    dev_tip: str           # 💡 Dev tip
    exercise: str          # 🏋️ bài tập
    source_file: str       # Đường dẫn file gốc
    tags: str              # "week2::grammar::comparison"


# ─── Regex Patterns ───────────────────────────────────────────────────────────

# Header ngữ pháp chính: ## 📐 Phần N: Ngữ Pháp — TÊN (25 phút)
RE_GRAMMAR_HEADER = re.compile(
    r'^## 📐 Phần \d+: Ngữ Pháp[— –-]+(.+?)(?:\s*\(\d+ phút\))?$',
    re.MULTILINE
)

# Bất kỳ level-2 heading nào để xác định kết thúc section
RE_ANY_H2 = re.compile(r'^## ', re.MULTILINE)

# ###-level sub-heading (Pattern, Ví dụ, So sánh...)
RE_H3 = re.compile(r'^### (.+)$', re.MULTILINE)

# Code block
RE_CODE_BLOCK = re.compile(r'```(.*?)```', re.DOTALL)

# Dev tip
RE_DEV_TIP = re.compile(
    r'> 💡 \*\*Dev tip.*?\*\*:?\s*(.+?)(?=\n\n|\n>|\Z)',
    re.DOTALL
)

# Exercise / Thực hành
RE_EXERCISE = re.compile(
    r'### 🏋️ Thực hành.*?\n(.*?)(?=\n###|\n##|\Z)',
    re.DOTALL
)

# <details> answer block — để lấy đáp án bài tập
RE_DETAILS = re.compile(r'<details>.*?</details>', re.DOTALL)

# Day/Week info từ dòng đầu file
RE_DAY_TITLE = re.compile(r'^# Day (\d+):', re.MULTILINE)
RE_WEEK_LINE = re.compile(r'Tuần (\d+)[^—\n]*(?:—|–|-)\s*Ngày \d+', re.IGNORECASE)


# ─── Helpers ─────────────────────────────────────────────────────────────────

def clean_text(text: str) -> str:
    """Làm sạch text: bỏ leading/trailing whitespace, normalize newlines."""
    text = text.strip()
    # Giảm nhiều dòng trắng liên tiếp xuống còn 2
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text


def extract_examples_from_code_blocks(section_text: str) -> str:
    """Trích xuất nội dung trong tất cả code block của section."""
    blocks = RE_CODE_BLOCK.findall(section_text)
    if not blocks:
        return ""
    return "\n---\n".join(b.strip() for b in blocks if b.strip())


def extract_dev_tip(section_text: str) -> str:
    """Trích xuất 💡 Dev tip."""
    m = RE_DEV_TIP.search(section_text)
    if not m:
        return ""
    tip = m.group(1).strip()
    # Bỏ markdown styling
    tip = re.sub(r'\*\*(.+?)\*\*', r'\1', tip)
    return tip


def extract_exercise(section_text: str) -> str:
    """Trích xuất phần bài tập (nếu có)."""
    m = RE_EXERCISE.search(section_text)
    if not m:
        return ""
    ex = m.group(1).strip()
    # Loại bỏ đáp án <details>
    ex = RE_DETAILS.sub("[Đáp án ẩn]", ex)
    return clean_text(ex)


def extract_notes(section_text: str) -> str:
    """
    Trích xuất các lưu ý quan trọng:
    - ⚠️ warnings
    - > blockquote (không phải dev tip)
    - So sánh trực tiếp (bảng | )
    """
    notes_parts = []

    # ⚠️ warnings
    warnings = re.findall(r'⚠️.*', section_text)
    if warnings:
        notes_parts.extend(warnings)

    # Các blockquote không phải dev tip
    blockquotes = re.findall(r'^> (?!💡)(.+)$', section_text, re.MULTILINE)
    if blockquotes:
        notes_parts.extend(blockquotes)

    # Bảng markdown ─ lấy nguyên 
    tables = re.findall(r'(\|.+\|\n(?:\|[-: |]+\|\n)?(?:\|.+\|\n)*)', section_text)
    if tables:
        notes_parts.extend(t.strip() for t in tables)

    return clean_text("\n\n".join(notes_parts))


def parse_grammar_name(raw_name: str) -> tuple[str, str]:
    """
    Tách tên ngữ pháp thành (grammar_name, grammar_meaning).
    Input: "想 vs 要 (Muốn)"
    Output: ("想 vs 要", "Muốn")
    """
    # Tìm phần trong dấu ngoặc cuối: (nghĩa)
    m = re.match(r'^(.+?)\s*\(([^)]+)\)\s*$', raw_name)
    if m:
        return m.group(1).strip(), m.group(2).strip()
    return raw_name.strip(), ""


def extract_pattern_formula(section_text: str) -> str:
    """
    Tìm dòng công thức/pattern cú pháp.
    Ưu tiên: ### Pattern: ... hoặc dòng đầu trong code block đầu tiên.
    """
    # ### Pattern: ...
    m = re.search(r'### (?:Pattern.*?:|Cách \d+:|\.\.\.):?\s*(.+)$', section_text, re.MULTILINE)
    if m:
        return m.group(1).strip()

    # Sub-heading pattern kiểu "### Cách 1: thêm 吗 cuối câu"
    m = re.search(r'### (.+)', section_text)
    if m:
        val = m.group(1)
        # Bỏ thời gian
        val = re.sub(r'\(\d+ phút\)', '', val).strip()
        return val

    return ""


# ─── Main Extraction ─────────────────────────────────────────────────────────

def extract_grammar_from_file(filepath: Path) -> list[GrammarCard]:
    """Trích xuất tất cả grammar card từ một file bài học."""
    cards = []
    content = filepath.read_text(encoding='utf-8', errors='replace')

    # Lấy thông tin Day/Week
    m_day = RE_DAY_TITLE.search(content)
    day_num = int(m_day.group(1)) if m_day else 0
    day_str = f"Day {day_num}" if day_num else filepath.stem

    m_week = RE_WEEK_LINE.search(content)
    week_num = int(m_week.group(1)) if m_week else 0
    week_str = f"Week {week_num}" if week_num else filepath.parent.name

    # Tìm tất cả grammar section headers
    grammar_matches = list(RE_GRAMMAR_HEADER.finditer(content))
    if not grammar_matches:
        return cards

    # Tìm tất cả H2 để xác định ranh giới section
    all_h2_positions = [m.start() for m in RE_ANY_H2.finditer(content)]

    for gm in grammar_matches:
        raw_name = gm.group(1).strip()
        # Loại bỏ thời gian nếu còn
        raw_name = re.sub(r'\s*\(\d+ phút\)\s*$', '', raw_name)

        grammar_name, grammar_meaning = parse_grammar_name(raw_name)

        # Xác định vị trí bắt đầu và kết thúc của section
        section_start = gm.start()
        # Tìm H2 tiếp theo sau section này
        next_h2 = next(
            (pos for pos in all_h2_positions if pos > section_start),
            len(content)
        )
        section_text = content[section_start:next_h2]

        # Extract các thành phần
        examples = extract_examples_from_code_blocks(section_text)
        dev_tip = extract_dev_tip(section_text)
        exercise = extract_exercise(section_text)
        notes = extract_notes(section_text)
        pattern_formula = extract_pattern_formula(section_text)

        # Build tags
        tags = [
            f"week{week_num}",
            f"day{day_num}",
            "grammar",
        ]
        # Thêm tag theo loại ngữ pháp
        name_lower = grammar_name.lower()
        if 'vs' in name_lower or '比较' in grammar_name:
            tags.append("comparison")
        if '?' in grammar_name or '吗' in grammar_name or '什么' in grammar_name:
            tags.append("question")
        if '了' in grammar_name:
            tags.append("aspect")
        if '被' in grammar_name or '把' in grammar_name:
            tags.append("special-structure")

        # NoteID = MD5 của week+day+name để Anki update đúng thẻ
        note_id = hashlib.md5(
            f"{week_num}_{day_num}_{grammar_name}".encode('utf-8')
        ).hexdigest()[:16]

        card = GrammarCard(
            note_id=note_id,
            day=day_str,
            week=week_str,
            day_num=day_num,
            week_num=week_num,
            grammar_name=grammar_name,
            grammar_meaning=grammar_meaning,
            pattern=pattern_formula,
            examples=clean_text(examples),
            notes=clean_text(notes),
            dev_tip=clean_text(dev_tip),
            exercise=clean_text(exercise),
            source_file=str(filepath.relative_to(BASE_DIR)),
            tags="::".join(tags),
        )
        cards.append(card)

    return cards


def process_all_weeks() -> list[GrammarCard]:
    """Duyệt qua tất cả các tuần và extract grammar cards."""
    all_cards = []

    for week_dir in WEEK_DIRS:
        week_files = sorted(week_dir.glob("*.md"))
        for f in week_files:
            if f.name.startswith("0") and f.name not in SKIP_FILES:
                # Chỉ lấy bài học chính (0X_day...), bỏ qua overview/assessment
                if "overview" in f.name or "assessment" in f.name or "report" in f.name:
                    continue
                if "review" in f.name.lower() and "day7" in f.name.lower():
                    continue
                cards = extract_grammar_from_file(f)
                if cards:
                    print(f"  ✅ {f.parent.name}/{f.name}: {len(cards)} grammar card(s)")
                    all_cards.extend(cards)
                else:
                    print(f"  ⚪ {f.parent.name}/{f.name}: no grammar section")

    return all_cards


# ─── Output Writers ──────────────────────────────────────────────────────────

def write_tsv(cards: list[GrammarCard], out_path: Path):
    """
    Xuất TSV để import vào Anki.
    Cột theo thứ tự fields của Note Type.
    """
    fieldnames = [
        "NoteID", "Day", "Week", "GrammarName", "GrammarMeaning",
        "Pattern", "Examples", "Notes", "DevTip", "Exercise", "Tags"
    ]

    with open(out_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter='\t', quoting=csv.QUOTE_ALL)
        f.write("#separator:tab\n")
        f.write("#html:false\n")
        f.write(f"#columns:{','.join(fieldnames)}\n")

        for c in cards:
            writer.writerow([
                c.note_id, c.day, c.week, c.grammar_name, c.grammar_meaning,
                c.pattern, c.examples, c.notes, c.dev_tip, c.exercise, c.tags
            ])

    print(f"\n📄 TSV saved: {out_path}")


def write_json(cards: list[GrammarCard], out_path: Path):
    """Xuất JSON đầy đủ."""
    data = [asdict(c) for c in cards]
    out_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f"📄 JSON saved: {out_path}")


def write_preview_md(cards: list[GrammarCard], out_path: Path):
    """Xuất Markdown preview để kiểm tra kết quả trước khi import."""
    lines = ["# Grammar Cards Preview\n"]
    lines.append(f"> **Tổng số thẻ:** {len(cards)}\n\n---\n")

    for i, c in enumerate(cards, 1):
        lines.append(f"## {i}. {c.grammar_name}")
        if c.grammar_meaning:
            lines.append(f"> {c.grammar_meaning}")
        lines.append(f"\n**📅 {c.day} · {c.week}**  \n**Tags:** `{c.tags}`\n")

        if c.pattern:
            lines.append(f"**Pattern:** `{c.pattern}`\n")

        if c.examples:
            lines.append("**Ví dụ:**")
            lines.append("```")
            lines.append(c.examples[:500] + ("..." if len(c.examples) > 500 else ""))
            lines.append("```\n")

        if c.notes:
            lines.append(f"**Lưu ý:** {c.notes[:300]}\n")

        if c.dev_tip:
            lines.append(f"**💡 Dev Tip:** {c.dev_tip[:200]}\n")

        if c.exercise:
            lines.append(f"**🏋️ Bài tập:** _(có)_\n")

        lines.append(f"\n_Source: `{c.source_file}`_\n")
        lines.append("\n---\n")

    out_path.write_text("\n".join(lines), encoding='utf-8')
    print(f"📄 Preview saved: {out_path}")


# ─── Entry Point ─────────────────────────────────────────────────────────────

def main():
    OUTPUT_DIR.mkdir(exist_ok=True)

    print("🔍 Đang quét các bài học...\n")
    all_cards = process_all_weeks()

    # Sắp xếp theo tuần rồi ngày
    all_cards.sort(key=lambda c: (c.week_num, c.day_num))

    print(f"\n✅ Tổng cộng: {len(all_cards)} grammar cards từ {len(WEEK_DIRS)} tuần\n")

    # Ghi output
    write_tsv(all_cards, OUTPUT_DIR / "grammar_cards.tsv")
    write_json(all_cards, OUTPUT_DIR / "grammar_cards.json")
    write_preview_md(all_cards, OUTPUT_DIR / "grammar_preview.md")

    # Thống kê
    print("\n📊 Thống kê theo tuần:")
    from collections import Counter
    week_count = Counter(c.week for c in all_cards)
    for w, cnt in sorted(week_count.items()):
        print(f"  {w}: {cnt} card(s)")

    print("\n✨ Done! Kiểm tra grammar_output/ để xem kết quả.")
    print("   → grammar_preview.md  — xem trước nội dung")
    print("   → grammar_cards.tsv   — import vào Anki")


if __name__ == "__main__":
    main()
