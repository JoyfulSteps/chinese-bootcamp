# Day 39: API Docs Tiếng Trung + 对...来说
## Tuần 6 — Ngày 4 (Day 39) | Thứ Năm 17/4/2026

---

## 🎯 Mục Tiêu Ngày 39
| Mục Tiêu | Chi Tiết | Đo lường |
|----------|----------|----------|
| Ngữ pháp: 对...来说 | Đối với...mà nói | 6 câu |
| Đọc API docs TQ | Swagger/docs mẫu | ≥ 50% hiểu |
| Tổng tích lũy | **434 từ / 254 Hán tự / 29 NP** | — |

---

## 📐 Phần 1: Ngữ Pháp — 对...来说 (15 phút)

### Pattern: 对 A 来说 = Đối với A mà nói

```
对我来说，学中文不难。
Đối với tôi, học TQ không khó.

对新人来说，Vue比React简单。
Đối với newbie, Vue đơn giản hơn React.

对程序员来说，英文很重要。
Đối với dev, tiếng Anh rất quan trọng.
```

> 💡 **Dev tip:** `对...来说` = `context.setScope(user)` — set context/scope cho nhận xét.

---

## 📖 Phần 2: Đọc API Docs TQ (30 phút)

### API docs mẫu (230 chữ):
```
# 用户登录接口

## 接口地址
POST /api/v1/user/login

## 请求参数
| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| username | String | 是 | 用户名 |
| password | String | 是 | 密码 |

## 返回结果
成功时返回：
{ "code": 200, "message": "登录成功", "data": { "token": "..." } }

失败时返回：
{ "code": 401, "message": "用户名或密码错误" }

## 注意事项
- 密码需要加密传输
- token有效期为24小时
- 连续五次登录失败，账号会被锁定
- 对于安全要求高的系统来说，建议使用双重验证

## 示例代码
// 发送登录请求
fetch('/api/v1/user/login', {
  method: 'POST',
  body: JSON.stringify({ username, password })
})

## 常见错误
| 错误码 | 说明 | 解决方案 |
|--------|------|---------|
| 401 | 用户名或密码错误 | 检查输入 |
| 403 | 账号被锁定 | 联系管理员 |
| 500 | 服务器异常 | 稍后重试 |
```

### Từ khóa API docs:
```
类型 lèixíng = loại/type      必填 bìtián = bắt buộc
说明 shuōmíng = giải thích     成功 chénggōng = thành công
失败 shībài = thất bại         注意事项 = điều lưu ý
示例 shìlì = ví dụ/example     常见 chángjiàn = thường gặp
错误码 = error code             解决方案 = solution
```

| # | 问题 | Đáp án |
|---|------|--------|
| 1 | 登录需要什么参数？ | <details><summary>🔑</summary>username和password</details> |
| 2 | 登录成功返回什么？ | <details><summary>🔑</summary>code:200, message和token</details> |
| 3 | 连续几次失败会被锁？ | <details><summary>🔑</summary>五次</details> |
| 4 | 出现500错误怎么办？ | <details><summary>🔑</summary>稍后重试</details> |

---

## 📖 Phần 3: 13 Từ Vựng Mới (25 phút)

> Tổng tích lũy sau Day 39: **434 từ**

| # | Hán tự | Pinyin | Nghĩa | Câu ví dụ |
|---|--------|--------|-------|-----------|
| 422 | **对...来说** | duì...lái shuō | đối với...mà nói | 对我来说不难。 |
| 423 | **类型** | lèixíng | loại/type | 参数类型是String。 |
| 424 | **成功** | chénggōng | thành công | 登录成功。 |
| 425 | **失败** | shībài | thất bại | 请求失败。 |
| 426 | **注意** | zhùyì | chú ý | 注意安全。 |
| 427 | **示例** | shìlì | ví dụ/example | 看示例代码。 |
| 428 | **常见** | chángjiàn | thường gặp | 常见错误。 |
| 429 | **解决方案** | jiějué fāng'àn | giải pháp | 找到解决方案。 |
| 430 | **说明** | shuōmíng | giải thích/docs | 参数说明。 |
| 431 | **有效** | yǒuxiào | có hiệu lực | token有效期24小时。 |
| 432 | **锁定** | suǒdìng | khóa | 账号被锁定。 |
| 433 | **传输** | chuánshū | truyền tải | 加密传输。 |
| 434 | **安全** | ānquán | an toàn/bảo mật | 安全很重要。 |

---

## ✏️ Phần 4: 8 Hán Tự Mới (20 phút)

#### 类 lèi (loại) — 9 nét
```
类型 = kiểu/type, 分类 = phân loại
Tập viết: 类 类 类 类 类 类 类 类 类 类
```
#### 型 xíng (hình) — 9 nét
```
类型 = type, 模型 = model
Tập viết: 型 型 型 型 型 型 型 型 型 型
```
#### 败 bài (bại) — 8 nét
```
失败 = thất bại
Tập viết: 败 败 败 败 败 败 败 败 败 败
```
#### 注 zhù (chú) — 8 nét
```
注意 = chú ý, 注册 = đăng ký
Tập viết: 注 注 注 注 注 注 注 注 注 注
```
#### 全 quán (toàn) — 6 nét
```
安全 = an toàn, 全部 = toàn bộ, 全栈 = fullstack
Tập viết: 全 全 全 全 全 全 全 全 全 全
```
#### 锁 suǒ (khóa) — 12 nét
```
锁定 = khóa, 死锁 = deadlock!
Tập viết: 锁 锁 锁 锁 锁 锁 锁 锁 锁 锁
```
#### 效 xiào (hiệu) — 10 nét
```
有效 = có hiệu lực, 效率 = hiệu suất
Tập viết: 效 效 效 效 效 效 效 效 效 效
```
#### 输 shū (thâu/truyền) — 13 nét
```
传输 = truyền tải, 输入 = nhập, 输出 = xuất
Tập viết: 输 输 输 输 输 输 输 输 输 输
```

---

## 📋 Checklist
- [ ] 对A来说 = đối với A
- [ ] Đọc hiểu API docs TQ: 类型 必填 说明 成功 失败 注意 示例
- [ ] Anki 13 mới + 🎧 Nghe 45 phút

---
## 📂 Navigation
| ← Trước | Đang học | Tiếp → |
|---------|----------|--------|
| [03_day3_workplace.md](./03_day3_workplace.md) | **04_day4_api_docs.md** | [05_day5_opinions.md](./05_day5_opinions.md) |
