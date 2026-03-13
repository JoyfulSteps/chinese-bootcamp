# Day 43: Đọc Blog Juejin Thật + 只要...就
## Tuần 7 — Ngày 1 (Day 43) | Thứ Hai 21/4/2026

---

## 🎯 Mục Tiêu Ngày 43
| Mục Tiêu | Chi Tiết | Đo lường |
|----------|----------|----------|
| Ngữ pháp: 只要...就 | Chỉ cần...thì/là... | 6 câu |
| Đọc blog thật | Juejin bài thật 250 chữ | ≥ 45% hiểu |
| Tech advanced vocab | Architecture, microservice | 13 từ mới |
| Tổng tích lũy | **473 từ / 278 Hán tự / 30 NP** | — |

---

## 📐 Phần 1: Ngữ Pháp — 只要...就 (20 phút)

### Pattern: 只要 A 就 B = Chỉ cần A thì B

```
只要 zhǐyào = chỉ cần     就 jiù = thì/liền

只要你每天练习，中文就会进步。
Chỉ cần bạn luyện mỗi ngày, TQ sẽ tiến bộ.

只要代码没有bug，就可以上线。
Chỉ cần code không có bug, có thể go live.

只要有网络，就能工作。
Chỉ cần có mạng, là làm việc được.
```

### Tech examples:
```
只要测试通过，就可以合并。
Chỉ cần test pass, có thể merge.

只要配置正确，系统就能正常运行。
Chỉ cần config đúng, system chạy bình thường.

只要学会了基础，框架就容易了。
Chỉ cần biết foundation, framework dễ thôi.

只要重启服务器，问题就解决了。
Chỉ cần restart server, vấn đề giải quyết.
```

> 💡 **Dev tip:** `只要...就` = `if (condition) { result; }` — điều kiện ĐỦ! Một điều kiện → chắc chắn ra kết quả.

---

## 📖 Phần 2: Đọc Blog Thật — Juejin Style (30 phút)

### Bài Đọc — Mô phỏng bài Juejin thật (250 chữ)

```
# 微服务架构入门指南

大家好，我是一个后端开发，做了六年微服务。
今天给大家分享一下微服务架构的基础知识。

## 什么是微服务？
微服务就是把一个大的应用拆分成多个小的服务。
每个服务独立运行，独立部署。服务之间通过
接口通信。

## 微服务的优点
1. **独立部署**：只要修改了一个服务，就只需要
   部署那一个，不影响其他服务。
2. **技术多样**：不同的服务可以用不同的编程语言。
   前端用Node.js，后端用Java，数据处理用Python。
3. **容易扩展**：哪个服务压力大，就单独扩展。

## 微服务的挑战
但是微服务也有问题。服务之间的通信变复杂了。
需要处理分布式事务、服务发现、负载均衡等。
对于小团队来说，微服务的运维成本比较高。

## 我的建议
只要项目规模不大，就不建议用微服务。单体
架构更简单，维护成本更低。只要团队人数超过
二十人，或者系统越来越复杂，才考虑微服务。

不管你选择什么架构，最重要的是适合你的团队
和项目需求。

👍 觉得有帮助就点个赞吧！
```

### Đọc Hiểu:
| # | 问题 | Đáp án |
|---|------|--------|
| 1 | 微服务是什么？ | <details><summary>🔑</summary>把大应用拆分成多个小服务</details> |
| 2 | 微服务有什么优点？(3个) | <details><summary>🔑</summary>独立部署、技术多样、容易扩展</details> |
| 3 | 微服务有什么挑战？ | <details><summary>🔑</summary>通信复杂、分布式事务、运维成本高</details> |
| 4 | 作者建议什么时候用微服务？ | <details><summary>🔑</summary>团队超过20人或系统越来越复杂</details> |
| 5 | 最重要的是什么？ | <details><summary>🔑</summary>适合团队和项目需求</details> |

**Đọc hiểu: ___/5**

---

## 📖 Phần 3: 13 Từ Vựng Mới (25 phút)

