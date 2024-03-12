# Python Tutorial
## Mục lục

<details>
  <summary>I. Biến và các kiểu dữ liệu cơ bản</summary>


- [Python Tutorial](#python-tutorial)
  - [Mục lục](#mục-lục)
  - [I. Biến và các kiểu dữ liệu cơ bản](#i-biến-và-các-kiểu-dữ-liệu-cơ-bản)
    - [1. In kết quả `print`](#1-in-kết-quả-print)
    - [2. Nhập giá trị từ bàn phím `input`](#2-nhập-giá-trị-từ-bàn-phím-input)
    - [3. Các kiểu dữ liệu trong Python `type, isinstance, eval`](#3-các-kiểu-dữ-liệu-trong-python-type-isinstance-eval)
    - [4. Kiểu dữ liệu số `int, float, complex`](#4-kiểu-dữ-liệu-số-int-float-complex)
    - [5. Kiểu dữ liệu chuỗi ký tự `str`](#5-kiểu-dữ-liệu-chuỗi-ký-tự-str)
  - [II. Cấu trúc điều kiện](#ii-cấu-trúc-điều-kiện)
    - [1. Toán tử logic](#1-toán-tử-logic)
    - [2. Cấu trúc rẽ nhánh if else](#2-cấu-trúc-rẽ-nhánh-if-else)
  - [III. Kiểu dữ liệu danh sách List](#iii-kiểu-dữ-liệu-danh-sách-list)
    - [1. Kiểu dữ liệu List](#1-kiểu-dữ-liệu-list)
    - [2. Phương thức sử dụng List](#2-phương-thức-sử-dụng-list)
  
</details>

<details>
  <summary>II. Cấu trúc điều kiện</summary>

   - [1. Toán tử logic](#1-toán-tử-logic)
   - [2. Cấu trúc rẽ nhánh if else](#2-cấu-trúc-rẽ-nhánh-if-else)
</details>

<details>
  <summary>III. Kiểu dữ liệu danh sách List</summary>

- [1. Kiểu dữ liệu List](#1-kiểu-dữ-liệu-list)
- [2. Phương thức sử dụng List](#2-phương-thức-sử-dụng-list)
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

## II. Cấu trúc điều kiện
[:arrow_up: Mục lục](#mục-lục)

### 1. Toán tử logic
[:arrow_up: Mục lục](#mục-lục)

| Toán tử	 | Mô tả | Ví dụ |
| :--: | :--: | :--: |
| `and` |	Trả về giá trị `True` nếu cả 2 toán hạng đều đúng. |	`a and b` |
| `or` |	Trả về giá trị `True` nếu 1 trong 2 toán hạng là đúng. |	`a or b` |
| `not` |	Trả về giá trị `True` nếu toán hạng là sai. |	`not a` |

### 2. Cấu trúc rẽ nhánh if else
[:arrow_up: Mục lục](#mục-lục)

```python
if điều_kiện1:
    Đoạn mã 1 #Thụt dòng!!!
elif điều_kiện2:
    Đoạn mã 2  #Thụt dòng!!!
else:
    Đoạn mã 3  #Thụt dòng!!!
```

## III. Kiểu dữ liệu danh sách List
[:arrow_up: Mục lục](#mục-lục)

### 1. Kiểu dữ liệu List
[:arrow_up: Mục lục](#mục-lục)

- **Định nghĩa:**

Kiểu dữ liệu danh sách List trong Python là **tập hợp dữ liệu gồm nhiều đối tượng dữ liệu**. Trong đó các đối tượng này có thể có kiểu khác nhau, chúng có thể là các **chuỗi ký tự, số nguyên, boolean, thậm chí là các danh sách khác**.

Chúng ta có thể tạo `list` trong Python bằng một trong hai cách:

- Sử dụng hàm tạo `list()`
- Sử dụng dấu ngoặc vuông (`[]`)

*Ví dụ:*

```python
my_list1 = list((1, 2, 3))
print(my_list1) # [1, 2, 3]
my_list2 = [1, 2, 3]
print(my_list2) # [1, 2, 3]

my_list3 = [300, "Python", 500.5]
print(my_list3) # [300, 'Python', 500.5]

my_list4 = list()
print(my_list4) # []
vi_du = []
print(vi_du) # []
```

Thậm chí, **một đối tượng kiểu List** cũng có thể **là phần tử của một đối tượng kiểu List khác**. Đây được gọi là **danh sách lồng nhau**.

*Ví dụ:*

```python
vi_du1 = []
vi_du2 = [100, 100.5, 200]
vi_du3 = [300, "Python", [500.5, 200, "Javascript"]]
```

- **Truy cập các phần tử của tập hợp List trong Python thông qua chỉ số âm**

```python
vi_du2 = ["Python", [100, 200, 300, 400]]
print(vi_du2[-1]) # [100, 200, 300, 400]
print(vi_du2[-2]) # Python
```

Các phần tử của List cũng có thể được truy cập theo chỉ số từ phải sang trái theo chỉ số âm. Chỉ số âm được đánh từ -1 cho đến -len của List. Nó thể hiện chỉ số theo chiều ngược của danh sách. Chỉ số -1 tham chiếu đến phần tử cuối cùng, -2 tham chiếu đến phần tử cuối cùng thứ hai,...

### 2. Phương thức sử dụng List
[:arrow_up: Mục lục](#mục-lục)

- Số phần tử hay độ dài của danh sách

```python
my_list = [100, 200, "Python"]
print(len(my_list)) # 3
```

**Đối với danh sách lồng nhau**, phần tử danh sách con bên trong cũng chỉ được coi là một phần tử của danh sách bên ngoài. Vì vậy độ dài của danh sách `vi_du3` dưới đây cũng có kết quả là `3`:

```python
vi_du3 = [300, "Python", [500.5, 200, "Javascript"]]
print(len(vi_du3)) # 3
```

