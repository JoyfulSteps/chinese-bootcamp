# 🏋️ Exercise 46 — Code Review Drill
## Day 46 (Tuần 7, Ngày 4)

---

## Bài Tập 1: CR Vocab (8 phút)
| # | Hán tự | Nghĩa | Đáp án |
|---|--------|-------|--------|
| 1 | 逻辑 | | <details><summary>🔑</summary>logic</details> |
| 2 | 变量 | | <details><summary>🔑</summary>biến/variable</details> |
| 3 | 函数 | | <details><summary>🔑</summary>function/hàm</details> |
| 4 | 判断 | | <details><summary>🔑</summary>check/phán đoán</details> |
| 5 | 导致 | | <details><summary>🔑</summary>dẫn đến/cause</details> |
| 6 | 日志 | | <details><summary>🔑</summary>log</details> |
| 7 | 排查 | | <details><summary>🔑</summary>troubleshoot</details> |
| 8 | 潜在 | | <details><summary>🔑</summary>tiềm ẩn/potential</details> |
| 9 | 缺少 | | <details><summary>🔑</summary>thiếu/missing</details> |
| 10 | 重复 | | <details><summary>🔑</summary>lặp lại/duplicate</details> |

**Điểm: ___/10**

## Bài Tập 2: Viết CR Comments (15 phút)
```python
# Code cần review:
def calculate_price(items):
    total = 0
    for item in items:
        total = total + item.price * item.quantity
    return total
```
Viết 3 CR comments bằng TQ:
```
1. _________________________________________________
2. _________________________________________________
3. _________________________________________________
```
<details><summary>🔑 Gợi ý</summary>
1. 缺少空值判断。如果items为空，应该返回0或者报错。
2. 没有处理负数的情况。如果price或quantity是负数怎么办？
3. 建议加上日志，记录计算结果，方便排查问题。
</details>

## Bài Tập 3: Dịch CR (12 phút)
| # | Câu | Đáp án |
|---|-----|--------|
| 1 | Logic rất rõ ràng, có thể merge. | <details><summary>🔑</summary>逻辑很清楚，可以合并。</details> |
| 2 | Thiếu error handling, có thể dẫn đến crash. | <details><summary>🔑</summary>缺少错误处理，可能导致崩溃。</details> |
| 3 | Code lặp lại, khuyên tách thành 1 function chung. | <details><summary>🔑</summary>代码重复，建议提取一个公共函数。</details> |
| 4 | Tên biến không rõ, đổi thành cái cụ thể hơn. | <details><summary>🔑</summary>变量名不清楚，建议改成更具体的。</details> |

**Điểm: ___/4**

---
## 📊 Tổng Kết: ___/14 + CR practice
