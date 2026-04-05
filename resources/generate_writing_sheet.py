#!/usr/bin/env python3
"""
汉字练习册生成器 — Chinese Hanzi Writing Practice Sheet Generator
================================================================
Generates print-ready A4 PDF worksheets with 田字格 (Tiánzìgé) grids
using 田英章硬笔楷书 calligraphy font for model characters.

Usage:
    python generate_writing_sheet.py                          # Default 20 basic chars
    python generate_writing_sheet.py -c "你好世界天地"         # Specify characters
    python generate_writing_sheet.py -f characters.txt        # Read from file
    python generate_writing_sheet.py -c "你好" -r 3           # 3 rows per character
    python generate_writing_sheet.py -c "学习中文" --no-pinyin # Without pinyin
"""

import os
import sys
import glob
import argparse
from pathlib import Path

from fpdf import FPDF
from pypinyin import pinyin, Style

# ─── Paths ────────────────────────────────────────────────────────────────────
SCRIPT_DIR = Path(__file__).parent
KAISHU_FONT_DIR = SCRIPT_DIR / "田英章硬笔楷书简体"
XINGSHU_FONT_DIR = SCRIPT_DIR / "司马彦简行修正版"
OUTPUT_DIR = SCRIPT_DIR / "writing_sheets"

# ─── Page Setup (A4, portrait) ────────────────────────────────────────────────
PAGE_W = 210   # mm
PAGE_H = 297   # mm
MARGIN_L = 12
MARGIN_R = 12
MARGIN_T = 15
MARGIN_B = 12

# ─── Grid Setup ───────────────────────────────────────────────────────────────
CELL_SIZE = 20          # mm per grid cell
PINYIN_GAP = 7          # mm above grid for pinyin text
ROW_GAP = 2             # mm between rows
COLS = 9                # total columns: 1 model + 2 trace + 6 empty
TRACE_COLS = 2          # number of light trace columns after model
USABLE_W = PAGE_W - MARGIN_L - MARGIN_R  # 186mm

# ─── Colors (RGB) ─────────────────────────────────────────────────────────────
CLR_GRID_BORDER  = (180, 180, 180)     # grid outer border
CLR_GRID_GUIDE   = (210, 215, 220)     # inner cross guides (dashed)
CLR_MODEL_CHAR   = (40, 40, 45)        # model character (near-black)
CLR_TRACE_CHAR   = (215, 218, 222)     # trace character (very light)
CLR_PINYIN       = (120, 120, 130)     # pinyin text
CLR_TITLE        = (50, 55, 65)        # page title
CLR_SUBTITLE     = (140, 140, 150)     # subtitle / footer
CLR_HEADER_LINE  = (80, 130, 200)      # decorative header accent


def find_ttf(font_dir: Path) -> str | None:
    """Auto-detect .ttf font file in a directory (handles garbled filenames)."""
    if not font_dir.exists():
        return None
    for f in font_dir.iterdir():
        if f.suffix.lower() == ".ttf":
            return str(f)
    return None


def get_pinyin(char: str) -> str:
    """Get pinyin with tone marks for a single character."""
    try:
        result = pinyin(char, style=Style.TONE)
        return result[0][0] if result else ""
    except Exception:
        return ""


