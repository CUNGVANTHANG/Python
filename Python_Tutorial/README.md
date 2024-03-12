# Python Tutorial
## Mục lục

<details>
  <summary>I. Biến và các kiểu dữ liệu cơ bản</summary>

  - [1. In kết quả](#1-in-kết-quả-print)
  - [2. Nhập giá trị từ bàn phím](#2-nhập-giá-trị-từ-bàn-phím-input)
</details>

## I. Biến và các kiểu dữ liệu cơ bản
### 1. In kết quả `print`
[:arrow_up: Mục lục](#mục-lục)

`print("Kết quả")` in `Kết quả` xong đó **xuống dòng**

`print("Kết quả", end="")` in `Kết quả` xong đó **không xuống dòng**

`print(12, 33)` in nhiều biến hoặc giá trị cách nhau bằng dấu phẩy `,`

`print("Hello " + "World!")` in nối chuỗi (Chú ý toán tử `+` không thể sử dụng với chuỗi + số)

`print("Giá trị của x là:", x)` in chuỗi với số (format)

`print(f"Giá trị của x là: {x}")` in chuỗi với số dạng chuỗi (format string)

`print(f"Giá trị của x là: {x:.2f}")` in số dạng chuỗi (format string) làm tròn x đến 2 chữ số thập phân

### 2. Nhập giá trị từ bàn phím `input`
[:arrow_up: Mục lục](#mục-lục)

**a. Cú pháp nhập chuỗi ký tự từ bàn phím:** `prompt` là chuỗi ký tự mà chúng ta muốn hiển thị lên trên màn hình.

```python
input([prompt])
```

_Ví dụ:_

```python
a = input('Nhập một số nguyên: ')
print(a)
```

_Kết quả:_

```
Nhập một số nguyên: 200
200
```

**b. Cú pháp nhập một số từ bàn phím:** `prompt` là chuỗi ký tự mà chúng ta muốn hiển thị lên trên màn hình.

```python
int(input([prompt]))
```

_Ví dụ:_

```python
a = int(input('Nhập một số nguyên: '))
print(a + 5)
```

_Kết quả:_

```
Nhập một số nguyên: 50
55
```

### 3. Các kiểu dữ liệu trong Python `type, isinstance, eval`
[:arrow_up: Mục lục](#mục-lục)

**Các kiểu dữ liệu trong Python:**

`int`, `float`, `bool`, `str`, `list`, `set`, `dict`, `tuple`

Phương thức `type([variable hoặc object])` để biết biến hoặc một đối tượng thuộc lớp nào

Phương thức `isinstance([variable hoặc object], [int, float, complex...])` để kiểm tra xem một biến hoặc đối tượng có thuộc một lớp cụ thể nào hay không.

_Ví dụ:_

```python
a = 100
print(type(a))
print(type(100.30))
b = 10 + 24j
print(b + 20)
print(isinstance(b, complex))
```

_Kết quả:_

```
<class 'int'>
<class 'float'>
(30+24j)
True
```

**Ép kiểu dữ liệu trong Python:**

**Cách 1:**

> <kiểu dữ liệu>(biểu thức)

_Ví dụ:_

```python
a = 100
b = float("200.5")
print(type(a))
print(type(b))
print(a+b)
```

_Kết quả:_

```
<class 'int'>
<class 'float'>
300.5
```

**Cách 2:** Sử dụng hàm `eval()` để ép kiểu số nguyên `int`

_Ví dụ:_

```python
print(eval('100 + 200'))
```

_Kết quả:_

```
300
```

### 4. Kiểu dữ liệu số `int, float, complex` 
[:arrow_up: Mục lục](#mục-lục)

Trong Python có 3 lớp `int`, `float` và `complex` (`a + bj`)

| Toán tử	 | Mô tả | Cú pháp | Ví dụ |
| :--: | :--: | :--: | :--: |
| `+` |	Thực hiện phép cộng cho các toán hạng. |	a + b + 100	| 100+200=300 |
| `-` |	Thực hiện phép trừ cho các toán hạng. |	a – b - 200	| 200-100=100 |
| `*` |	Thực hiện phép nhân 2 toán hạng.	| a * b	 | 16*5=80 |
| `/` |	Thực hiện phép chia cho 2 toán hạng. | a / b |	8/5=1.6 |
| `%` |	Phép chia lấy phần dư. | a % b (phần dư của phép a chia b)	| 8%5=3 |
| `//` |	Phép chia làm tròn dưới (chia nguyên) |	a // b	| 8//5=1 |
| `**` |	Số mũ.	| a**b (a mũ b)	| 2**3=8 |

_Chú ý:_ Không thể sử dụng toán tử `+` để nối chuỗi với số (Bởi Python không cho phép cộng một chuỗi ký tự và một số)

Ví dụ:

```python
print("Kết quả là" + 5)
```

Kết quả:

```
TypeError: can only concatenate str (not "int") to str
```

Khắc phục: Sử dụng dấu `,` thay bằng toán tử `+`. Chú ý hàm `print()` sẽ tự động thêm vào một khoảng trắng với mỗi một tham số mới sau dấu phẩy `,`)

```python
print("Kết quả =",5)
```

Kết quả:

```
Kết quả = 5
```

_Trường hợp có thể sẽ gặp:_ 

```python
print(0.1+0.2) # 0.30000000000000004
tolerance = 0.00001
x = 0.1 + 0.2
print(abs(x - 0.3) < tolerance)
```

Hàm `abs()` trả về giá trị tuyệt đối. Nếu giá trị tuyệt đối của hiệu số giữa hai số nhỏ hơn một mức sai số `tolerance` quy định chấp nhận được, tức là chúng đủ gần bằng nhau để được coi là bằng nhau.

### 5. Kiểu dữ liệu chuỗi ký tự `str`
[:arrow_up: Mục lục](#mục-lục)

| Toán tử | Tác dụng |
| :--: | :--: |
| `+` | nối chuỗi |
| `*` | lặp chuỗi |

_Ví dụ:_

```python
print("Hello" + " world!")
print(a * 4)
```

_Kết quả:_

```
Hello World
aaaa
```

_So sánh chuỗi:_

```python
print("abc" == "abc") # True
```

### 6. Toán tử logic
[:arrow_up: Mục lục](#mục-lục)

| Toán tử	 | Mô tả | Ví dụ |
| :--: | :--: | :--: |
| `and` |	Trả về giá trị `True` nếu cả 2 toán hạng đều đúng. |	`a and b` |
| `or` |	Trả về giá trị `True` nếu 1 trong 2 toán hạng là đúng. |	`a or b` |
| `not` |	Trả về giá trị `True` nếu toán hạng là sai. |	`not a` |
