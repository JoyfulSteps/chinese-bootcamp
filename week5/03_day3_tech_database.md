# Day 31: Tech — Database & Server Nâng Cao
## Tuần 5 — Ngày 3 (Day 31) | Thứ Tư 9/4/2026

---

## 🎯 Mục Tiêu Ngày 31
| Mục Tiêu | Chi Tiết | Đo lường |
|----------|----------|----------|
| Tech vocab: DB & Server | Query, connect, backup, update | 13 từ mới |
| Đọc tech 180 chữ | Database architecture | ≥ 60% hiểu |
| Tổng tích lũy | **343 từ / 198 Hán tự** | — |

---

## 🔄 Ôn Tập Day 29-30 (10 phút)
```
⚡ Tech vocab speed check (nói to):
  [ ] 系统 应用 编程 运行 安装 下载 功能 错误
  [ ] 前端 后端 全栈 浏览器 页面 用户 登录 密码
  [ ] 请求 返回 参数 链接 显示
```

---

## 📚 Phần 1: Database & Server Vocab (35 phút)

### Database:
| Hán tự | Pinyin | Nghĩa | English |
|--------|--------|-------|---------|
| **查询** | cháxún | truy vấn | query |
| **连接** | liánjiē | kết nối | connect |
| **备份** | bèifèn | sao lưu | backup |
| **更新** | gēngxīn | cập nhật | update |
| **删除** | shānchú | xóa | delete |
| **添加** | tiānjiā | thêm | add/insert |
| **保存** | bǎocún | lưu | save |
| **修改** | xiūgǎi | sửa đổi | modify |

### Server & DevOps:
```
配置     pèizhì      cấu hình     configuration
环境     huánjìng     môi trường   environment
性能     xìngnéng     hiệu suất   performance
正常     zhèngcháng   bình thường  normal
异常     yìcháng      bất thường   abnormal/exception
```

### Câu thực tế:
```
数据库查询太慢了，需要优化。
Database query quá chậm, cần tối ưu.

请先备份数据，然后再删除。
Backup data trước, rồi hãy xóa.

把配置文件更新一下。
Update file config đi.

服务器连接异常，请检查环境配置。
Kết nối server bất thường, check config env.

这个操作会修改数据库里的数据。
Thao tác này sẽ modify data trong DB.
```

> 💡 **Dev tip:** CRUD trong TQ: **添加**(Create) **查询**(Read) **修改/更新**(Update) **删除**(Delete). Nhớ 4 từ này = đọc hiểu API docs TQ!

---

## 📖 Phần 2: 13 Từ Vựng Mới (25 phút)

> Tổng tích lũy sau Day 31: **343 từ**

| # | Hán tự | Pinyin | Nghĩa | Câu ví dụ |
|---|--------|--------|-------|-----------|
| 331 | **查询** | cháxún | truy vấn/query | 查询数据库。 |
| 332 | **连接** | liánjiē | kết nối | 数据库连接失败。 |
| 333 | **备份** | bèifèn | backup | 请先备份数据。 |
| 334 | **更新** | gēngxīn | update | 更新系统版本。 |
| 335 | **删除** | shānchú | xóa/delete | 删除这个文件。 |
| 336 | **添加** | tiānjiā | thêm/add | 添加一个新功能。 |
| 337 | **保存** | bǎocún | lưu/save | 保存文件。 |
| 338 | **修改** | xiūgǎi | sửa đổi/modify | 修改了代码。 |
| 339 | **配置** | pèizhì | cấu hình/config | 检查配置文件。 |
| 340 | **环境** | huánjìng | môi trường/env | 开发环境和生产环境。 |
| 341 | **性能** | xìngnéng | hiệu suất/perf | 性能需要优化。 |
| 342 | **正常** | zhèngcháng | bình thường | 系统运行正常。 |
| 343 | **异常** | yìcháng | bất thường/exception | 服务器连接异常。 |

---

## 📖 Phần 3: Bài Đọc Tech (15 phút)

### Bài Đọc 3 — 数据库管理 (180 chữ)

