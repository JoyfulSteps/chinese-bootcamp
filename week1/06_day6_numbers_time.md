# Day 6: Số Đếm Nâng Cao, Ngày Tháng & Giờ
## Tuần 1 — Ngày 6 | Thứ Bảy 15/3/2026

---

## 🎯 Mục Tiêu Ngày 6

| Mục Tiêu | Chi Tiết | Đo lường |
|----------|----------|----------|
| Đếm 1–100+ | Quy tắc số lớn: mười, trăm | Đếm bất kỳ |
| Ngày tháng năm | Nói ngày hôm nay bằng TQ | Nói đúng |
| Nói giờ | Mấy giờ rồi? Giờ + phút | 5 mốc giờ |
| Thứ trong tuần | Thứ 2 → CN | Kể đúng 7 thứ |
| Ngữ pháp: 几/多少 | Hỏi số lượng | Đặt 5 câu |
| Học 14 từ mới | Tổng tích lũy: 70 từ 🎯 | Anki test |
| Viết 5 Hán tự mới | Tổng tích lũy: 30 chữ 🎯 | Viết đúng |

---

## 📚 Phần 1: Số Đếm 11–100+ (20 phút)

### Quy tắc tạo số

```
Tiếng Trung đếm rất logic — giống viết code!

11–19: 十 + số đơn vị
  11 = 十一    shí yī
  12 = 十二    shí èr
  15 = 十五    shí wǔ
  19 = 十九    shí jiǔ

20–99: chục + 十 + đơn vị
  20 = 二十    èr shí           (2 × 10)
  25 = 二十五  èr shí wǔ        (2 × 10 + 5)
  38 = 三十八  sān shí bā       (3 × 10 + 8)
  50 = 五十    wǔ shí           (5 × 10)
  99 = 九十九  jiǔ shí jiǔ      (9 × 10 + 9)

100+:
  100 = 一百   yì bǎi
  200 = 两百 / 二百   liǎng bǎi
  365 = 三百六十五    sān bǎi liù shí wǔ
  1000 = 一千  yì qiān
  10000 = 一万 yí wàn

⚠️ 二 vs 两: đếm dùng 二, đo lường/số lượng dùng 两
  第二 (thứ 2) = dùng 二
  两个人 (2 người) = dùng 两
```

> 💡 **Dev tip:** `number = (chục × 十) + đơn vị`. Thuần tuý concatenation, giống `toString()` nhưng mỗi chữ số là 1 word!

**🎯 Luyện đếm:**
```
10 → 20 → 30 → 40 → 50 → 60 → 70 → 80 → 90 → 100
shí → èr shí → sān shí → sì shí → wǔ shí → liù shí → qī shí → bā shí → jiǔ shí → yì bǎi

Random: 27 → 43 → 68 → 91 → 55 → 82 → 14 → 76
```

---

## 📚 Phần 2: Ngày Tháng Năm (25 phút)

### Năm 年 nián

```
2026年 = èr líng èr liù nián (đọc từng số!)
         2  0   2  6   năm

⚠️ Năm đọc TỪNG SỐ, không đọc "hai ngàn không trăm hai mươi sáu"
```

### Tháng 月 yuè

```
一月 yī yuè   = tháng 1     七月 qī yuè   = tháng 7
二月 èr yuè   = tháng 2     八月 bā yuè   = tháng 8
三月 sān yuè  = tháng 3     九月 jiǔ yuè  = tháng 9
四月 sì yuè   = tháng 4     十月 shí yuè  = tháng 10
五月 wǔ yuè   = tháng 5     十一月 shíyī yuè = tháng 11
六月 liù yuè  = tháng 6     十二月 shíèr yuè = tháng 12

Siêu đơn giản: số + 月!
```

### Ngày 号 hào (口语) / 日 rì (sách vở)

```
一号 yī hào = ngày 1     ...     十五号 shíwǔ hào = ngày 15
二号 èr hào = ngày 2     ...     三十一号 sānshíyī hào = ngày 31
```

