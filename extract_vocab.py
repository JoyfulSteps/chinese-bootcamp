#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
"""
extract_vocab.py
----------------
Quét tất cả file bài học từ Day 22 trở đi (week4+),
tìm section "📖 Phần X: N Từ Vựng Mới" và lấy danh sách
Hán tự trong bảng từ vựng.

Output:
  - In ra màn hình: Day XX - TenBai   từ1, từ2, từ3, ...
  - Lưu file vocab_list.txt cùng thư mục
"""

import os
import re
import unicodedata

BOOTCAMP_DIR = os.path.dirname(os.path.abspath(__file__))

# Weeks cần quét (week4 trở đi = Day 22+)
WEEK_DIRS = ["week1", "week2", "week3", "week4", "week5", "week6", "week7", "week8"]


def slugify(text: str) -> str:
    """
    Chuyển tên bài thành đường dẫn folder hợp lệ.
    Ví dụ: "Trường Học, Học Tập & 正在 (Đang Làm)"
         → "Truong_Hoc_Hoc_Tap_va_Dang_Lam"
    """
    # Chuẩn hóa unicode → tách dấu
    nfkd = unicodedata.normalize("NFKD", text)
    # Giữ lại ký tự ASCII và Hán tự, bỏ combining marks
    result = []
    for ch in nfkd:
        cat = unicodedata.category(ch)
        # Bỏ combining diacritics (Mn)
        if cat == "Mn":
            continue
        result.append(ch)
    text = "".join(result)

    # Thay & → va, giữ Hán tự vì có thể muốn
    text = text.replace("&", "va").replace("，", " ").replace(",", " ")
    # Bỏ ký tự đặc biệt, giữ chữ cái, số, khoảng trắng, Hán tự
    text = re.sub(r"[^\w\s\u4e00-\u9fff]", " ", text, flags=re.UNICODE)
    # Thay nhiều khoảng trắng thành 1
    text = re.sub(r"\s+", "_", text.strip())
    # Bỏ underscore đầu/cuối
    text = text.strip("_")
    return text


def parse_day_title(filepath: str) -> tuple[int | None, str, str]:
    """
    Đọc dòng đầu file để lấy:
      - day_number (int)
      - title_raw  (str): "Trường Học, Học Tập & 正在"
      - folder_name (str): slug hợp lệ
    """
    with open(filepath, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            # Tìm dòng: # Day 22: Trường Học, Học Tập & 正在 (Đang Làm)
            m = re.match(r"^#\s+Day\s+(\d+)[:\s]+(.+)$", line, re.IGNORECASE)
            if m:
                day_num = int(m.group(1))
                title_raw = m.group(2).strip()
                # Bỏ phần trong ngoặc đơn nếu muốn rút gọn (tuỳ chọn)
                folder_name = slugify(title_raw)
                return day_num, title_raw, folder_name
            break  # Chỉ check dòng đầu tiên có nội dung
    return None, "", ""


def extract_vocab_from_file(filepath: str) -> list[str]:
    """
    Tìm section '📖 Phần X: N Từ Vựng Mới' (không phân biệt hoa thường)
    rồi lấy cột Hán tự từ bảng markdown bên dưới.
    
    Bảng có dạng:
    | # | Hán tự | Pinyin | Nghĩa | Câu ví dụ |
    |---|--------|--------|-------|-----------|
    | 227 | **正在** | zhèngzài | ... | ... |
    """
    vocab = []
    in_section = False
    in_table = False
    header_found = False

    with open(filepath, encoding="utf-8") as f:
        for line in f:
            stripped = line.strip()

            # Phát hiện section header: ## 📖 Phần X: N Từ Vựng Mới
            if re.search(r"từ\s*vựng\s*mới", stripped, re.IGNORECASE):
                in_section = True
                in_table = False
                header_found = False
                continue

            if not in_section:
                continue

            # Thoát section nếu gặp heading mới (##)
            if stripped.startswith("##") and in_section:
                break

            # Phát hiện bảng markdown
            if stripped.startswith("|"):
                parts = [p.strip() for p in stripped.split("|")]
                parts = [p for p in parts if p]  # bỏ phần tử rỗng

                if not header_found:
                    # Dòng header bảng — kiểm tra có cột "Hán tự" không
                    if any("hán tự" in p.lower() or "hanzi" in p.lower() or 
                           "hán" in p.lower() for p in parts):
                        header_found = True
                    in_table = True
                    continue

                # Bỏ dòng separator (---)
                if all(re.match(r"^[-:]+$", p) for p in parts):
                    continue

                # Dòng dữ liệu — cột Hán tự là cột 2 (index 1, sau cột #)
                if len(parts) >= 2:
                    hanzi_cell = parts[1]
                    # Bỏ **bold**
                    hanzi_cell = re.sub(r"\*+", "", hanzi_cell).strip()
                    # Chỉ lấy nếu cell chứa ít nhất 1 ký tự Hán
                    if re.search(r"[\u4e00-\u9fff]", hanzi_cell):
                        # Lấy token đầu tiên (tránh có text phụ)
                        token = hanzi_cell.split()[0] if hanzi_cell.split() else hanzi_cell
                        if re.search(r"[\u4e00-\u9fff]", token):
                            vocab.append(token)

    return vocab


def main():
    results = []

    for week in WEEK_DIRS:
        week_path = os.path.join(BOOTCAMP_DIR, week)
        if not os.path.isdir(week_path):
            continue

        # Lấy tất cả file .md, bỏ file overview và assessment
        md_files = sorted([
            f for f in os.listdir(week_path)
            if f.endswith(".md")
            and not f.startswith("00_")
            and "assessment" not in f.lower()
            and "overview" not in f.lower()
            and "report" not in f.lower()
        ])

        for fname in md_files:
            fpath = os.path.join(week_path, fname)
            day_num, title_raw, folder_name = parse_day_title(fpath)

            if day_num is None or day_num < 1:
                continue

            vocab = extract_vocab_from_file(fpath)

            results.append({
                "day": day_num,
                "title": title_raw,
                "folder": folder_name,
                "vocab": vocab,
                "file": os.path.relpath(fpath, BOOTCAMP_DIR),
            })

    # Sort by day number
    results.sort(key=lambda x: x["day"])

    # Build output lines
    lines = []
    for r in results:
        vocab_str = ", ".join(r["vocab"]) if r["vocab"] else "(khong tim thay)"
        header = f"Day {r['day']} - {r['title']}"
        folder_line = f"\t>> Folder: {r['folder']}"
        vocab_line = f"\t{vocab_str}"
        count_line = f"\t({len(r['vocab'])} tu) | File: {r['file']}"

        print(header)
        print(folder_line)
        print(vocab_line)
        print(count_line)
        print()

        lines.append(header)
        lines.append(folder_line)
        lines.append(vocab_line)
        lines.append(count_line)
        lines.append("")

    # Lưu ra file
    out_path = os.path.join(BOOTCAMP_DIR, "vocab_list.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"✅ Đã lưu kết quả vào: {out_path}")
    print(f"📊 Tổng: {len(results)} ngày có từ vựng mới")


if __name__ == "__main__":
    main()
