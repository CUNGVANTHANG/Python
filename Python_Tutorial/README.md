# Python Tutorial
## Mục lục

<details>
  <summary>I. Biến và các kiểu dữ liệu cơ bản</summary>

- [1. In kết quả `print`](#1-in-kết-quả-print)
- [2. Nhập giá trị từ bàn phím `input`](#2-nhập-giá-trị-từ-bàn-phím-input)
- [3. Các kiểu dữ liệu trong Python `type, isinstance, eval`](#3-các-kiểu-dữ-liệu-trong-python-type-isinstance-eval)
- [4. Kiểu dữ liệu số `int, float, complex`](#4-kiểu-dữ-liệu-số-int-float-complex)
- [5. Kiểu dữ liệu chuỗi ký tự `str`](#5-kiểu-dữ-liệu-chuỗi-ký-tự-str)
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

**_Chú ý:_** Không sử dụng được toán tử `+` để in chuỗi cùng với số

```python
print("Số " + 3) # TypeError: can only concatenate str (not "int") to str
```

Muốn in chuỗi cùng với số thì phải dùng `,`

```python
# Chú ý là sau dấu phẩy , sẽ tự động có 1 khoảng trắng
print("Số", 3) # Số 3
```

hoặc ta có thể convert sang chuỗi để sử dụng toán tử `+`

```python
print("Số " + str(3)) # Số 3
```

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

- **Các kiểu dữ liệu trong Python:**

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

- **Ép kiểu dữ liệu trong Python:**

**Cách 1:**

> <kiểu dữ liệu>(biểu thức)

_Ví dụ 1:_

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

_Ví dụ 2:_

```python
number = 3
print("Số " + str(number))
```

_Kết quả:_

```
Số 3
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

**_Chú ý:_** Không sử dụng được toán tử `+` để in chuỗi cùng với số

```python
print("Số " + 3) # TypeError: can only concatenate str (not "int") to str
```

Muốn in chuỗi cùng với số thì phải dùng `,`

```python
# Chú ý là sau dấu phẩy , sẽ tự động có 1 khoảng trắng
print("Số", 3) # Số 3
```

hoặc ta có thể convert sang chuỗi để sử dụng toán tử `+`

```python
print("Số " + str(3)) # Số 3
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

<img src="https://github.com/CUNGVANTHANG/Python/assets/96326479/da0f22bd-707d-456d-a350-44271e75ea3f" width="500px">

### 2. Phương thức sử dụng List
[:arrow_up: Mục lục](#mục-lục)

| STT | Mô tả | Phương thức |
| :--: | :--: | :--: |
| 1 | [Số phần tử hay độ dài của danh sách](#a-số-phần-tử-hay-độ-dài-của-danh-sách) | `len()` |
| 2 | [Lấy ra một danh sách con trong List](#b-lấy-ra-một-danh-sách-con-trong-list) | `listname[start_index : end_index : step]` |
| 3 | [Thêm phần tử vào trong danh sách](#c-thêm-phần-tử-vào-trong-danh-sách) | `append()`, `insert()`, `extend()` | 
| 4 | [Xóa các phần tử khỏi danh sách](#d-xóa-các-phần-tử-khỏi-danh-sách) | `remove(item)`, `pop(index)`, `clear()`, `del list_name` |
| 5 | [Kiểm tra phần tử có tồn tại](#e-kiểm-tra-phần-tử-có-tồn-tại) | `in`, `not in` |
| 6 | [Tìm một phần tử trong danh sách](#f-tìm-một-phần-tử-trong-danh-sách) | `index()` |
| 7 | [Sắp xếp danh sách](#g-sắp-xếp-danh-sách) | `sort()` |
| 8 | [Đảo ngược danh sách](#h-đảo-ngược-danh-sách) | `reverse()` |
| 9 | [Tìm giá trị lớn nhất và nhỏ nhất trong danh sách](#i-tìm-giá-trị-lớn-nhất-và-nhỏ-nhất-trong-danh-sách) | `max()`, `min()` |
| 10 | [Tính tổng các phần tử có trong danh sách](#j-tính-tổng-các-phần-tử-có-trong-danh-sách) | `sum()` |
| 11 | [Đếm số lần phần tử xuất hiện](#k-đếm-số-lần-phần-tử-xuất-hiện) | `count()` | 
| 12 | [Nối các danh sách](#l-nối-các-danh-sách) | `+`, `extend()` |
| 13 | [Sao chép danh sách](#m-sao-chép-danh-sách) | `=`, `copy()` |
| 14 | [Kiểm tra tất cả giá trị trong danh sách](#n-kiểm-tra-tất-cả-giá-trị-trong-danh-sách) | `all()` |
| 15 | [Kiểm tra giá trị trong danh sách](#o-kiểm-tra-giá-trị-trong-danh-sách) |  `any()` |

#### a. Số phần tử hay độ dài của danh sách

```python
my_list = [100, 200, "Python"]
print(len(my_list)) # 3
```

**Đối với danh sách lồng nhau**, phần tử danh sách con bên trong cũng chỉ được coi là một phần tử của danh sách bên ngoài. Vì vậy độ dài của danh sách `vi_du3` dưới đây cũng có kết quả là `3`:

```python
vi_du3 = [300, "Python", [500.5, 200, "Javascript"]]
print(len(vi_du3)) # 3
```

#### b. Lấy ra một danh sách con trong List

```python
listname[start_index : end_index : step]
```

- `start_index` biểu diễn giá trị của chỉ số bắt đầu của phép cắt 
- `end_index` đại diện cho chỉ số cuối cùng của phép cắt (Các phần tử được lấy sẽ được tính từ `start_index` cho đến phần tử `end_index - 1`, không tính phần tử tại vị tri có chỉ số là `end_index`.
- `step` cho phép chúng ta nhảy cách qua một loạt các phần tử thay vì đi từ đầu đến cuối trong khoảng `start_index:end_index`. Chỉ số này có thể được bỏ qua khi sử dụng. Khi đó, Python sẽ mặc định bước nhảy là `1`.

_Ví dụ 1:_ Không sử dụng `step`

```python
vi_du2 = [50, 100, 200, 300, 400]
print(vi_du2[0:2])
print(vi_du2[1:3])
```

_Kết quả:_

```
[50, 100]
[100, 200]
```

_Ví dụ 2:_ Sử dụng `step`

```python
vidu_list=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(vidu_list[2:6:2])
print(vidu_list[0:8:3])
```

_Kết quả:_

```
[2, 4]
[0, 3, 6]
```

_Ví dụ 3:_

```python
vidu_list=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(vidu_list[:5:2]) # Bỏ trống chỉ số đầu, bước nhảy dương
print(vidu_list[:5:-2]) # Bỏ trống chỉ số đầu, bước nhảy âm
print(vidu_list[5::2]) # Bỏ trống chỉ số cuối, bước nhảy dương
print(vidu_list[5::-2]) # Bỏ trống chỉ số cuối, bước nhảy âm
print(vidu_list[::2]) # Bỏ trống cả chỉ số đầu và cuối, bước nhảy dương
print(vidu_list[::-2]) # Bỏ trống cả chỉ số đầu và cuối, bước nhảy âm
print(vidu_list[::]) # Bỏ trống tất cả các chỉ số và bước nhảy
print(vidu_list[:5]) # Bỏ trống chỉ số đầu và bước nhảy
print(vidu_list[5:]) # Bỏ trống chỉ số cuối và bước nhảy
```

_Kết quả:_

```
[0, 2, 4]
[9, 7]
[5, 7, 9]
[5, 3, 1]
[0, 2, 4, 6, 8]
[9, 7, 5, 3, 1]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 1, 2, 3, 4]
[5, 6, 7, 8, 9]
```

#### c. Thêm phần tử vào trong danh sách

| STT | Phương thức | Mô tả |
| :--: | :--: | :--: |
| 1 | `append()` | Thêm 1 phần tử vào cuối danh sách | 
| 2 | `insert()` | Thêm 1 phần tử vào vị trí bất kỳ trong danh sách | 
| 3 | `extend()` | Thêm danh sách các phần tử vào cuối danh sách |

_Ví dụ 1:_ Dùng `append()` để thêm 1 phần tử vào cuối danh sách

```python
my_list = list([1, 2, 'abc', 12.13])
my_list.append('Python')
print(my_list) # [1, 2, 'abc', 12.13, 'Python']
my_list.append([11, 12, 13])
print(my_list) # [1, 2, 'abc', 12.13, 'Python', [11, 12, 13]]
```

_Ví dụ 2:_ Dùng `insert()` để thêm 1 phần tử vào vị trí bất kỳ trong danh sách

Syntax:

```python
object.insert(position,value)
```

Nó sẽ chèn giá trị `value` vào đối tượng `object` tại chỉ số được chỉ định là `position`.

```python
my_list = [1, 2, 'abc', 1.2]
my_list.insert(3, 5)
print(my_list) # [1, 2, 'abc', 5, 1.2]
my_list.insert(4, [11, 12, 13])
print(my_list) # [1, 2, 'abc', 5, [11, 12, 13], 1.2]
```

_Ví dụ 3:_ Dùng `extend()` để thêm danh sách các phần tử vào cuối danh sách (khác với `append()`)

```python
my_list = list([1, 2, 'abc', 4.5])
my_list.extend([11, 12, 13])
print(my_list) # [1, 2, 'abc', 4.5, 11, 12, 13]
```

#### d. Xóa các phần tử khỏi danh sách

| STT | Phương thức | Mô tả |
| :--: | :--: | :--: |
| 1 | `remove(item)` | Loại bỏ 1 phần tử có giá trị nào đó tại vị trí lần đầu tiên nó xuất hiện. |
| 2 | `pop(index)` |	Loại bỏ và trả về giá trị của phần tử tại vị trí index trong danh sách. |
| 3 | `clear()` |	Loại bỏ toàn bộ phần tử khỏi danh sách. Đầu ra sẽ là danh sách rỗng. |
| 4 | `del list_name` |	Xóa nhiều phần tử trong danh sách. |

_Ví dụ 1:_ Dùng `pop()` xóa phần tử tại một vị trí được chỉ định trong danh sách

```python
my_list = list([2, 4, 6, 8, 10, 12])
my_list.pop(2)
print(my_list) # [2, 4, 8, 10, 12]
my_list.pop()
print(my_list) # [2, 4, 8, 10]
```

_Ví dụ 2:_ Dùng `del list_name` xóa nhiều phần tử trong danh sách

```python
my_list = list([2, 4, 6, 8, 10, 12])
del my_list[2:5]
print(my_list) # [2, 4, 12]
my_list = list([1, 2, 3, 4, 5, 6])
del my_list[3:]
print(my_list) # [1, 2, 3]
```

hoặc dùng để xóa toàn bộ danh sách

```python
my_list = list([1, 2, 3, 4, 5, 6])
del my_list
print(my_list) # NameError: name 'my_list' is not defined
```

_Ví dụ 3:_ Dùng `clear()` xóa toàn bộ danh sách

```python
my_list = list([1, 2, 3, 4, 5, 6])
my_list.clear()
print(my_list) # []
```

_Ví dụ 4:_ Dùng `remove` để xóa 1 lần xuất hiện đầu tiên của phần tử ra khỏi danh sách

```python
my_list = list([2, 4, 6, 8, 6, 10, 12])
my_list.remove(6)
my_list.remove(8)
print(my_list) # [2, 4, 6, 10, 12]
```

#### e. Kiểm tra phần tử có tồn tại

#### f. Tìm một phần tử trong danh sách

#### g. Sắp xếp danh sách

#### h. Đảo ngược danh sách

#### i. Tìm giá trị lớn nhất và nhỏ nhất trong danh sách

#### j. Tính tổng các phần tử có trong danh sách

#### k. Đếm số lần phần tử xuất hiện

#### l. Nối các danh sách

#### m. Sao chép danh sách

#### n. Kiểm tra tất cả giá trị trong danh sách

#### o. Kiểm tra giá trị trong danh sách
