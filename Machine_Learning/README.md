# Machine Learning
## Mục lục

## I. Tổng quan về Machine Learning
### 1. Machine Learning hoạt động như thế nào?

Nguyên tắc hoạt động của machine learning tương tự như bộ não con người đó là học từ kinh nghiệm

![image](https://github.com/user-attachments/assets/b66d7297-df1c-442d-84c1-ff86b859889d)

Mục tiêu của quá trình huấn luyện là tạo ra các mô hình được sử dụng cho quá trình dự đoán, các mô hình này sẽ được lưu lại và sử dụng trong các sản phẩm

![image](https://github.com/user-attachments/assets/363c27df-acaf-4abe-a0c4-7595b553c0d1)

Sau đó mô hình này sẽ được dùng để dự đoán kết quả với đầu vào do người dùng cung cấp

### 2. Những khái niệm cơ bản

Quan sát (**Observation**): Là dữ liệu đầu vào (input) của bài toán, thường có dạng là một vector x = <math>(x₁, x₂, ..., xₙ) ∈ ℝⁿ</math> được gọi là vector đặc trưng (feature vector) và mỗi xi là một đặc trưng (**feature**). Ví dụ bạn muốn đoán giá nhà dựa vào các dữ liệu quan sát gồm các feature (vị trí nhà, hướng nhà, tình trạng giao thông, cơ sở hạ tầng, giá nhà trung bình…).

Nhãn (**Label**): Là đầu ra cần dự đoán của bài toán (với bài toán học có giám sát). Mỗi quan sát sẽ có thể có một nhãn tương ứng trong dữ liệu. Ở ví dụ trên label giá nhà có thể là 1 tỷ, 2 tỷ, 2.5 tỷ… hoặc trong một số bài toán với điều kiện nhà như vậy thì có quyết định “Mua” hay “Không mua”. Nhãn có thể mang nhiều dạng nhưng đều có thể chuyển đổi thành một số thực hoặc một vector.

Tập dữ liệu (**dataset**): là tập hợp của các quan sát hay các mẫu dữ liệu và các nhãn nếu có được sử dụng để xây dựng mô hình.

Mô hình (**Model**): là một hàm số f(x) hoặc một quy tắc R cho phép ánh xạ dữ liệu quan sát sang một dự đoán đầu ra (có thể là nhãn của dữ liệu hoặc mối quan hệ trong dữ liệu).

Tham số (**parameter**): là mọi thứ của mô hình được sử dụng để tính toán ra giá trị đầu ra. Chẳng hạn model là một hàm đa thức bậc hai: f(x) = a*x² + b*x + c thì tham số của mô hình là a, b, c. Ngoài ra, còn một loại tham số đặc biệt khác gọi là siêu tham số (**hyperparameter**). Đây là một khái niệm mang tính chất khá tương đối chỉ các tham số có dạng cố định và không thay đổi trong quá trình huấn luyện. Đối với hàm đa thức ở trên thì bậc của đa thức có thể được xem là một siêu tham số.