```
数据库是每个应用最重要的部分之一。如果数据库
出了问题，整个系统都不能正常运行。

我们公司用MySQL数据库。每天晚上十二点，
系统会自动备份数据。如果数据被误删了，
可以从备份里恢复。

上个月，一个同事不小心删除了一个表的数据。
因为我们有备份，所以很快就恢复了。但是从那
以后，经理决定修改权限配置。现在除了管理员
以外，其他人都不能删除正式环境的数据。

做数据库操作的时候要特别小心。添加和修改
数据之前，最好先在测试环境里试一下。
查询的时候也要注意性能，如果查询太慢，
需要添加索引或者优化SQL。

我们每个星期都会检查一次数据库的连接和
性能，确保系统正常运行。
```

| # | 问题 | Đáp án |
|---|------|--------|
| 1 | 什么时候自动备份？ | <details><summary>🔑</summary>每天晚上十二点</details> |
| 2 | 上个月发生了什么？ | <details><summary>🔑</summary>同事不小心删除了数据</details> |
| 3 | 经理做了什么改变？ | <details><summary>🔑</summary>修改了权限配置，只有管理员能删除正式环境数据</details> |
| 4 | 修改数据之前应该怎么做？ | <details><summary>🔑</summary>先在测试环境里试一下</details> |
| 5 | 查询太慢怎么办？ | <details><summary>🔑</summary>添加索引或者优化SQL</details> |

**Đọc hiểu: ___/5**

---

## 🗣️ Phần 4: Hội Thoại — Database Issue (15 phút)

```
A: 服务器连接异常了！你看一下是什么问题。
B: 好的。让我查一下...是数据库连接的问题。
   配置文件里的密码被修改了。
A: 谁修改的？
B: 不知道。我先把密码改回来，然后检查连接。
A: 好。数据有没有问题？
B: 数据没有问题，备份也是正常的。
   我已经把配置更新了，系统恢复正常了。
A: 太好了。以后要注意，修改配置之前一定要备份。
```

> 🎤 **Shadowing** 5 lần。

---

## ✏️ Phần 5: 8 Hán Tự Mới (20 phút)

#### 查 chá (tra/kiểm) — 9 nét
```
查询 = truy vấn, 检查 = kiểm tra
Tập viết: 查 查 查 查 查 查 查 查 查 查
```
#### 询 xún (hỏi) — 8 nét
```
查询 = truy vấn/query
Tập viết: 询 询 询 询 询 询 询 询 询 询
```
#### 删 shān (xóa) — 7 nét
```
删除 = xóa/delete
Tập viết: 删 删 删 删 删 删 删 删 删 删
```
#### 除 chú (trừ/bỏ) — 9 nét
```
删除 = xóa, 除了 = ngoài ra
Tập viết: 除 除 除 除 除 除 除 除 除 除
```
#### 存 cún (lưu/tồn) — 6 nét
```
保存 = lưu/save, 存储 = lưu trữ
Tập viết: 存 存 存 存 存 存 存 存 存 存
```
#### 改 gǎi (sửa) — 7 nét
```
修改 = sửa đổi, 改变 = thay đổi
Tập viết: 改 改 改 改 改 改 改 改 改 改
```
#### 境 jìng (cảnh) — 14 nét
```
环境 = môi trường/environment
Tập viết: 境 境 境 境 境 境 境 境 境 境
```
#### 配 pèi (phối/cấu) — 10 nét
```
配置 = cấu hình/config
Tập viết: 配 配 配 配 配 配 配 配 配 配
```

---

## 📋 Checklist + 🎧 Nghe 45 phút
- [ ] CRUD: 添加 查询 修改/更新 删除
- [ ] 备份 保存 连接 配置 环境 性能 正常 异常
- [ ] Đọc bài + Shadowing + Anki 13 mới
- [ ] Nghe: sáng 10p + trưa 15p + tối 10p + shadowing 10p

---

## 📂 Navigation
| ← Trước | Đang học | Tiếp → |
|---------|----------|--------|
| [02_day2_tech_web.md](./02_day2_tech_web.md) | **03_day3_tech_database.md** | [04_day4_tech_git.md](./04_day4_tech_git.md) |