### Thứ trong tuần 星期 xīngqī

```
星期一   xīngqī yī    Thứ Hai
星期二   xīngqī èr    Thứ Ba
星期三   xīngqī sān   Thứ Tư
星期四   xīngqī sì    Thứ Năm
星期五   xīngqī wǔ    Thứ Sáu
星期六   xīngqī liù   Thứ Bảy
星期天/日 xīngqī tiān  Chủ Nhật

Đơn giản: 星期 + số! (CN đặc biệt = 天 hoặc 日)
```

### 🎤 Thực hành: Nói ngày hôm nay

```
今天是2026年3月15号，星期六。
Jīntiān shì èr líng èr liù nián sān yuè shíwǔ hào, xīngqī liù.
Hôm nay là ngày 15 tháng 3 năm 2026, thứ Bảy.
```

> Nói to 5 lần!

---

## 📚 Phần 3: Giờ 点 diǎn & Phút 分 fēn (25 phút)

### Nói giờ

```
Cấu trúc: 数字 + 点 = ___ giờ

一点    yī diǎn     1 giờ
两点    liǎng diǎn  2 giờ (dùng 两 không phải 二!)
三点    sān diǎn    3 giờ
...
十二点  shíèr diǎn  12 giờ

Buổi:
  早上   zǎoshang    sáng (6–9)
  上午   shàngwǔ     trước trưa (9–12)
  中午   zhōngwǔ     trưa (12)
  下午   xiàwǔ       chiều (12–18)
  晚上   wǎnshang    tối (18+)
```

### Nói phút

```
Cấu trúc: 数字 + 点 + 数字 + 分 = _giờ _phút

三点十五分  sān diǎn shíwǔ fēn  3:15 (3 giờ 15 phút)
八点三十分  bā diǎn sānshí fēn  8:30
十点零五分  shí diǎn líng wǔ fēn 10:05 (có 零 cho số < 10!)

Đặc biệt:
  半 bàn = nửa → 三点半 sān diǎn bàn = 3:30
  一刻 yí kè = 15 phút → 三点一刻 = 3:15
```

### Hỏi giờ

```
Q: 现在几点？    Xiànzài jǐ diǎn?    Bây giờ mấy giờ?
A: 现在三点半。  Xiànzài sān diǎn bàn. Bây giờ 3:30.
```

---

## 📐 Phần 4: Ngữ Pháp — 几 jǐ vs 多少 duōshao (15 phút)

```
几 jǐ — hỏi số NHỎ (1–10), dùng với lượng từ
  你几岁？           Nǐ jǐ suì?          Bạn mấy tuổi? (trẻ em)
  几个人？           Jǐ ge rén?           Mấy người?
  几点？             Jǐ diǎn?             Mấy giờ?
  今天星期几？       Jīntiān xīngqī jǐ?   Hôm nay thứ mấy?

多少 duōshao — hỏi số LỚN hoặc không biết phạm vi
  你多大？           Nǐ duō dà?           Bao nhiêu tuổi? (người lớn)
  多少钱？           Duōshao qián?         Bao nhiêu tiền?
  多少人？           Duōshao rén?          Bao nhiêu người?
```

> 💡 **Dev tip:** `几` = `small int` query (expect 1–10). `多少` = `any number` query.

---

## 📖 Phần 5: 14 Từ Vựng Mới (30 phút)

> 🎯 Tổng tích lũy sau Day 6: **70 từ** — Đạt mục tiêu tuần!