> Tổng tích lũy sau Day 43: **473 từ**

| # | Hán tự | Pinyin | Nghĩa | Câu ví dụ |
|---|--------|--------|-------|-----------|
| 461 | **只要** | zhǐyào | chỉ cần | 只要努力就行。 |
| 462 | **架构** | jiàgòu | kiến trúc | 微服务架构。 |
| 463 | **拆分** | chāifēn | tách/split | 拆分成小服务。 |
| 464 | **独立** | dúlì | độc lập | 独立部署。 |
| 465 | **通信** | tōngxìn | truyền thông | 服务之间通信。 |
| 466 | **扩展** | kuòzhǎn | mở rộng/scale | 容易扩展。 |
| 467 | **压力** | yālì | áp lực | 服务器压力大。 |
| 468 | **维护** | wéihù | bảo trì | 维护成本。 |
| 469 | **规模** | guīmó | quy mô | 项目规模。 |
| 470 | **处理** | chǔlǐ | xử lý | 处理请求。 |
| 471 | **通过** | tōngguò | thông qua | 测试通过。 |
| 472 | **指南** | zhǐnán | hướng dẫn | 入门指南。 |
| 473 | **单独** | dāndú | riêng/đơn độc | 单独部署。 |

---

## 🗣️ Phần 4: Hội Thoại — Thảo Luận Architecture (15 phút)
```
A: 你觉得我们应该用微服务还是单体架构？
B: 对于我们的项目来说，现在规模不大，
   我建议先用单体。
A: 如果以后用户越来越多呢？
B: 只要系统压力变大，我们就可以把一些
   服务拆分出来。不用一开始就用微服务。
A: 有道理。那数据库呢？
B: 先用一个MySQL就够了。只要做好索引优化，
   性能不会有问题。
A: 好的，我同意你的方案。
```
> 🎤 Shadowing 5 lần。

---

## ✏️ Phần 5: 8 Hán Tự Mới (20 phút)

#### 构 gòu (cấu) — 8 nét
```
架构 = kiến trúc, 结构 = cấu trúc, 构建 = xây dựng
Tập viết: 构 构 构 构 构 构 构 构 构 构
```
#### 拆 chāi (tách) — 8 nét
```
拆分 = tách/split
Tập viết: 拆 拆 拆 拆 拆 拆 拆 拆 拆 拆
```
#### 独 dú (độc) — 9 nét
```
独立 = độc lập, 单独 = riêng
Tập viết: 独 独 独 独 独 独 独 独 独 独
```
#### 扩 kuò (khoách) — 6 nét
```
扩展 = mở rộng/scale
Tập viết: 扩 扩 扩 扩 扩 扩 扩 扩 扩 扩
```
#### 维 wéi (duy) — 11 nét
```
维护 = bảo trì, 思维 = tư duy
Tập viết: 维 维 维 维 维 维 维 维 维 维
```
#### 护 hù (hộ) — 7 nét
```
维护 = bảo trì, 保护 = bảo vệ
Tập viết: 护 护 护 护 护 护 护 护 护 护
```
#### 规 guī (quy) — 8 nét
```
规模 = quy mô, 规则 = quy tắc
Tập viết: 规 规 规 规 规 规 规 规 规 规
```
#### 模 mó (mô) — 14 nét
```
规模 = quy mô, 模型 = mô hình/model
Tập viết: 模 模 模 模 模 模 模 模 模 模
```

---

## 📋 Checklist
- [ ] 只要A就B = chỉ cần A thì B
- [ ] 架构 拆分 独立 通信 扩展 压力 维护 规模 处理 通过 指南 单独
- [ ] Đọc blog 250 chữ + 🎧 Nghe 45p + Anki 13 mới

---
## 📂 Navigation
| ← Trước | Đang học | Tiếp → |
|---------|----------|--------|
| [00_week7_overview.md](./00_week7_overview.md) | **01_day1_real_blog.md** | [02_day2_interview.md](./02_day2_interview.md) |
