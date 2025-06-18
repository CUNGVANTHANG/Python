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

<details>
  <summary>IV. Các thao tác trên chuỗi ký tự</summary>

- [1. Một số thao tác trên chuỗi ký tự trên Python](#1-một-số-thao-tác-trên-chuỗi-ký-tự-trên-python)
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
[:arrow_up: 2. Phương thức sử dụng List](#2-phương-thức-sử-dụng-list)

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
[:arrow_up: 2. Phương thức sử dụng List](#2-phương-thức-sử-dụng-list)

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
[:arrow_up: 2. Phương thức sử dụng List](#2-phương-thức-sử-dụng-list)

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
[:arrow_up: 2. Phương thức sử dụng List](#2-phương-thức-sử-dụng-list)

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
[:arrow_up: 2. Phương thức sử dụng List](#2-phương-thức-sử-dụng-list)

_Ví dụ 1:_ Kiểm tra phần tử thành viên với toán tử in và not in

```python
vi_du1 = [100, 200, 300, 400, 500, 600, 700, 800, 900]
print(100 in vi_du1) # True
print(1000 in vi_du1) # False
print(800 not in vi_du1) # False
```

Trong đó:

- Toán tử `in` trả về `True` nếu phần tử thuộc danh sách và `False` nếu phần tử không thuộc danh sách.
- Toàn từ `not in` ngược lại sẽ trả về `True` nếu phần tử không thuộc danh sách và `False` nếu phần tử thuộc danh sách.

#### f. Tìm một phần tử trong danh sách
[:arrow_up: 2. Phương thức sử dụng List](#2-phương-thức-sử-dụng-list)

_Ví dụ 1:_ Tìm một phần tử trong danh sách

Trong nhiều trường hợp, chúng ta không chỉ muốn biết danh sách có chứa một phần tử hay không, mà còn muốn biết chính xác vị trí mà phần tử đó xuất hiện trong danh sách. Khi đó, chúng ta sẽ sử dụng phương thức `index()` để tìm ra một phần tử trong danh sách. Phương thức `index()` sẽ nhận vào giá trị của phần tử làm một tham số và trả về giá trị xuất hiện đầu tiên của phần tử hoặc trả về `ValueError` nếu phần tử không tồn tại.

```python
my_list = list([1, 2, 3, 4, 3, 5, 6])
print(my_list.index(3)) # 2
```

#### g. Sắp xếp danh sách
[:arrow_up: 2. Phương thức sử dụng List](#2-phương-thức-sử-dụng-list)

Phương thức `sort()` được sử dụng để sắp xếp danh sách theo thứ tự giảm dần hoặc tăng dần theo giá trị của các phần tử trong danh sách đó. Cú pháp của phương thức `sort()` có dạng như sau:

```python
list.sort(key=..., reverse=...)
```

Trong đó `list` là tên của danh sách muốn thực hiện sắp xếp.

Theo mặc định, `sort()` không yêu cầu bất kỳ tham số bổ sung nào. Tuy nhiên, nó có hai tham số tùy chọn mà lập trình viên có thể sử dụng, bao gồm:

- `reverse`: Nếu giá trị là `True`, danh sách đã được sắp xếp sẽ bị đảo ngược (hoặc sắp xếp theo thứ tự giảm dần).
- `key`: Là một hàm đóng có nhiệm vụ chỉ định thuộc tính sắp xếp cho các phần tử con trong mảng.

Phương thức `sort()` sẽ không trả về bất kỳ giá trị nào. Nó sẽ thay đổi tập hợp kiểu danh sách ban đầu.

_Ví dụ 1:_

```python
vowels = ['e', 'a', 'u', 'o', 'i']
vowels.sort()
print('Sorted list:', vowels)
```

_Kết quả:_

```
Sorted list: ['a', 'e', 'i', 'o', 'u']
```

Phương thức `sort()` chấp nhận tham số `reverse` để thực hiện sắp xếp theo thứ tự giảm dần.

_Ví dụ 2:_

```python
vowels = ['e', 'a', 'u', 'o', 'i']
vowels.sort(reverse=True)
print('Sorted list (in Descending):', vowels)
```

_Kết quả:_

```
Sorted list (in Descending): ['u', 'o', 'i', 'e', 'a']
```

#### h. Đảo ngược danh sách
[:arrow_up: 2. Phương thức sử dụng List](#2-phương-thức-sử-dụng-list)

_Ví dụ 1:_ Đảo ngược danh sách

```python
mylist = [3, 4, 5, 6, 1]
mylist.reverse()
print(mylist)
```

_Kết quả:_

```
[1, 6, 5, 4, 3]
```

#### i. Tìm giá trị lớn nhất và nhỏ nhất trong danh sách
[:arrow_up: 2. Phương thức sử dụng List](#2-phương-thức-sử-dụng-list)

Hàm `max()` trả về giá trị lớn nhất trong danh sách, trong khi, hàm `min()` trả về giá trị nhỏ nhất trong danh sách.

_Ví dụ 1:_ 

```python
mylist = [3, 4, 5, 6, 1]
print(max(mylist))
print(min(mylist))
```

_Kết quả:_

```
6
1
```

#### j. Tính tổng các phần tử có trong danh sách
[:arrow_up: 2. Phương thức sử dụng List](#2-phương-thức-sử-dụng-list)

Python cung cấp hàm sum() trả về tổng của tất cả các phần tử có trong danh sách.

_Ví dụ 1:_

```python
mylist = [3, 4, 5, 6, 1]
print(sum(mylist)) # 19
```

#### k. Đếm số lần phần tử xuất hiện
[:arrow_up: 2. Phương thức sử dụng List](#2-phương-thức-sử-dụng-list)

Phương thức `count()` trả về số lần phần tử được chỉ định xuất hiện trong tập hợp danh sách. Phương thức này chỉ nhận duy nhất một tham số là phần tử cần được đếm số lần xuất hiện.

```python
vowels = ['a', 'e', 'i', 'o', 'i', 'u']
count = vowels.count('i')
print(count) # 2
```

#### l. Nối các danh sách
[:arrow_up: 2. Phương thức sử dụng List](#2-phương-thức-sử-dụng-list)

Việc nối hai danh sách có nghĩa là hợp nhất hai danh sách lại với nhau thành một danh sách chung tổng hợp có các phần tử là các phần tử của cả hai danh sách này. Có hai cách để làm điều đó.

- Sử dụng toán tử cộng (`+`).
- Sử dụng phương thức `extend()`. Phương thức `extend()` nối các phần tử của một danh sách vào cuối một danh sách khác. Cách này đã trình bày ở phần thêm phần tử vào danh sách ở bài trước.

_Ví dụ:_

```python
my_list1 = [1, 2, 3]
my_list2 = [4, 5, 6]

my_list3 = my_list1 + my_list2
print(my_list3) # [1, 2, 3, 4, 5, 6]

my_list1.extend(my_list2)
print(my_list1) # [1, 2, 3, 4, 5, 6]
```

Hãy chú ý, khi chúng ta sử dụng toán tử `+` thì chúng ta cần lưu danh sách tổng hợp từ phép nối vào một biến khác, còn khi sử dụng phương thức `extend()` thì kết quả của phép nối sẽ được thực hiện trực tiếp trên danh sách gọi phương thức đó.

#### m. Sao chép danh sách
[:arrow_up: 2. Phương thức sử dụng List](#2-phương-thức-sử-dụng-list)

Có hai cách để tạo một bản sao của danh sách:

- Sử dụng toán tử gán
- Sử dụng phương thức `copy()`

_Ví dụ 1:_ Sử dụng toán tử gán

```python
my_list1 = [1, 2, 3]
new_list = my_list1

print(new_list) # [1, 2, 3]
my_list1.append(4)
print(my_list1) # [1, 2, 3, 4]
print(new_list) # [1, 2, 3, 4]
```

_Ví dụ 2:_ Sử dụng phương thức `copy()`

```python
my_list1 = [1, 2, 3]
new_list = my_list1.copy()

print(new_list) # [1, 2, 3]
my_list1.append(4)

print(my_list1) # [1, 2, 3, 4]
print(new_list) # [1, 2, 3]
```

#### n. Kiểm tra tất cả giá trị trong danh sách
[:arrow_up: 2. Phương thức sử dụng List](#2-phương-thức-sử-dụng-list)

Kiểm tra tất cả giá trị trong danh sách với `all()`

Trong trường hợp của hàm `all()`, giá trị trả về sẽ là `True` khi tất cả các giá trị bên trong danh sách đều là `True`. Do đó, chúng ta có thể sử dụng 1 danh sách để lưu các giá trị đúng sai của các biểu thức, sau đó sử dụng hàm `all()` lên danh sách này. Khi đó, nó sẽ tương đương với việc chúng ta sử dụng phép toán logic `and` giữa tất cả các phần tử hay giá trị của biểu thức Boolean thuộc danh sách này.

| Các giá trị có trong danh sách |  Giá trị trả về |
| :--: | :--: |
| Tất cả các giá trị đều đúng | True |
| 1 hoặc nhiều giá trị False | False | 
| Tất cả các giá trị là False | False |
| Danh sách rỗng | True |

_Ví dụ 1:_ 

```python
samplelist1 = [1,1,True]
print(all(samplelist1)) # True

samplelist2 = [0,1,True,1]
print(all(samplelist2)) # False

samplelist3 = [0,0,False]
print(all(samplelist3)) # False

samplelist4 = []
print(all(samplelist4)) # True
```

#### o. Kiểm tra giá trị trong danh sách
[:arrow_up: 2. Phương thức sử dụng List](#2-phương-thức-sử-dụng-list)

Kiểm tra giá trị trong danh sách với `any()`

Hàm `any()` sẽ trả về `True` nếu có ít nhất một giá trị `True`. Trong trường hợp danh sách rỗng, nó sẽ trả về `False`. Chúng ta có thể sử dụng hàm `any()` như sử dụng toán tử `or` với danh sách các biểu thức.

| Các giá trị có trong danh sách |  Giá trị trả về |
| :--: | :--: |
| Tất cả các giá trị là True | True |
| 1 hoặc nhiều giá trị False | True | 
| Tất cả các giá trị là False | False |
| Danh sách rỗng | False |

_Ví dụ 1:_

```python
samplelist1 = [1,1,True]
print(any(samplelist1)) # True

samplelist2 = [0,1,True,1]
print(any(samplelist2)) # True

samplelist3 = [0,0,False]
print(any(samplelist3)) # False

samplelist4 = []
print(any(samplelist4)) # False
```

## IV. Các thao tác trên chuỗi ký tự
[:arrow_up: Mục lục](#mục-lục)

### 1. Một số thao tác trên chuỗi ký tự trên Python
[:arrow_up: Mục lục](#mục-lục)

**1. Chỉ số của chuỗi ký tự trong Python**

Như đã biết, chuỗi ký tự là một tập hợp của các ký tự được sắp xếp theo thứ tự nhất định. Chúng ta có thể truy cập các ký tự riêng lẻ của chuỗi bằng cách sử dụng chỉ số thể hiện vị trí của ký tự đó trong chuỗi. Chỉ số đầu tiên sẽ bắt đầu từ giá trị là 0. Tức là chuỗi ký tự sẽ được đánh số từ ký tự 0, ký tự 1,...cho đến ký tự cuối cùng.

Chẳng hạn với chuỗi `Python TEK4.VN!` thì chỉ số của các ký tự sẽ được đánh số như sau:

![image](https://github.com/user-attachments/assets/538dc209-cc9c-4564-bc00-ef1ca21b49fb)

**2. Làm thế nào để truy cập các ký tự trong một chuỗi?**

Chúng ta có thể truy cập các ký tự của chuỗi thông qua các chỉ số của nó. Để làm được điều này, chúng ta chỉ cần đặt chỉ số muốn truy cập vào trong dấu ngoặc vuông (`[]`). Với lưu ý rằng CHỈ SỐ CỦA CHUỖI BẮT ĐẦU TỪ `0` !!!!

_Ví dụ 1:_

```python
a = 'Python TEK4.VN!'
print(a)
print(a[2]) # Lấy ký tự thứ 3
```

_Kết quả:_

```
Python
t
```

Ở ví dụ trên, chúng ta truy cập và in ra ký tự **thứ 3** trong chuỗi (lưu ý đánh **chỉ số từ 0** do đó để truy cập **ký tự thứ 3** của chuỗi, chúng ta cần đưa vào chỉ số cần truy cập là **2**).

Một điều đặc biệt trong Python, đó là nó cho phép sử dụng chỉ số âm để truy cập vào phần tử của chuỗi. **Chỉ số -1** tham chiếu đến ký tự cuối cùng, **-2** tham chiếu đến phần tử cuối cùng thứ hai (tính từ phải sang),...Quy tắc về chỉ số này tương tự như quy tắc về chỉ số đối với danh sách.

Chẳng hạn, chuỗi **"Python TEK4.VN!"** khi đánh chỉ số âm thì các ký tự sẽ có chỉ số như sau:

![image](https://github.com/user-attachments/assets/a1b497c6-d320-46d1-9e4b-9b385bfbac3f)

Bằng cách sử dụng chỉ số âm, chúng ta có thể lấy được ký tự `o` bằng cách tham chiếu đến vị trí của nó trong chuỗi với **chỉ số là -11**

_Ví dụ 2:_

```python
a = 'Python TEK4.VN!'
print(a[-11]) # Lấy ký tự vị trí -11
```

_Kết quả:_

```
o
```

**3. Cắt chuỗi và lấy chuỗi con**

Chúng ta có thể truy cập nhiều phần tử trong một chuỗi ký tự (để lấy một chuỗi con) bằng cách sử dụng phép cắt chuỗi. Phép cắt chuỗi này hoạt động theo nguyên tắc tương tự như phép cắt danh sách lấy danh sách con. Để cắt chuỗi, chúng ta chỉ định vị trí bắt đầu cắt và vị trí kết thúc việc cắt, và phân tách hai vị trí này bởi dấu hai chấm `[x:y]`. Khi thực hiện việc cắt chuỗi, chỉ số đầu tiên là vị trí bắt đầu được cắt (lấy cả ký tự ứng với chỉ số này), còn chỉ số thứ hai là vị trí kết thúc cắt (không lấy ký tự tại vị trí này). Kết quả ta lấy được một chuỗi con trong khoảng tương ứng.

_Ví dụ 1:_

```python
my_string = "Python is easy"
a1=my_string[0:3] #Lấy các ký tự từ ký tự 0 tới ký tự 2
a2=my_string[2:-2] #Lấy các ký tự từ ký tự 2 tới ký tự 11 (-3)
print(a1) # Pyt
print(a2) # thon is ea
```

Ở đây chúng ta lưu ý, chuỗi con được cắt ra sẽ bao gồm các ký tự từ vị trí đầu tiên đến vị trí cuối cùng (không bao gồm ký tự vị trí cuối cùng). Khi chỉ số kết thúc nhỏ hơn hoặc bằng chỉ số đầu thì chương trình vẫn không báo lỗi mà sẽ in ra chuỗi ký tự rỗng.

Ngoài ra, chúng ta có thể lấy tiền tố và hậu tố của một chuỗi bằng cách bỏ qua một chỉ số trong cú pháp `string[m:n]`.

_Ví dụ 2:_

```python
my_string = "Python is easy"
print(my_string[2:]) #Lấy hậu tố của chuỗi là tất cả ký tự bắt đầu từ vị trí 2 đến hết
print(my_string[:-1]) #Lấy tiền tố của chuỗi tất cả ký tự từ đầu cho tới trước ký tự cuối cùng (-2)
```

_Kết quả:_

```
thon is easy
Python is eas
```

Hãy nhớ câu kinh điển "Giữ đầu bỏ đuôi".

Trong đoạn mã trên:

- `[2:]`: Tất cả các **ký tự từ chỉ số 2** đến chỉ số cuối cùng được lấy ra (tính từ `0` nên là **ký tự thứ 3**).
- `[: -1]`: Tất cả văn bản trước chỉ số cuối cùng được lấy ra (bỏ đuôi nên chỉ lấy đến ký tự có chỉ số là **-2** tức là ký tự gần cuối cùng).
- 
Ở đây, các giá trị được bỏ cách sẽ được hiểu là không được chỉ định và sẽ lấy đến giá trị cực trị của nó có thể có.

**4. Bước nhảy khi lấy chuỗi con**

Phép cắt chuỗi trong Python tương tự như phép cắt danh sách còn cho phép sử dụng một tham số thứ ba bên cạnh chỉ số bắt đầu và kết thúc. Tham số này được gọi là bước nhảy (stride), thể hiện số ký tự nhảy cách khi lấy chuỗi con. Dạng tổng quát của phép cắt chuỗi như sau:

```python
string[start:end:stride]
```

Trong các ví dụ trước, chúng ta bỏ qua tham số `stride`, và khi đó Python sẽ hiểu rằng mặc định của bước nhảy là `1`, hay tất cả các ký tự giữa hai chỉ số `start` và `end` đều được lấy. Quay lại ví dụ 1, câu lệnh đầy đủ để thực hiện cùng chức năng lấy ra chuỗi con trong khoảng từ `[0,3]` sẽ là:

_Ví dụ 1:_

```python
my_string = "Python is easy"
print(my_string[2:12:2]) # to se
print(my_string[2:12:3]) # tnsa
```

Bằng cách sử dụng giá trị bước nhảy là **2** ở tham số cuối, ta sẽ thấy rằng chuỗi con sẽ bỏ cách các ký tự xen giữa. Trong trường hợp bước nhảy là **3** thì nó sẽ **bỏ cách 3 ký tự**.

Khi chúng ta chỉ muốn lấy ra các ký tự có chỉ số chẵn của chuỗi, ta có thể thực hiện:

_Ví dụ 2:_

```python
my_string = "Python is easy"
print(my_string[::2]) # Pto ses
```

**5. Đảo ngược chuỗi ký tự**

Để đảo ngược một chuỗi ký tự, chúng ta có thể thực hiện một cách rất đơn giản đó là đặt tham số bước nhảy là -1:

_Ví dụ:_

```python
my_string = "Python is easy"
print(my_string[::-1]) # ysae si nohtyP
print(my_string[::-2]) # ya inhy
```

Hai tham số đầu chúng ta để trống để lấy toàn bộ chuỗi gốc, nếu bước nhảy bằng `1` thì chúng ta sẽ lấy được toàn bộ các ký tự của chuỗi mà không bỏ qua ký tự nào, và trong trường hợp bước nhảy là âm thì chuỗi ký tự ban đầu sẽ bị đảo ngược. Nếu chúng ta làm lại với bước nhảy bằng `-2`, thì việc nhảy cách vẫn diễn ra bình thường.

**6. Đếm số ký tự trong chuỗi**

Chúng ta có thể đếm số ký tự hoặc xác định độ dài của chuỗi ký tự tương tự như đếm số lượng phần tử trong danh sách bằng cách sử dụng hàm `len()` trong Python.

_Ví dụ:_

```python
my_string = "Python is easy"
print(len(my_string)) # 14
```

**7. Kiểm tra thành viên của một chuỗi ký tự**

Chúng ta có thể kiểm tra xem một chuỗi con có tồn tại trong một chuỗi hay không bằng cách sử dụng từ khóa `in` hoặc `not in`.

_Ví dụ:_

```python
my_string = "Python is easy"
print('P' in my_string) # True
print('Q' in my_string) # False
print ("Python" in my_string) # True
print ("TEK4.VN" not in my_string) # True
```

**8. Làm thế nào để thay đổi hoặc xóa một chuỗi ký tự?**

Một điều đặc biệt khác **trong Python đó là chuỗi ký tự có tính bất biến**. Điều này có nghĩa là các **phần tử của một chuỗi ký tự sẽ không thể thay đổi giá trị sau khi chúng đã được gán bởi các giá trị đã có**. Tuy nhiên, chúng ta có thể gán lại một chuỗi ký tự khác cho cùng một biến.

_Ví dụ 1:_

```python
a = 'Python'
print(a)
a[0] = 'A' #Lỗi
print(a)
a = 'Javascript'
print(a)
```

_Kết quả:_

```
Python
Traceback (most recent call last):
  File "main.py", line 3, in <module>
    a[0] = 'A' // Lỗi
NameError: name 'Lỗi' is not defined
```

Điều này có vẻ khá bất tiện phải không ạ?

Tuy nhiên, trên thực tế, không có nhiều trường hợp mà chúng ta cần phải sửa đổi các phần tử trong một chuỗi. Nếu thực sự cần, bạn có thể dễ dàng làm được việc này với một mẹo nhỏ. Đó là tạo ra một bản sao của chuỗi mong muốn với các phần được cắt và ghép một cách phù hợp từ các chuỗi con. Có nhiều cách để làm điều này. Ta có thể xem xét ví dụ sau:

_Ví dụ 2:_

```python
s="Học Python với tek4.vn"
s_new = s[:4] + 'Java' + s[10:]
print(s_new)
```

_Kết quả:_

```
Học Java với tek4.vn
```

Bạn có thể thấy rằng, bằng một cách hết sức đơn giản đó là tách các chuỗi con và ghép lại, chúng ta đã thu được một chuỗi mới theo đúng yêu cầu thay đổi.

Chúng ta cũng có thể có một cách khác. Đó là sử dụng phương thức `replace()`. Đây là phương thức đặc biệt được hỗ trợ để thay đổi giá trị của chuỗi ký tự.

_Ví dụ 3:_

```python
s = 'I love you'
s = s.replace('love', 'like')
print(s)
```

_Kết quả:_

```
I like you
```

Tương tự, chúng ta cũng **không thể xóa hoặc loại bỏ các ký tự khỏi một chuỗi**. Nhưng việc **xóa toàn bộ chuỗi ký tự hoàn toàn có thể thực hiện** được bằng cách sử dụng từ khóa `del`.

_Ví dụ 4:_

```python
a = 'Python'
print(a)
#del a[0] # Lỗi
del a # Hợp lệ
print(a)
```

_Kết quả:_

```
Python
Traceback (most recent call last):
  File "e:/Learning/IT/Python/Bai2.py", line 5, in <module>
    print(a)
NameError: name 'a' is not defined
```

Ở đây, do chúng ta đã xoá biến `a`, do đó, khi thực hiện câu lệnh in ra biến `a` thì chương trình sẽ báo lỗi rằng `a` chưa được khai báo!!!!

Một điều cần lưu ý nữa là: Tuy Python là tập hợp của các ký tự, nhưng chúng ta lại không thể khai báo một chuỗi ký tự bằng cách viết nó dưới dạng tập hợp như danh sách `['p','y','t','h','o','n']`. Nếu chúng ta khai báo như trên nó sẽ trở thành một dữ liệu dạng danh sách và không phải là chuỗi ký tự. Cách duy nhất để khai báo các chuỗi ký tự đó là sử dụng các dấu nháy đơn (`'`) hoặc nháy kép (`"`).

**9. So sánh hai chuỗi ký tự**

Kiểu chuỗi ký tự cũng tương tự như các kiểu dữ liệu cơ bản khác như số thực hay số nguyên. Chúng ta cũng có thể so sánh được giá trị của hai chuỗi ký tự.

_Ví dụ 1:_

```python
s1="Python"
s2="Python"
s3="Java"
s4="12345"
s5="12346"

print(s1==s2) # True
print(s4<s5) # True
print(s3>s1) # False
```

Các chuỗi ký tự sẽ được so sánh theo giá trị của từng ký tự tại từng vị trí một cách lần lượt. Nếu hai chuỗi có phần đầu bằng nhau thì chuỗi nào dài hơn sẽ lớn hơn, chuỗi nào có ký tự đầu tiên lớn hơn ký tự của chuỗi còng lại sẽ giống nhau. Cách thức so sánh này tương tự như khi chúng ta so sánh hai danh sách với nhau.

_Ví dụ 2:_

```python
l1=[1,2,3,4]
l2=[1,2,3,4]
l3=[1,2,3,5]
print(l1==l2) # True
print(l3>l1) # True
```