class HanziPracticeSheet(FPDF):
    """Custom PDF generator for Chinese character writing practice."""

    def __init__(self, font_path: str, title: str = "汉字书写练习",
                 show_pinyin: bool = True):
        super().__init__(orientation="P", unit="mm", format="A4")
        self.title_text = title
        self.show_pinyin = show_pinyin
        self._font_path = font_path
        self._page_count = 0

        # Register calligraphy font
        self.add_font("Kaishu", "", font_path)

        self.set_auto_page_break(auto=False)
        self.set_margins(MARGIN_L, MARGIN_T, MARGIN_R)

    # ── Header ────────────────────────────────────────────────────────────
    def _draw_header(self):
        """Draw page title and decorative line."""
        # Title
        self.set_font("Kaishu", "", 18)
        self.set_text_color(*CLR_TITLE)
        self.set_xy(MARGIN_L, MARGIN_T)
        self.cell(USABLE_W, 10, self.title_text, align="C")

        # Accent line under title
        line_y = MARGIN_T + 12
        self.set_draw_color(*CLR_HEADER_LINE)
        self.set_line_width(0.6)
        center = PAGE_W / 2
        self.line(center - 40, line_y, center + 40, line_y)

        # Thin secondary lines
        self.set_line_width(0.2)
        self.set_draw_color(*CLR_GRID_GUIDE)
        self.line(center - 60, line_y, center - 42, line_y)
        self.line(center + 42, line_y, center + 60, line_y)

    # ── Footer ────────────────────────────────────────────────────────────
    def _draw_footer(self):
        """Draw page number at the bottom."""
        self._page_count += 1
        self.set_font("Kaishu", "", 8)
        self.set_text_color(*CLR_SUBTITLE)
        footer_text = f"— {self._page_count} —"
        self.set_xy(MARGIN_L, PAGE_H - MARGIN_B)
        self.cell(USABLE_W, 5, footer_text, align="C")

    # ── Grid Drawing ──────────────────────────────────────────────────────
    def _draw_tianzige(self, x: float, y: float, size: float,
                       is_model: bool = False):
        """Draw a single 田字格 cell with cross guide lines."""
        # Outer border
        border_clr = CLR_HEADER_LINE if is_model else CLR_GRID_BORDER
        self.set_draw_color(*border_clr)
        self.set_line_width(0.4 if is_model else 0.25)
        self.rect(x, y, size, size)

        # Inner dashed cross guides
        self.set_draw_color(*CLR_GRID_GUIDE)
        self.set_line_width(0.15)

        mid_x = x + size / 2
        mid_y = y + size / 2

        # Horizontal dashed line
        dash_len = 1.2
        gap_len = 1.2
        cx = x + 0.5
        while cx < x + size - 0.5:
            end = min(cx + dash_len, x + size - 0.5)
            self.line(cx, mid_y, end, mid_y)
            cx += dash_len + gap_len

        # Vertical dashed line
        cy = y + 0.5
        while cy < y + size - 0.5:
            end = min(cy + dash_len, y + size - 0.5)
            self.line(mid_x, cy, mid_x, end)
            cy += dash_len + gap_len

    def _put_char_in_cell(self, x: float, y: float, size: float,
                          char: str, color: tuple):
        """Place a character centered in a grid cell."""
        font_size = size * 1.35  # pt, slightly smaller than cell
        self.set_font("Kaishu", "", font_size)
        self.set_text_color(*color)

        # Use cell for centering
        self.set_xy(x, y + 0.5)
        self.cell(size, size, char, align="C")

    # ── Row Drawing ───────────────────────────────────────────────────────
    def _draw_row(self, y_top: float, char: str):
        """Draw a complete practice row for one character.

        Layout: [pinyin] then [MODEL | TRACE | TRACE | empty × 6]
        """
        x_start = MARGIN_L
        grid_y = y_top + (PINYIN_GAP if self.show_pinyin else 0)

        # ── Pinyin annotation ──
        if self.show_pinyin:
            py = get_pinyin(char)
            self.set_font("Kaishu", "", 9)
            self.set_text_color(*CLR_PINYIN)
            self.text(x_start + 1, y_top + PINYIN_GAP - 1.5, py)

        # ── Grid cells ──
        for col in range(COLS):
            x = x_start + col * CELL_SIZE
            is_model = (col == 0)
            self._draw_tianzige(x, grid_y, CELL_SIZE, is_model=is_model)

            if col == 0:
                # Model character — full color
                self._put_char_in_cell(x, grid_y, CELL_SIZE,
                                       char, CLR_MODEL_CHAR)
            elif col <= TRACE_COLS:
                # Trace characters — very light for tracing over
                self._put_char_in_cell(x, grid_y, CELL_SIZE,
                                       char, CLR_TRACE_CHAR)
            # Remaining cells are empty for free practice

        return grid_y + CELL_SIZE

    # ── Main Generation ───────────────────────────────────────────────────
    def generate(self, characters: list[str], rows_per_char: int = 2):
        """Generate the full practice PDF."""
        row_height = CELL_SIZE + (PINYIN_GAP if self.show_pinyin else 0) + ROW_GAP
        content_start_y = MARGIN_T + 18  # after header
        usable_h = PAGE_H - content_start_y - MARGIN_B - 5
        rows_per_page = int(usable_h / row_height)

        # Build list of (char, repetition) pairs
        all_rows = []
        for char in characters:
            for _ in range(rows_per_char):
                all_rows.append(char)

        # Generate pages
        for i, char in enumerate(all_rows):
            page_row = i % rows_per_page

            if page_row == 0:
                if i > 0:
                    self._draw_footer()
                self.add_page()
                self._draw_header()

            y = content_start_y + page_row * row_height
            self._draw_row(y, char)

        # Final page footer
        self._draw_footer()


