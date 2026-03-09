# 📘 Phương Pháp Học Writing Hoàn Chỉnh
## Tài liệu hướng dẫn AI tạo khóa học Writing cho ngôn ngữ mới

> **Mục đích:** Tổng hợp TẤT CẢ phương pháp, cấu trúc, quy trình đã được sử dụng thành công trong khóa học Vietnamese Foundation + English Foundation → IELTS 7.0. Dùng làm **blueprint** để nhân bản sang ngôn ngữ khác (ví dụ: tiếng Trung).

---

## 📑 Mục Lục

1. [Triết Lý Tổng Quan](#-1-triết-lý-tổng-quan)
2. [Kiến Trúc Khóa Học](#-2-kiến-trúc-khóa-học)
3. [Cấu Trúc Thư Mục & Đánh Số File](#-3-cấu-trúc-thư-mục--đánh-số-file)
4. [Nội Dung Chi Tiết Từng Phase](#-4-nội-dung-chi-tiết-từng-phase)
5. [Flow Tạo Bài Giảng](#-5-flow-tạo-bài-giảng)
6. [Flow Review & Chữa Bài](#-6-flow-review--chữa-bài)
7. [Workflow Templates (Prompt cho AI)](#-7-workflow-templates)
8. [Anki Integration](#-8-anki-integration)
9. [Đánh Giá & Theo Dõi Tiến Độ](#-9-đánh-giá--theo-dõi-tiến-độ)

---

## 🧠 1. Triết Lý Tổng Quan

### Vấn đề gốc rễ
Người học viết câu đơn giản **ngay cả bằng tiếng mẹ đẻ** → Không thể viết phong phú bằng tiếng nước ngoài.

### Giải pháp: **L1 First Approach** (Ngôn ngữ mẹ đẻ trước)
```
PHASE 1: Vietnamese Foundation (3 tuần)
    → Học TƯ DUY viết phong phú bằng tiếng Việt
    → Câu → Đoạn → Bài luận
    
PHASE 2: English Foundation (1 tuần)  
    → Chuyển đổi tư duy sang tiếng Anh
    → Sentence Patterns → Paragraph → Essay
    
PHASE 3: IELTS Writing (8 tuần)
    → Luyện đề theo format IELTS
    → Task 1 + Task 2
```

### 4 Nguyên tắc cốt lõi
| # | Nguyên Tắc | Chi Tiết |
|---|-----------|----------|
| 1 | **Thực hành > Lý thuyết** | 80% viết, 20% đọc hướng dẫn |
| 2 | **Chất lượng > Số lượng** | 1 câu viết kỹ > 10 câu qua loa |
| 3 | **Tích lũy dần** | Mỗi ngày thêm 1 kỹ năng, không cố học hết |
| 4 | **Tự đánh giá** | Cuối mỗi ngày review, cuối tuần assessment |

---

## 🏗️ 2. Kiến Trúc Khóa Học

### Mô hình 3 cấp: Câu → Đoạn → Bài luận

```
📊 PROGRESSION MODEL (áp dụng cho MỌI ngôn ngữ)

TUẦN 1: CÂU - Từ Đơn Giản Đến Phong Phú
    ├── Day 1-2: Mở rộng câu (thêm 5 lớp thông tin)
    ├── Day 3-4: Biến đổi cấu trúc (8 cách biến đổi 1 câu)
    ├── Day 5-6: Diễn đạt đa dạng (7 góc nhìn cho 1 ý)
    └── Day 7: Ôn tập + Viết đoạn văn đầu tiên

TUẦN 2: ĐOẠN VĂN - Kết Nối Ý Tưởng
    ├── Day 1-2: Logic Flow (câu sau phản hồi câu trước)
    ├── Day 3-4: 20 Từ Nối (6 nhóm chức năng)
    ├── Day 5-6: PEEL Structure (Point-Explain-Example-Link)
    └── Day 7: Ôn tập + Bài 300 từ

TUẦN 3: BÀI LUẬN - Tổng Hợp & Áp Dụng
    ├── Day 1-2: Cấu trúc bài luận 5 đoạn
    ├── Day 3-4: 6 kỹ thuật lập luận thuyết phục
    ├── Day 5-6: Viết bài luận 500-600 từ
    └── Day 7: Đánh giá cuối + Chuẩn bị chuyển ngôn ngữ đích
```

### Thời gian học
| Block | Thời Gian | Nội Dung |
|-------|-----------|----------|
| Block 1 | 30-45 phút | Học kỹ năng mới |
| Block 2 | 60-75 phút | Thực hành viết + Nộp bài |
| Block 3 | 15-30 phút | AI review → Tự đánh giá |

---

## 📂 3. Cấu Trúc Thư Mục & Đánh Số File

### Quy tắc đánh số

```
📁 [language]_foundation/
│
├── 00_course_overview.md          ← Tổng quan khóa học
├── 01_assessment_baseline.md      ← Bài đánh giá ban đầu
├── 02_master_roadmap.md           ← Lộ trình 3 tuần
├── 03_skill_checklist.md          ← 46 kỹ năng cần đạt
├── 04_progress_tracker.md         ← Theo dõi tiến độ
│
├── 📁 week1/                      ← Folder mỗi tuần
│   ├── 00_week1_overview.md       ← Overview tuần
│   ├── 01_day1_[skill].md         ← Bài giảng Day 1
│   ├── 02_day2_[skill].md         ← Bài giảng Day 2
│   ├── ...
│   ├── 07_day7_[skill].md         ← Day 7
│   ├── week1_assessment_report.md ← Báo cáo cuối tuần
│   │
│   └── 📁 exercises/              ← Folder bài tập & feedback
│       ├── 01_day1_[type]_feedback.md    ← Feedback #1
│       ├── 02_day2_[type]_feedback.md    ← Feedback #2
│       ├── ...
│       └── 09_day7_summary.md            ← Tổng kết tuần
│
├── 📁 week2/
│   ├── (cấu trúc tương tự)
│   └── 📁 exercises/
│       ├── 10_w2d1_[type]_feedback.md    ← Đánh số tiếp tục!
│       ├── 11_w2d1_[type]_feedback.md
│       └── ...
│
└── 📁 week3/
    └── (tương tự)
```

### Quy tắc đặt tên file

| Loại File | Format | Ví Dụ |
|-----------|--------|-------|
| **Bài giảng** | `NN_dayX_[skill_name].md` | `01_day1_sentence_expansion.md` |
| **Overview tuần** | `00_weekN_overview.md` | `00_week2_overview.md` |
| **Feedback** | `NN_wXdY_[type]_feedback.md` | `15_w2d4_exercise1_feedback.md` |
| **Assessment** | `weekN_assessment_report.md` | `week1_assessment_report.md` |

> **QUAN TRỌNG:** Số thứ tự feedback **LIÊN TỤC** xuyên suốt khóa học (01 → 02 → ... → 17 → 18...), KHÔNG reset theo tuần.

---

## 📖 4. Nội Dung Chi Tiết Từng Phase

### TUẦN 1: CÂU - Kỹ năng cần dạy

#### Day 1-2: Mở Rộng Câu (5 Lớp Thông Tin)

Từ câu ngắn, thêm dần các lớp:

| Lớp | Câu Hỏi | Ví Dụ (tiếng Việt) |
|-----|---------|---------------------|
| **Lớp 1** | AI? CÁI GÌ? | Công nghệ giúp học sinh |
| **Lớp 2** | NHƯ THẾ NÀO? | ...học tập **hiệu quả hơn** |
| **Lớp 3** | Ở ĐÂU? KHI NÀO? | ...**ở vùng sâu vùng xa**...trong **thời đại số** |
| **Lớp 4** | TẠI SAO? | ...**nhờ khả năng tiếp cận nguồn tài liệu** |
| **Lớp 5** | VÍ DỤ? | ...**chẳng hạn các khóa học trên Coursera** |

**Bài tập:** 10 câu ngắn → Mở rộng qua 5 lớp (= 50 câu)

#### Day 3-4: Biến Đổi Cấu Trúc (8 Cách)

Từ **1 câu gốc**, biến đổi thành 8 kiểu:

| # | Kiểu | Ví Dụ |
|---|------|-------|
| 1 | **Đảo ngữ** | Giới trẻ chịu ảnh hưởng lớn từ MXH |
| 2 | **Bị động** | Giới trẻ bị ảnh hưởng bởi MXH |
| 3 | **Trạng ngữ đầu** | Trong thời đại số, MXH ảnh hưởng... |
| 4 | **Câu hỏi tu từ** | Liệu ai phủ nhận ảnh hưởng của MXH? |
| 5 | **Nhấn mạnh** | Chính MXH là yếu tố ảnh hưởng lớn nhất |
| 6 | **Phủ định kép** | Không thể không thừa nhận ảnh hưởng... |
| 7 | **So sánh** | MXH ảnh hưởng hơn bất kỳ phương tiện nào |
| 8 | **Câu ghép** | MXH không chỉ ảnh hưởng tâm lý mà còn thay đổi hành vi |

**Bài tập:** 5 câu × 8 kiểu = 40 câu biến đổi

#### Day 5-6: Diễn Đạt Đa Dạng (7 Góc Nhìn)

| # | Góc Nhìn | Mô Tả |
|---|----------|-------|
| 1 | **Khẳng định trực tiếp** | Nêu thẳng quan điểm |
| 2 | **Phủ định ngược** | "Không thể phủ nhận rằng..." |
| 3 | **Nêu hệ quả** | "Nếu không có X thì..." |
| 4 | **So sánh tương đồng** | "X quan trọng như Y..." |
| 5 | **Ví dụ cụ thể** | "Điển hình như..." |
| 6 | **Góc nhìn lịch sử** | "Từ xa xưa..." |
| 7 | **Đặt câu hỏi** | "Liệu cuộc sống có thể...?" |

**Bài tập:** 5 ý × 7 cách = 35 diễn đạt

#### Day 7: Ôn Tập + Viết Đoạn Đầu Tiên (100-120 từ)

---

### TUẦN 2: ĐOẠN VĂN - Kỹ năng cần dạy

#### Day 1-2: Logic Flow
- Câu sau phải **PHẢN HỒI** câu trước (giải thích, ví dụ, hệ quả, đối lập)

#### Day 3-4: 20 Từ Nối (6 Nhóm)

| Nhóm | Màu | Từ Nối |
|------|-----|--------|
| 🟢 Thêm Ý | Xanh | Hơn nữa, Ngoài ra, Bên cạnh đó, Đặc biệt là |
| 🟡 Tương Phản | Vàng | Tuy nhiên, Mặt khác, Ngược lại |
| 🔴 Kết Quả | Đỏ | Do đó, Vì vậy, Kết quả là |
| 🟣 Ví Dụ | Tím | Chẳng hạn như, Ví dụ điển hình là, Có thể kể đến |
| 🔵 Nhấn Mạnh | Xanh dương | Đặc biệt, Quan trọng hơn cả, Điều đáng chú ý |
| ⚫ Kết Luận | Đen | Tóm lại, Nhìn chung, Có thể thấy rằng |

#### Day 5-6: PEEL Structure

```
P - POINT      → Luận điểm (1 câu, 15-20 từ)
E - EXPLAIN    → Giải thích TẠI SAO (1-2 câu, 25-35 từ)
E - EXAMPLE    → Ví dụ + SEN (2-3 câu, 40-50 từ)
L - LINK       → Liên kết về Point (1 câu, 15-25 từ)
```

**Công thức SEN cho Example:**
| Chữ | Ý Nghĩa | Ví Dụ |
|-----|---------|-------|
| **S** - Số liệu | Con số cụ thể | 70%, 1.5 tỷ |
| **E** - Example | Tên tổ chức/người | Google, Harvard |
| **N** - Nguồn | Cơ quan uy tín | WHO, UNESCO |

#### Day 7: Bài 300 từ (4 đoạn: Mở + PEEL 1 + PEEL 2 + Kết)

---

### TUẦN 3: BÀI LUẬN

#### Day 1-2: Cấu trúc 5 đoạn
```
Đoạn 1: MỞ BÀI (50-60 từ) - Bối cảnh + Thesis
Đoạn 2: THÂN BÀI 1 (80-100 từ) - PEEL
Đoạn 3: THÂN BÀI 2 (80-100 từ) - PEEL
Đoạn 4: THÂN BÀI 3 (optional/phản biện)
Đoạn 5: KẾT BÀI (50-60 từ) - Tóm tắt + Mở rộng
```

#### Day 3-4: 6 Kỹ Thuật Lập Luận
1. Dẫn chứng số liệu
2. So sánh tương đồng
3. Phản biện trước
4. Câu hỏi tu từ
5. Nêu hệ quả
6. Trích dẫn chuyên gia

#### Day 5-7: Viết bài 500-600 từ + Đánh giá cuối

---

## 🔄 5. Flow Tạo Bài Giảng

### Mỗi bài giảng (file Day) phải có:

```markdown
# Day X: [Tên Kỹ Năng]
## Tuần Y - Ngày X

## 🎯 Mục Tiêu Ngày X
| Mục Tiêu | Chi Tiết |
|----------|----------|
| ... | ... |

## 📚 Phần Lý Thuyết (20-30 phút)
- Giải thích kỹ năng
- Bảng so sánh/ví dụ
- Mẫu câu tham khảo (10+ mẫu theo chủ đề)

## 📋 Bài Tập 1: [Tên] (X phút)
- Yêu cầu rõ ràng
- Template để điền
- Số lượng cụ thể

## 📋 Bài Tập 2: [Tên] (X phút)
(tương tự)

## 📋 Bài Tập 3: [Tên] (X phút)  
(bài tổng hợp, khó hơn)

## 📋 Checklist Cuối Ngày
- [ ] Kiến thức
- [ ] Bài tập hoàn thành
- [ ] Tự đánh giá

## 🎯 Chuẩn Bị Ngày Sau

## 📁 Navigation
| File | Nội Dung |
|------|----------|
| `prev_file.md` | ← Quay lại |
| `current_file.md` | **ĐANG HỌC** |
| `next_file.md` | Ngày tiếp → |
```

---

## ✍️ 6. Flow Review & Chữa Bài

### Quy trình chữa bài

```
1. Học sinh nộp bài viết
       ↓
2. AI đọc bài + chọn workflow phù hợp
       ↓
3. Tạo file feedback theo template
       ↓
4. File feedback gồm các phần:
   📊 Tổng Quan (bảng điểm)
   ✍️ Chi Tiết Từng Câu (phân tích lỗi + sửa)
   📊 So Sánh Gốc vs Thay Thế
   📋 Tổng Hợp Lỗi
   🔑 Quy Tắc Cần Nhớ
   🏆 Câu Hay Nhất (khen)
   ✅ Checklist Bài Sau
   📈 So Sánh Tiến Bộ (so với bài trước)
```

### Template chi tiết cho MỖI CÂU:

```markdown
### Câu [X]: [Tên kỹ thuật]

**📝 Bài của bạn:**
> "[câu gốc của học sinh - NGUYÊN VĂN]"

**❌ Lỗi:**
| Vị Trí | Lỗi | Giải Thích |
|--------|-----|------------|
| "[từ/cụm sai]" | [loại lỗi] | [tại sao sai] |

**✅ CÂU THAY THẾ (Sửa câu của bạn):**
> "[Sửa câu gốc, giữ ý, chỉ sửa lỗi + nâng cấp]"

**✅ CÂU MẪU CỦA TÔI (Tham khảo):**
> "[Câu MỚI HOÀN TOÀN, cùng chủ đề, hay hơn, có số liệu]"

**💡 So sánh / Điểm hay:**
- [Giải thích tại sao câu mẫu tốt hơn]

**Status:** ✅ ĐÚNG / ⚠️ LỖI NHỎ / ❌ SAI
```

### 2 loại câu sửa (QUAN TRỌNG):

| Loại | Mục Đích | Quy Tắc |
|------|----------|---------|
| **CÂU THAY THẾ** | Sửa câu gốc, giữ ý | Bám sát câu gốc, chỉ sửa lỗi + nâng cấp nhẹ |
| **CÂU MẪU CỦA TÔI** | Câu MỚI HOÀN TOÀN | Viết câu khác về cùng chủ đề, thường có số liệu, trình độ IELTS 7.0 |

---

## 🤖 7. Workflow Templates

### Các workflow đã tạo (trong `.agent/workflows/`):

| Workflow | Dùng Khi | Trọng Tâm |
|----------|---------|------------|
| `vietnamese-writing-tutor.md` | Review bài tiếng Việt | Câu thay thế + Câu mẫu (không có Vocab Bank EN) |
| `ielts-writing-tutor.md` | Review bài tiếng Anh | Câu thay thế + IELTS 7.0 + Vocabulary Bank |
| `model-answer-generator.md` | Tạo đáp án mẫu | Vocabulary Bank + đáp án IELTS 7.0 |
| `ielts-assessment.md` | Đánh giá cuối tuần/khóa | Bảng điểm chi tiết, so sánh |
| `ielts-resource-creator.md` | Tạo tài liệu học | Bài giảng, bài tập |
| `ielts-sample-analyzer.md` | Phân tích bài mẫu | Mining patterns từ Band 7-8 |
| `ielts-tutorial-creator.md` | Tạo hướng dẫn | Lý thuyết + bài tập |

### Cấu trúc workflow file:

```yaml
---
description: [Mô tả ngắn]
---

# Tên Workflow

## 🎯 ROLE & CONTEXT
## 📋 LEARNER PROFILE
## 🔄 WHEN TO USE
## 📄 FEEDBACK FILE STRUCTURE
   ### 1️⃣ HEADER
   ### 2️⃣ SESSION OVERVIEW
   ### 3️⃣ CHI TIẾT TỪNG CÂU (quan trọng nhất)
   ### 4️⃣ BẢNG SO SÁNH
   ### 5️⃣ TỔNG HỢP LỖI
   ### 6️⃣ QUY TẮC CẦN NHỚ
   ### 7️⃣ CÂU HAY NHẤT
   ### 8️⃣ CHECKLIST
## 🎯 QUALITY STANDARDS
## 📝 EXAMPLE
## 🚀 START PROMPT
```

---

## 🎴 8. Anki Integration

### Note Type "Writing Pattern Practice"

**10 Fields:**

| # | Field | Nội Dung |
|---|-------|----------|
| 1 | PatternName | Tên bài/pattern |
| 2 | PatternFormula | Công thức/cấu trúc |
| 3 | Hints | Gợi ý ngắn: `fan → air`, `I → mouse` |
| 4 | TypeAnswer | Field để gõ câu trả lời (type & compare) |
| 5 | CorrectSentences | Các câu đúng |
| 6 | OriginalSentences | Các câu gốc (có lỗi) |
| 7 | ModelSentences | Câu mẫu IELTS 7.0 |
| 8 | ErrorSummary | Bảng tổng hợp lỗi (HTML table) |
| 9 | PriorityFocus | Trọng tâm cần sửa |
| 10 | Score | Điểm phiên học |

### Cách dùng Anki:
- **1 card = 1 phiên học** (không phải 1 card/câu)
- **Mặt trước:** Pattern + Hints → gõ câu trả lời
- **Mặt sau:** So sánh + Câu mẫu + Lỗi + Điểm
- Theme: Dark/sáng, glassmorphism, color-coded sections

---

## 📊 9. Đánh Giá & Theo Dõi Tiến Độ

### Bảng điểm mỗi feedback

```markdown
## 📊 Tổng Quan

| Phần | ✅ Đúng | ⚠️ Lỗi nhỏ | ❌ Sai |
|------|--------|------------|-------|
| [Kiểu 1] | X | X | X |
| **TỔNG** | **X** | **X** | **X** |

**Điểm: X/10**
```

### So sánh tiến bộ (cuối mỗi feedback):

```markdown
## 📈 So Sánh Tiến Bộ

| Bài Tập | Điểm | Nhận Xét |
|---------|------|----------|
| W2D3 BT2 | 7/10 | Lỗi: ngược lại/tuy nhiên |
| W2D4 BT1 | 7/10 | Sai từ nối yêu cầu |
| **BÀI NÀY** | **6.5/10** | Dài, thiếu SEN |
```

### Skill Checklist (46 kỹ năng):
- `[ ]` Chưa học
- `[/]` Đang học  
- `[x]` Đã thành thạo
- Kèm **Evidence** (ví dụ câu chứng minh)

### Assessment cuối tuần:
- So sánh điểm tuần trước vs tuần này
- Checklist kỹ năng đã đạt
- Hành động cho tuần tiếp

---

## 🎯 Các Lỗi Phổ Biến Đã Phát Hiện (Tham Khảo)

| Loại Lỗi | Mô Tả | Mức |
|-----------|--------|-----|
| Viết thường đầu câu | "mạng" thay vì "Mạng" | ⚠️ |
| Đại từ mơ hồ "Nó" | "Nó giống như..." → viết rõ danh từ | ⚠️ |
| Thiếu SEN | Ví dụ không có số liệu/nguồn | ❌ |
| Nhầm Explain ↔ Example | Liệt kê thay vì giải thích TẠI SAO | ❌ |
| Lặp từ/nghĩa | "Bởi vì nhờ", "phổ biến và rộng rãi" | ⚠️ |
| Cấu trúc câu sai | Câu thiếu vị ngữ hoàn chỉnh | ❌ |
| Comma splice | Nối 2 mệnh đề bằng dấu phẩy | ⚠️ |
| Diễn đạt cứng | "việc xuất hiện công nghệ" | ⚠️ |

---

## 💡 Cách Áp Dụng Sang Ngôn Ngữ Khác (vd: Tiếng Trung)

### Bước 1: Tạo cấu trúc tương tự
```
📁 chinese_foundation/
├── 00_course_overview.md
├── 01_assessment_baseline.md
├── 02_master_roadmap.md
├── 03_skill_checklist.md
├── 04_progress_tracker.md
├── 📁 week1/ (Câu)
├── 📁 week2/ (Đoạn)
└── 📁 week3/ (Bài luận)
```

### Bước 2: Điều chỉnh nội dung cho ngôn ngữ đích
- **Tuần 1:** 5 lớp thông tin, 8 biến đổi, 7 góc nhìn → áp dụng cho tiếng Trung
- **Tuần 2:** Từ nối tiếng Trung, PEEL bằng tiếng Trung
- **Tuần 3:** Bài luận tiếng Trung

### Bước 3: Tạo workflow chữa bài
- Copy `vietnamese-writing-tutor.md` → sửa thành `chinese-writing-tutor.md`
- Giữ nguyên cấu trúc feedback, thay ngôn ngữ

### Bước 4: Chạy flow
```
Học sinh đọc bài giảng → Làm bài tập → Nộp bài
          ↓
AI dùng workflow → Tạo file feedback
          ↓
Học sinh đọc feedback → Làm bài tiếp
          ↓
(Lặp lại cho đến hết tuần)
```