| # | Hán tự | Pinyin | Nghĩa | Ghi nhớ |
|---|--------|--------|-------|---------|
| 57 | **今天** | jīntiān | hôm nay | 今 (nay) + 天 (ngày) |
| 58 | **明天** | míngtiān | ngày mai | 明 (sáng/rõ) + 天 |
| 59 | **昨天** | zuótiān | hôm qua | 昨 (hôm qua) + 天 |
| 60 | **年** | nián | năm | 2026年 |
| 61 | **月** | yuè | tháng/trăng | 三月 = tháng 3 |
| 62 | **号/日** | hào/rì | ngày | 15号 = ngày 15 |
| 63 | **星期** | xīngqī | tuần/thứ | 星期一 = thứ Hai |
| 64 | **点** | diǎn | giờ (o'clock) | 三点 = 3 giờ |
| 65 | **分** | fēn | phút | 十分 = 10 phút |
| 66 | **半** | bàn | nửa | 三点半 = 3:30 |
| 67 | **现在** | xiànzài | bây giờ | 现在几点？ |
| 68 | **百** | bǎi | trăm | 一百 = 100 |
| 69 | **两** | liǎng | hai (đếm) | 两个 = 2 cái |
| 70 | **多** | duō | nhiều | 多少 = bao nhiêu |

### Câu thực hành

```
今天是星期六。         Jīntiān shì xīngqī liù.     Hôm nay thứ Bảy.
明天是星期天。         Míngtiān shì xīngqī tiān.    Ngày mai Chủ Nhật.
现在几点？             Xiànzài jǐ diǎn?              Bây giờ mấy giờ?
现在三点半。           Xiànzài sān diǎn bàn.         Bây giờ 3:30.
你今天去哪里？         Nǐ jīntiān qù nǎli?          Hôm nay bạn đi đâu?
今天几号？             Jīntiān jǐ hào?               Hôm nay ngày mấy?
今天三月十五号。       Jīntiān sān yuè shíwǔ hào.    Hôm nay 15/3.
他有两百块钱。         Tā yǒu liǎng bǎi kuài qián.  Anh có 200 đồng.
```

---

## ✏️ Phần 6: 5 Hán Tự Mới (25 phút)

#### 天 tiān (trời/ngày) — 4 nét
```
一 (ngang) + 大 (lớn) = 天
"Trên đại = TRỜI"
Tập viết: 天 天 天 天 天 天 天 天 天 天
```

#### 月 yuè (trăng/tháng) — 4 nét
```
Hình trăng lưỡi liềm
Tập viết: 月 月 月 月 月 月 月 月 月 月
```

#### 日 rì (mặt trời/ngày) — 4 nét
```
Hình mặt trời (hình vuông + nét ngang giữa)
Tập viết: 日 日 日 日 日 日 日 日 日 日
```

#### 今 jīn (nay/hiện tại) — 4 nét
```
亻(người) biến thể + 一 + ... → "bây giờ"
Tập viết: 今 今 今 今 今 今 今 今 今 今
```

#### 明 míng (sáng/rõ) — 8 nét
```
日 (mặt trời) + 月 (trăng) = 明 (SÁNG)
"Mặt trời + trăng = sáng" — chữ Hán logic tuyệt vời!
Tập viết: 明 明 明 明 明 明 明 明 明 明
```

---

## 📋 Checklist Cuối Ngày 6

### Kiến thức
- [ ] Đếm 1–100 không cần nghĩ
- [ ] Nói ngày tháng năm bằng tiếng Trung
- [ ] Nói giờ + phút
- [ ] 7 thứ trong tuần
- [ ] 几 vs 多少

### Thực hành
- [ ] Nói ngày hôm nay bằng TQ (năm + tháng + ngày + thứ)
- [ ] Nói 5 mốc giờ bất kỳ
- [ ] Đếm 10 → 100 (nhảy 10)
- [ ] Anki: 14 mới + review 56 cũ
- [ ] Viết 5 Hán tự mới

### Tự đánh giá
- [ ] Đếm số: ___/5
- [ ] Nói ngày giờ: ___/5
- [ ] Nhớ 14 từ mới: ___/14
- ⭐ Đánh giá ngày: ___/5

---

## 📂 Navigation
| ← Trước | Đang học | Tiếp → |
|---------|----------|--------|
| [05_day5_basic_greetings.md](./05_day5_basic_greetings.md) | **06_day6_numbers_time.md** | [07_day7_review_assessment.md](./07_day7_review_assessment.md) |
