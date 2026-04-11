# 📐 Chinese Grammar Card — Cấu Trúc Fields

## Note Type: `Chinese Grammar Card`
## Deck: `Chinese Grammar::Week N`

---

## Fields

| # | Field | Nguồn | Mô tả |
|---|-------|-------|-------|
| 1 | `GrammarName` | grammar_extract.py | Tên pattern: `想 vs 要`, `从...到...` |
| 2 | `GrammarMeaning` | grammar_extract.py | Nghĩa tiếng Việt: `Muốn (mức độ)` |
| 3 | `Pattern` | grammar_extract.py | Công thức cú pháp: `S + 想 + V` |
| 4 | `Examples` | grammar_extract.py | Ví dụ đầy đủ (Hán + Pinyin + nghĩa) |
| 5 | `Notes` | grammar_extract.py | Lưu ý, ⚠️ cảnh báo, so sánh |
| 6 | `DevTip` | grammar_extract.py | 💡 Gợi nhớ bằng analogy lập trình |
| 7 | `Exercise` | grammar_extract.py | Bài tập điền từ từ bài học |
| 8 | `Day` | grammar_extract.py | `Day 12` |
| 9 | `Week` | grammar_extract.py | `Week 2` |
| 10 | `SourceFile` | grammar_extract.py | `week2\05_day5_daily_activities.md` |
| 11 | `Tags` | grammar_extract.py | `week2::day12::grammar::comparison` |

---

## Workflow Tự Động

```
1. grammar_extract.py     → grammar_output/grammar_cards.json
2. grammar_sync.py        → Anki (tạo/cập nhật notes)
```

### Các lệnh:

```powershell
# Bước 1 — Extract từ bài học
python -X utf8 grammar_extract.py

# Bước 2 — Sync vào Anki (Anki phải đang mở)
python grammar_sync.py

# Chỉ sync 1 tuần
python grammar_sync.py --week 3

# Cập nhật template thẻ (khi sửa front.html / back.html / style.css)
python grammar_sync.py --update-template

# Xây lại từ đầu (xóa tất cả rồi tạo lại)
python grammar_sync.py --rebuild

# Xem trước, không thay đổi Anki
python grammar_sync.py --dry-run
```

---

## Cấu Trúc Deck Anki

```
Chinese Grammar
├── Week 1   (4 cards: 是字句, 不vs没, 吗, 几vs多少)
├── Week 2   (7 cards: 的, 有, 在, 想vs要, 时候, 很, 太...了)
├── Week 3   (7 cards: 从..到, 比, 了, 给, 跟, 因为所以, 虽然但是)
├── Week 4   (6 cards: 正在, V过, 能可以会, 把, 被, 是..的)
├── Week 5   (2 cards: 除了以外, 不但而且)
├── Week 6   (3 cards: 越来越, 一边一边, 对..来说)
└── Week 7   (2 cards: 只要就, 不管都)
```

---

## Mặt Trước — Thiết Kế Đánh Đố

1. **Tên pattern** hiển thị to (câu trả lời chính)
2. **Fill-in-the-blank** — câu ví dụ đầu tiên với blank
3. Nút gợi ý nghĩa (ẩn/hiện)
4. Nút xem công thức (ẩn/hiện)

## Mặt Sau — 4 Tab

| Tab | Nội dung | Phím tắt |
|-----|----------|----------|
| 📖 Ví dụ | Tất cả ví dụ được parse sẵn | `1` |
| ⚠️ Lưu ý | Cảnh báo, quy tắc đặc biệt | `2` |
| 💡 Dev Tip | Analogy lập trình | `3` |
| 🏋️ Tập | Bài tập điền từ | `4` |