def load_characters_from_file(filepath: str) -> list[str]:
    """Load characters from a text file.

    Supports formats:
      - One character per line
      - Multiple characters per line (each char extracted)
      - Lines starting with # are comments
      - Empty lines are skipped
    """
    chars = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            # Extract only CJK characters
            for ch in line:
                if "\u4e00" <= ch <= "\u9fff" or "\u3400" <= ch <= "\u4dbf":
                    chars.append(ch)
    return chars


def main():
    parser = argparse.ArgumentParser(
        description="Generate Chinese character writing practice sheets (PDF)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python generate_writing_sheet.py                        # Default 20 basic chars
  python generate_writing_sheet.py -c "你好世界"           # Specify characters
  python generate_writing_sheet.py -f characters.txt      # Read from file
  python generate_writing_sheet.py -c "学习" -r 3         # 3 rows per character
  python generate_writing_sheet.py -c "大小" --no-pinyin  # Without pinyin
        """,
    )
    parser.add_argument("-c", "--characters", type=str,
                        help="Characters to practice (e.g. '你好世界')")
    parser.add_argument("-f", "--file", type=str,
                        help="Text file with characters (one per line or grouped)")
    parser.add_argument("-r", "--rows", type=int, default=2,
                        help="Practice rows per character (default: 2)")
    parser.add_argument("-o", "--output", type=str, default=None,
                        help="Output PDF filename (default: auto-generated)")
    parser.add_argument("-t", "--title", type=str,
                        default="汉字书写练习",
                        help="Sheet title")
    parser.add_argument("--no-pinyin", action="store_true",
                        help="Hide pinyin annotations")
    parser.add_argument("--font", choices=["kaishu", "xingshu"],
                        default="kaishu",
                        help="Font style: kaishu (楷书, default) or xingshu (行书)")
    args = parser.parse_args()

    # ── Find font ──
    font_dir = KAISHU_FONT_DIR if args.font == "kaishu" else XINGSHU_FONT_DIR
    font_path = find_ttf(font_dir)
    if not font_path:
        print(f"❌ ERROR: Cannot find .ttf font in: {font_dir}")
        print("   Make sure the font directories exist alongside this script.")
        sys.exit(1)
    font_name = "田英章楷书" if args.font == "kaishu" else "司马彦行书"
    print(f"✅ Font: {font_name}")

    # ── Get characters ──
    if args.file:
        chars = load_characters_from_file(args.file)
        if not chars:
            print(f"❌ No characters found in: {args.file}")
            sys.exit(1)
        source = f"file: {args.file}"
    elif args.characters:
        chars = [ch for ch in args.characters
                 if "\u4e00" <= ch <= "\u9fff" or "\u3400" <= ch <= "\u4dbf"]
        source = "command line"
    else:
        # Default: essential beginner characters
        chars = list("一二三四五六七八九十大小人口日月水火山木")
        source = "default (20 basic characters)"

    print(f"✅ Characters ({len(chars)}): {''.join(chars)}")
    print(f"   Source: {source}")
    print(f"   Rows per character: {args.rows}")
    total_rows = len(chars) * args.rows
    print(f"   Total rows: {total_rows}")

    # ── Output path ──
    OUTPUT_DIR.mkdir(exist_ok=True)
    if args.output:
        out_name = args.output
    else:
        # Auto-name based on first few chars
        sample = "".join(chars[:6])
        out_name = f"practice_{sample}.pdf"
    output_path = OUTPUT_DIR / out_name

    # ── Generate PDF ──
    print(f"\n📝 Generating PDF...")
    pdf = HanziPracticeSheet(
        font_path=font_path,
        title=args.title,
        show_pinyin=not args.no_pinyin,
    )
    pdf.generate(chars, rows_per_char=args.rows)
    pdf.output(str(output_path))

    file_size = output_path.stat().st_size / 1024
    print(f"✅ PDF saved: {output_path}")
    print(f"   Size: {file_size:.0f} KB")
    print(f"   Pages: {pdf._page_count}")
    print(f"\n🖨️  Ready to print! Open the PDF and print on A4 paper.")


if __name__ == "__main__":
    main()
