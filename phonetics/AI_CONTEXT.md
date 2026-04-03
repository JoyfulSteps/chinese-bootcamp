# 🚀 Chinese Phonetics Anki Workflow - Hướng dẫn tiếp tục

File này chứa toàn bộ context để AI khác (hoặc chính tôi trên máy cá nhân) hiểu luồng công việc hiện tại, các quyết định đã đưa ra và cách tiếp tục dự án tạo thẻ Anki học phiên âm tiếng Trung.

## 🎯 Mục tiêu dự án
Tạo một hệ thống hoàn toàn tự động để học phiên âm Pinyin qua ứng dụng Anki, sử dụng 1 video dạy phát âm dài (của cô Vũ Hà). Thay vì xem thụ động, AI tóm tắt nội dung cực kỳ chi tiết, cắt nhỏ clip và tự động import vào Anki bằng Python.

## 📁 Cấu trúc thư mục hiện tại (`d:\Chinese\bootcamp\phonetics\`)
- `Học phát âm tiếng Trung.mp4`: File video gốc 30 phút.
- `timestamps.csv`: Bảng mapping thời gian cắt các clip 1 cách chính xác.
- `cut_video.py`: Script dùng ffmpeg cắt video dựa vào timestamps. (ĐÃ CẮT XONG 61 CLIPS VÀO THƯ MỤC `clips/`).
- `anki_card/`: Chứa template front.html, back.html, style.css cho thẻ học (Pinyin Phonetics note type).
- `anki_phonetics_sync.py`: Script (Dùng AnkiConnect) tự sinh thẻ vào Anki.
- `output/`: Thư mục lưu các file markdown (MD) do AI sinh ra chứa nội dung các thẻ.

## 📌 Context: Đã làm được gì?
1. **Lên ý tưởng thẻ:** Đã chốt thẻ chia làm 3 loại (Âm đơn, So sánh cặp, Tổng quan nhóm) với nội dung rất chi tiết (không chỉ cắt clip mà thêm phiên âm IPA, Trick, Warning tránh nhầm lẫn,...).
2. **Template Anki:** Đạt thiết kế theo phong cách modern light theme. Chú trọng UX: Mặt trước chỉ có câu hỏi, không video (tránh spoiler); mặt sau có đầy đủ video, ghi chú.
3. **Gen nội dung:** Đã viết xong TOÀN BỘ file markdown chi tiết (.md) cho các Pinyin vào thư mục `output/`. (Thực hiện cách gộp nhóm các âm vào chung các file lớn: `batch_van_mau_don.md`, `batch_thanh_dieu.md`, `batch_thanh_mau_1.md` -> 2, 3... ). Phân tách bởi chuỗi `===SOUND===`.
4. **Cắt Video:** Lệnh `python phonetics/cut_video.py --include-practice` đã chạy thành công, sinh ra 61 video ngắn trong mục `clips/`.

## ⏭️ Bước tiếp theo cần làm ngay (Import vào Anki)
Khi bạn chạy trên máy cá nhân, tất cả file markdown đã gen xong, video đã cắt. Bạn chỉ cần:
1. Mở Anki (nhớ cài addon AnkiConnect)
2. Mở Terminal tại gốc thư mục dự án và chạy sync:
   ```bash
   cd d:\Chinese\bootcamp
   python phonetics/anki_phonetics_sync.py
   ```
   *Note: Bước này ở đoạn chat trước đã bị lỗi do AnkiConnect từ chối kết nối (vì Anki có thể đang bị tắt).*

---

## 🎨 QUAN TRỌNG: Template & Nội dung chuẩn (Nếu cần gen tiếp âm mới)
Phần nội dung này phải bắt buộc giữ y nguyên form thiết lập, một mẫu chuẩn gồm 9 thành phần sau:

**Mỗi phần âm thanh phân cách bằng chuỗi `===SOUND===` .**

**📝 Dưới đây là ví dụ chuẩn cho thẻ Vận mẫu "e" (tất cả các âm mới phải làm giống form này):**

```markdown
Cách phát âm **e** /ɤ/ chuẩn nhất:

📍 Phân loại:
- **Nhóm:** Vận mẫu đơn (单韵母 — Simple Finals)
- **IPA:** /ɤ/
- **Độ khó:** ⭐⭐

❌ KHÔNG PHẢI:
- ❌ KHÔNG phải "e" tiếng Việt

✅ THỰC SỰ LÀ:
- ≈ **"ưa/ơ"** tiếng Việt, miệng mở ngang

🏋️ CÁCH LUYỆN:
1. Nói **"ơ"** tiếng Việt
2. Kéo 2 khóe miệng ngang

🧪 Tự kiểm tra: Nghe giống "ơ" mới chuẩn.

🔀 SO SÁNH / DỄ NHẦM:
| Âm | Cách đọc | 
|:---:|----------|
| **e** | ≈ "ơ/ưa" | 

📝 QUY TẮC ĐẶC BIỆT:
- e sau i đọc là iê

🎯 TỪ MẪU:
| Hán tự | Pinyin | Nghĩa | Ghi chú |
|:------:|--------|-------|---------|
| **喝** | hē | uống | e đơn = "ơ" |

⚠️ LỖI PHỔ BIẾN:
- ❌ Đọc "e" Trung thành "e" Việt

🧠 TRICK NHỚ:
- 😮‍💨 **"Ơ mà cười"**

👨‍👩‍👧 GIA ĐÌNH ÂM:
- e đơn: hē
- e kép: xiě

---META---
Pinyin: e
IPA: /ɤ/
Type: Vận mẫu đơn
Category: Nguyên âm đơn · 单韵母
Difficulty: ⭐⭐
Compare_With: "e" tiếng Việt
Teacher_Note: Lưỡi rút về sau, mồm há vừa. Gần giống ưa.
Video_File: van_mau_don_e.mp4
```

---

## 💡 Nhắc nhở cho AI mới đọc file này
- Bạn không cần làm lại file `timestamps.csv` hay viết lại `cut_video.py`.
- Nếu được yêu cầu **sửa HTML/CSS Anki card**, đảm bảo sửa xong phải có step tự sync (hướng dẫn user chạy script python).
- Tránh thay đổi cấu trúc của parser đọc `---META---`. File `.md` luôn phải có metadata block dùng syntax 3 dấu gạch.
- Nếu phải sinh lại nội dung MD bị thiếu, **bắt buộc dùng đúng 9 section** được đề cập ở trên.
