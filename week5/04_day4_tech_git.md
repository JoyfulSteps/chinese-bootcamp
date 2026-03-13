# Day 32: Tech — Git, DevOps & Workflow
## Tuần 5 — Ngày 4 (Day 32) | Thứ Năm 10/4/2026

---

## 🎯 Mục Tiêu Ngày 32
| Mục Tiêu | Chi Tiết | Đo lường |
|----------|----------|----------|
| Tech vocab: Git & DevOps | Commit, branch, merge, deploy | 13 từ mới |
| Đọc tech 180 chữ | Git workflow | ≥ 60% hiểu |
| Tổng tích lũy | **356 từ / 206 Hán tự** | — |

---

## 📚 Phần 1: Git & Workflow Vocab (35 phút)

### Git:
| Hán tự | Pinyin | Nghĩa | English |
|--------|--------|-------|---------|
| **提交** | tíjiāo | nộp/commit | commit |
| **分支** | fēnzhī | nhánh | branch |
| **合并** | hébìng | gộp/merge | merge |
| **版本** | bǎnběn | phiên bản | version |
| **发布** | fābù | phát hành | release |
| **回滚** | huígǔn | rollback | rollback |

### DevOps & Process:
```
上线     shàngxiàn    đưa lên production   go live
需求     xūqiú        yêu cầu              requirement
任务     rènwu        nhiệm vụ/task        task
进度     jìndù        tiến độ              progress
完成     wánchéng     hoàn thành           complete
```

### Câu thực tế:
```
把代码提交到Git上。
Commit code lên Git.

先创建一个新分支，然后写代码。
Tạo branch mới trước, rồi viết code.

代码合并到主分支以后，就可以发布了。
Merge code vào main branch xong là có thể release.

这个版本有一个bug，需要回滚到上一个版本。
Version này có bug, cần rollback về version trước.

这个任务的进度怎么样？— 已经完成80%了。
Task này progress thế nào? — Đã xong 80%.

新版本准备上线了。
Version mới chuẩn bị go live.
```

> 💡 **Dev tip:** Git flow trong TQ: 需求(requirement) → 分支(branch) → 编码(coding) → 提交(commit) → 合并(merge) → 测试(test) → 部署(deploy) → 上线(go live). Đọc Juejin sẽ thấy flow này!

---

## 📖 Phần 2: 13 Từ Vựng Mới (25 phút)

> Tổng tích lũy sau Day 32: **356 từ**

| # | Hán tự | Pinyin | Nghĩa | Câu ví dụ |
|---|--------|--------|-------|-----------|
| 344 | **提交** | tíjiāo | commit/nộp | 把代码提交了。 |
| 345 | **分支** | fēnzhī | branch/nhánh | 创建一个新分支。 |
| 346 | **合并** | hébìng | merge/gộp | 合并到主分支。 |
| 347 | **版本** | bǎnběn | version | 最新版本是2.0。 |
| 348 | **发布** | fābù | release/phát hành | 新版本已经发布了。 |
| 349 | **需求** | xūqiú | requirement | 客户有新需求。 |
| 350 | **任务** | rènwu | task/nhiệm vụ | 今天的任务很多。 |
| 351 | **进度** | jìndù | progress/tiến độ | 进度怎么样？ |
| 352 | **完成** | wánchéng | complete | 任务已经完成了。 |
| 353 | **上线** | shàngxiàn | go live | 准备上线。 |
| 354 | **创建** | chuàngjiàn | tạo/create | 创建新项目。 |
| 355 | **解决** | jiějué | giải quyết | 问题已经解决了。 |
| 356 | **负责** | fùzé | chịu trách nhiệm | 我负责后端。 |

---

## 📖 Phần 3: Bài Đọc — Git Workflow (180 chữ)

```
我们团队用Git管理代码。每个人负责不同的功能。

每次写新功能的时候，我们先从主分支创建一个
新分支。在自己的分支上写代码，写完以后提交。
然后请同事帮忙看一下代码，这叫代码审查。

代码审查通过以后，就可以把分支合并到主分支了。
合并以后，在测试环境里测试。如果测试没问题，
就可以部署到正式环境，系统上线。

有时候上线以后发现问题。上个星期新版本上线
以后，系统性能变差了。我们马上回滚到上一个
版本，然后花了两天时间找到问题，修改了代码，
重新提交和测试，最后成功上线了。

我们每两个星期发布一个新版本。每个版本都有
一个任务清单，写了要完成什么需求。目前我们的
进度还不错，大部分任务都按时完成了。
```

| # | 问题 | Đáp án |
|---|------|--------|
| 1 | 写新功能时先做什么？ | <details><summary>🔑</summary>从主分支创建新分支</details> |
| 2 | 代码审查是什么？ | <details><summary>🔑</summary>请同事帮忙看代码</details> |
| 3 | 上个星期出了什么问题？ | <details><summary>🔑</summary>新版本上线后系统性能变差</details> |
| 4 | 他们怎么处理的？ | <details><summary>🔑</summary>回滚→找问题→修改→重新测试→上线</details> |
| 5 | 多久发布一个新版本？ | <details><summary>🔑</summary>每两个星期</details> |

**Đọc hiểu: ___/5**

---

## ✏️ Phần 4: 8 Hán Tự Mới (20 phút)

#### 提 tí (đề/nâng) — 12 nét
```
提交 = commit, 提高 = nâng cao
Tập viết: 提 提 提 提 提 提 提 提 提 提
```
#### 交 jiāo (giao) — 6 nét
```
提交 = nộp/commit, 交流 = trao đổi
Tập viết: 交 交 交 交 交 交 交 交 交 交
```
#### 支 zhī (chi/nhánh) — 4 nét
```
分支 = branch, 支持 = hỗ trợ/support
Tập viết: 支 支 支 支 支 支 支 支 支 支
```
#### 并 bìng (gộp) — 6 nét
```
合并 = merge, 并且 = và/hơn nữa
Tập viết: 并 并 并 并 并 并 并 并 并 并
```
#### 版 bǎn (bản) — 8 nét
```
版本 = version, 出版 = xuất bản
Tập viết: 版 版 版 版 版 版 版 版 版 版
```
#### 布 bù (bố/vải) — 5 nét
```
发布 = phát hành/release, 部署 = deploy
Tập viết: 布 布 布 布 布 布 布 布 布 布
```
#### 务 wù (vụ/nhiệm) — 5 nét
```
任务 = task, 服务 = dịch vụ, 服务器 = server
Tập viết: 务 务 务 务 务 务 务 务 务 务
```
#### 完 wán (hoàn) — 7 nét
```
完成 = hoàn thành, 做完 = làm xong
Tập viết: 完 完 完 完 完 完 完 完 完 完
```

---

## 📋 Checklist + 🎧 Nghe 45 phút
- [ ] Git: 提交 分支 合并 版本 发布 回滚
- [ ] Process: 需求 任务 进度 完成 上线 创建 解决 负责
- [ ] Đọc bài + Shadowing + Anki 13 mới
- [ ] Nghe 45 phút (sáng 10p + trưa 15p + tối 10p + shadowing 10p)

---

## 📂 Navigation
| ← Trước | Đang học | Tiếp → |
|---------|----------|--------|
| [03_day3_tech_database.md](./03_day3_tech_database.md) | **04_day4_tech_git.md** | [05_day5_tech_reading.md](./05_day5_tech_reading.md) |
