# BÁO CÁO ĐỒ ÁN TỐT NGHIỆP

## HỆ THỐNG QUẢN LÝ PHÒNG KHÁM VÀ ĐẶT LỊCH KHÁM TRỰC TUYẾN

---

**Sinh viên thực hiện:** [Tên sinh viên]  
**Mã số sinh viên:** [MSSV]  
**Lớp:** [Tên lớp]  
**Khoa:** Công nghệ Thông tin  
**Trường:** [Tên trường]  

**Giảng viên hướng dẫn:** [Tên giảng viên]  

**Thời gian thực hiện:** [Thời gian]

---

## LỜI CẢM ƠN

Tôi xin chân thành cảm ơn thầy/cô [Tên giảng viên hướng dẫn] đã tận tình hướng dẫn, chỉ bảo và đưa ra những góp ý quý báu trong suốt quá trình thực hiện đồ án này.

Tôi cũng xin gửi lời cảm ơn đến các thầy cô trong khoa Công nghệ Thông tin đã truyền đạt những kiến thức chuyên môn vững chắc, tạo nền tảng để tôi có thể hoàn thành đồ án này.

Cuối cùng, tôi xin cảm ơn gia đình, bạn bè đã luôn động viên, hỗ trợ tôi trong suốt quá trình học tập và thực hiện đồ án.

Mặc dù đã cố gắng hết sức, nhưng đồ án không tránh khỏi những thiếu sót. Tôi rất mong nhận được sự góp ý của các thầy cô để đồ án được hoàn thiện hơn.

Xin chân thành cảm ơn!

---

## MỤC LỤC

**LỜI CẢM ƠN** .................................................... 2

**MỤC LỤC** ........................................................ 3

**DANH SÁCH HÌNH ẢNH VÀ BẢNG BIỂU** ................................. 5

**TÓM TẮT ĐỀ TÀI** ................................................. 6

**GIỚI THIỆU** ..................................................... 7

**CHƯƠNG 1: TỔNG QUAN VỀ HỆ THỐNG** ................................. 9

**CHƯƠNG 2: CƠ SỞ LÝ THUYẾT VÀ CÔNG NGHỆ** ......................... 17

**CHƯƠNG 3: PHÂN TÍCH VÀ THIẾT KẾ HỆ THỐNG** ....................... 27

**CHƯƠNG 4: TRIỂN KHAI HỆ THỐNG** .................................. 39

**CHƯƠNG 5: ĐÁNH GIÁ VÀ KẾT QUẢ** ................................. 54

**KẾT LUẬN VÀ KIẾN NGHỊ** .......................................... 57

**TÀI LIỆU THAM KHẢO** ............................................. 59

**PHỤ LỤC** ........................................................ 60

---
## DANH SÁCH HÌNH ẢNH VÀ BẢNG BIỂU

### Danh sách hình ảnh
- Hình 1.1: Quy trình khám bệnh truyền thống
- Hình 1.2: Mô hình hệ thống quản lý phòng khám số hóa
- Hình 2.1: Kiến trúc Django MTV
- Hình 2.2: Cấu trúc thư mục Django project
- Hình 3.1: Use case diagram tổng thể
- Hình 3.2: Sơ đồ ERD của hệ thống
- Hình 3.3: Wireframe giao diện chính
- Hình 3.4: Kiến trúc tổng thể hệ thống
- Hình 4.1: Giao diện đăng nhập
- Hình 4.2: Dashboard bệnh nhân
- Hình 4.3: Danh sách bác sĩ
- Hình 4.4: Form đặt lịch khám
- Hình 4.5: Dashboard bác sĩ
- Hình 4.6: Form tạo hồ sơ bệnh án
- Hình 4.7: Dashboard admin
- Hình 4.8: Quản lý bác sĩ

### Danh sách bảng biểu
- Bảng 2.1: So sánh các framework web Python
- Bảng 3.1: Phân tích yêu cầu chức năng
- Bảng 3.2: Phân tích yêu cầu phi chức năng
- Bảng 3.3: Mô tả các bảng trong cơ sở dữ liệu
- Bảng 4.1: Cấu trúc thư mục dự án
- Bảng 4.2: Danh sách các models
- Bảng 4.3: Danh sách các views
- Bảng 4.4: Danh sách templates
- Bảng 5.1: Kết quả kiểm thử chức năng
- Bảng 5.2: Đánh giá hiệu năng hệ thống

---

## TÓM TẮT ĐỀ TÀI

Trong bối cảnh công nghệ thông tin phát triển mạnh mẽ và nhu cầu số hóa trong lĩnh vực y tế ngày càng tăng cao, việc xây dựng một hệ thống quản lý phòng khám hiện đại, hiệu quả là vô cùng cần thiết. Đồ án này trình bày quá trình phát triển một hệ thống quản lý phòng khám và đặt lịch khám trực tuyến sử dụng Django framework.

**Mục tiêu của đồ án:**
- Xây dựng hệ thống quản lý phòng khám toàn diện, hỗ trợ ba đối tượng chính: bệnh nhân, bác sĩ và quản trị viên
- Tự động hóa quy trình đặt lịch khám, giảm thiểu thời gian chờ đợi và tăng hiệu quả công việc
- Số hóa hồ sơ bệnh án, tạo điều kiện thuận lợi cho việc lưu trữ và tra cứu thông tin
- Cung cấp giao diện thân thiện, dễ sử dụng cho tất cả người dùng

**Phương pháp nghiên cứu:**
Đồ án sử dụng phương pháp nghiên cứu ứng dụng, kết hợp giữa nghiên cứu lý thuyết về các công nghệ web hiện đại và thực hành phát triển hệ thống thực tế. Quá trình phát triển tuân theo mô hình Waterfall với các giai đoạn: phân tích yêu cầu, thiết kế, triển khai, kiểm thử và bảo trì.

**Công nghệ sử dụng:**
- Backend: Django 5.2.8 (Python framework)
- Frontend: HTML5, CSS3, JavaScript, Bootstrap
- Cơ sở dữ liệu: SQLite
- Môi trường phát triển: Python 3.14, Visual Studio Code

**Kết quả đạt được:**
Hệ thống đã được phát triển thành công với đầy đủ các chức năng cơ bản:
- Quản lý người dùng với 3 vai trò: bệnh nhân, bác sĩ, admin
- Hệ thống đặt lịch khám trực tuyến tự động
- Quản lý hồ sơ bệnh án điện tử
- Dashboard thống kê cho từng vai trò
- Giao diện responsive, thân thiện với người dùng

Hệ thống đã được kiểm thử và hoạt động ổn định, đáp ứng được các yêu cầu đặt ra ban đầu. Đây là nền tảng tốt để phát triển thành một sản phẩm thương mại trong tương lai.

---

## GIỚI THIỆU

### Lý do chọn đề tài

Trong thời đại công nghệ 4.0, việc số hóa các dịch vụ y tế đã trở thành xu hướng tất yếu trên toàn thế giới. Tại Việt Nam, mặc dù ngành y tế đã có những bước tiến đáng kể, nhưng việc ứng dụng công nghệ thông tin vào quản lý phòng khám vẫn còn nhiều hạn chế, đặc biệt là tại các phòng khám tư nhân quy mô nhỏ và vừa.

Hiện tại, hầu hết các phòng khám vẫn sử dụng phương pháp quản lý truyền thống với sổ sách giấy tờ, gây ra nhiều bất tiện:
- Bệnh nhân phải đến trực tiếp để đặt lịch, tốn thời gian và công sức
- Khó khăn trong việc quản lý lịch hẹn, dễ xảy ra trùng lặp hoặc nhầm lẫn
- Hồ sơ bệnh án giấy dễ thất lạc, khó bảo quản và tra cứu
- Không có thống kê tự động, khó đánh giá hiệu quả hoạt động

Nhận thấy những vấn đề trên, tôi quyết định chọn đề tài "Hệ thống quản lý phòng khám và đặt lịch khám trực tuyến" nhằm ứng dụng kiến thức đã học để xây dựng một giải pháp công nghệ thiết thực, góp phần cải thiện chất lượng dịch vụ y tế.

### Mục tiêu nghiên cứu

**Mục tiêu tổng quát:**
Xây dựng một hệ thống quản lý phòng khám toàn diện, hiện đại, giúp tự động hóa các quy trình nghiệp vụ và nâng cao hiệu quả hoạt động của phòng khám.

**Mục tiêu cụ thể:**
1. **Đối với bệnh nhân:**
   - Cung cấp nền tảng đặt lịch khám trực tuyến tiện lợi, tiết kiệm thời gian
   - Cho phép xem lịch sử khám bệnh và hồ sơ bệnh án cá nhân
   - Cung cấp thông tin chi tiết về bác sĩ và chuyên khoa

2. **Đối với bác sĩ:**
   - Hỗ trợ quản lý lịch hẹn một cách hiệu quả
   - Số hóa việc tạo và lưu trữ hồ sơ bệnh án
   - Cung cấp dashboard theo dõi hoạt động khám bệnh

3. **Đối với quản trị viên:**
   - Quản lý tập trung thông tin bác sĩ và bệnh nhân
   - Cung cấp báo cáo thống kê chi tiết về hoạt động phòng khám
   - Kiểm soát quyền truy cập và bảo mật thông tin

### Phạm vi nghiên cứu

**Phạm vi về chức năng:**
- Quản lý người dùng (bệnh nhân, bác sĩ, admin)
- Hệ thống đặt lịch khám trực tuyến
- Quản lý hồ sơ bệnh án điện tử
- Báo cáo và thống kê
- Bảo mật và phân quyền

**Phạm vi về công nghệ:**
- Sử dụng Django framework cho backend
- Giao diện web responsive với HTML, CSS, JavaScript
- Cơ sở dữ liệu SQLite cho môi trường phát triển
- Triển khai trên môi trường local

**Phạm vi về đối tượng:**
- Phòng khám tư nhân quy mô nhỏ và vừa
- Hỗ trợ tiếng Việt
- Tối ưu cho thị trường Việt Nam

### Phương pháp nghiên cứu

**1. Phương pháp nghiên cứu tài liệu:**
- Nghiên cứu các tài liệu về Django framework và web development
- Tìm hiểu các hệ thống quản lý phòng khám hiện có
- Nghiên cứu các chuẩn bảo mật trong lĩnh vực y tế

**2. Phương pháp phân tích và thiết kế:**
- Phân tích yêu cầu nghiệp vụ của phòng khám
- Thiết kế cơ sở dữ liệu và kiến trúc hệ thống
- Thiết kế giao diện người dùng

**3. Phương pháp thực nghiệm:**
- Phát triển hệ thống theo mô hình Waterfall
- Kiểm thử từng module và tích hợp
- Đánh giá hiệu năng và tối ưu hóa

**4. Phương pháp đánh giá:**
- Kiểm thử chức năng và phi chức năng
- Thu thập phản hồi từ người dùng thử nghiệm
- Phân tích kết quả và đề xuất cải tiến

### Ý nghĩa khoa học và thực tiễn

**Ý nghĩa khoa học:**
- Ứng dụng thành công Django framework vào lĩnh vực y tế
- Đề xuất mô hình kiến trúc phù hợp cho hệ thống quản lý phòng khám
- Nghiên cứu và triển khai các giải pháp bảo mật thông tin y tế

**Ý nghĩa thực tiễn:**
- Cung cấp giải pháp công nghệ thiết thực cho các phòng khám
- Góp phần số hóa ngành y tế Việt Nam
- Tạo nền tảng để phát triển thành sản phẩm thương mại
- Nâng cao chất lượng dịch vụ y tế và trải nghiệm bệnh nhân

---
# CHƯƠNG 1: TỔNG QUAN VỀ HỆ THỐNG

## 1.1. Giới thiệu về quản lý phòng khám

### 1.1.1. Khái niệm phòng khám

Phòng khám là cơ sở y tế cung cấp dịch vụ khám bệnh, chữa bệnh cho người dân, thường có quy mô nhỏ hơn bệnh viện và tập trung vào các dịch vụ y tế cơ bản. Theo Luật Khám bệnh, chữa bệnh của Việt Nam, phòng khám được phân loại thành:

- **Phòng khám đa khoa:** Cung cấp dịch vụ khám và điều trị nhiều chuyên khoa
- **Phòng khám chuyên khoa:** Tập trung vào một lĩnh vực y tế cụ thể
- **Phòng khám tư nhân:** Do cá nhân hoặc tổ chức tư nhân thành lập và quản lý

### 1.1.2. Quy trình quản lý phòng khám truyền thống

Quy trình quản lý phòng khám truyền thống thường bao gồm các bước sau:

1. **Tiếp nhận bệnh nhân:**
   - Bệnh nhân đến trực tiếp tại phòng khám
   - Đăng ký thông tin cá nhân vào sổ sách
   - Nhận số thứ tự và chờ đợi

2. **Quản lý lịch hẹn:**
   - Ghi chép lịch hẹn trên sổ giấy hoặc lịch treo tường
   - Điều phối thủ công giữa các bác sĩ
   - Thông báo lịch hẹn qua điện thoại

3. **Khám bệnh và điều trị:**
   - Bác sĩ khám bệnh và ghi chép trên giấy
   - Tạo hồ sơ bệnh án bằng tay
   - Kê đơn thuốc trên giấy

4. **Lưu trữ hồ sơ:**
   - Hồ sơ được lưu trong tủ hồ sơ
   - Phân loại theo tên hoặc mã số bệnh nhân
   - Tra cứu thủ công khi cần thiết

### 1.1.3. Hạn chế của phương pháp truyền thống

**Đối với bệnh nhân:**
- Phải đến trực tiếp để đặt lịch, tốn thời gian di chuyển
- Thời gian chờ đợi lâu do không biết trước lịch trình
- Khó theo dõi lịch sử khám bệnh cá nhân
- Dễ thất lạc hồ sơ bệnh án

**Đối với bác sĩ:**
- Khó quản lý lịch làm việc cá nhân
- Tốn thời gian ghi chép thủ công
- Khó tra cứu thông tin bệnh nhân cũ
- Không có thống kê tự động về hoạt động khám bệnh

**Đối với phòng khám:**
- Chi phí cao cho việc in ấn, lưu trữ giấy tờ
- Rủi ro mất mát, hư hỏng hồ sơ
- Khó thống kê doanh thu và hiệu quả hoạt động
- Không thể mở rộng quy mô dễ dàng

## 1.2. Tình hình hiện tại của các phòng khám

### 1.2.1. Thống kê về phòng khám tại Việt Nam

Theo số liệu từ Bộ Y tế năm 2023:
- Cả nước có khoảng 15.000 phòng khám tư nhân
- 70% phòng khám vẫn sử dụng phương pháp quản lý truyền thống
- Chỉ 30% phòng khám đã ứng dụng công nghệ thông tin một phần
- Dưới 10% phòng khám có hệ thống quản lý hoàn chỉnh

### 1.2.2. Thách thức hiện tại

**1. Áp lực cạnh tranh:**
- Số lượng phòng khám tăng nhanh
- Bệnh nhân ngày càng đòi hỏi dịch vụ chất lượng cao
- Cần cải thiện trải nghiệm khách hàng để giữ chân bệnh nhân

**2. Yêu cầu pháp lý:**
- Quy định về lưu trữ hồ sơ bệnh án ngày càng nghiêm ngặt
- Cần đảm bảo bảo mật thông tin cá nhân theo GDPR
- Yêu cầu báo cáo định kỳ cho cơ quan quản lý

**3. Thay đổi hành vi người tiêu dùng:**
- Thế hệ trẻ quen với việc đặt dịch vụ online
- Mong muốn được thông báo và nhắc nhở tự động
- Cần truy cập thông tin y tế cá nhân mọi lúc, mọi nơi

### 1.2.3. Cơ hội phát triển

**1. Hỗ trợ từ chính phủ:**
- Chương trình chuyển đổi số quốc gia
- Ưu đãi thuế cho doanh nghiệp ứng dụng công nghệ
- Đầu tư vào hạ tầng internet và viễn thông

**2. Sự phát triển của công nghệ:**
- Chi phí phát triển phần mềm giảm
- Công nghệ cloud computing phổ biến
- Các framework web ngày càng dễ sử dụng

**3. Nhu cầu thị trường:**
- Dân số già hóa, nhu cầu y tế tăng cao
- Thu nhập người dân tăng, sẵn sàng chi trả cho dịch vụ tốt
- Ý thức về sức khỏe ngày càng được quan tâm

## 1.3. Nhu cầu số hóa trong y tế

### 1.3.1. Xu hướng toàn cầu

**Digital Health Revolution:**
Theo báo cáo của WHO (2023), ngành y tế toàn cầu đang trải qua cuộc cách mạng số hóa với các đặc điểm:
- 85% bệnh viện lớn đã triển khai hệ thống quản lý bệnh viện (HIS)
- 60% bệnh nhân sử dụng ứng dụng di động để quản lý sức khỏe
- Thị trường Digital Health dự kiến đạt 659 tỷ USD vào năm 2025

**Telemedicine và Remote Care:**
- Dịch COVID-19 đã thúc đẩy mạnh mẽ việc khám bệnh từ xa
- 40% cuộc hẹn y tế được thực hiện online trong năm 2022
- Tiết kiệm 30-50% chi phí so với khám bệnh truyền thống

### 1.3.2. Lợi ích của số hóa trong y tế

**1. Cải thiện chất lượng chăm sóc:**
- Giảm sai sót y khoa nhờ hệ thống cảnh báo tự động
- Tăng độ chính xác trong chẩn đoán với hỗ trợ AI
- Theo dõi liên tục tình trạng sức khỏe bệnh nhân

**2. Tăng hiệu quả hoạt động:**
- Giảm 40% thời gian xử lý hành chính
- Tối ưu hóa lịch trình làm việc của bác sĩ
- Tự động hóa các quy trình lặp lại

**3. Tiết kiệm chi phí:**
- Giảm chi phí in ấn, lưu trữ giấy tờ
- Tối ưu hóa nhân lực
- Giảm chi phí vận hành tổng thể 20-30%

**4. Nâng cao trải nghiệm bệnh nhân:**
- Đặt lịch hẹn 24/7 từ bất kỳ đâu
- Nhận thông báo và nhắc nhở tự động
- Truy cập hồ sơ y tế cá nhân mọi lúc

### 1.3.3. Thách thức trong số hóa y tế

**1. Bảo mật và quyền riêng tư:**
- Thông tin y tế là dữ liệu nhạy cảm, cần bảo vệ nghiêm ngặt
- Tuân thủ các quy định về bảo vệ dữ liệu cá nhân
- Nguy cơ tấn công mạng và rò rỉ thông tin

**2. Chi phí đầu tư ban đầu:**
- Phát triển và triển khai hệ thống tốn kém
- Đào tạo nhân viên sử dụng công nghệ mới
- Nâng cấp hạ tầng công nghệ

**3. Kháng cự thay đổi:**
- Nhân viên y tế quen với phương pháp truyền thống
- Bệnh nhân lớn tuổi khó tiếp cận công nghệ
- Cần thời gian để thích nghi với hệ thống mới

## 1.4. Các hệ thống quản lý phòng khám hiện có

### 1.4.1. Hệ thống quốc tế

**1. Epic Systems (Mỹ):**
- Hệ thống quản lý bệnh viện hàng đầu thế giới
- Phục vụ hơn 250 triệu bệnh nhân
- Tích hợp đầy đủ từ đặt lịch đến thanh toán
- Chi phí cao, phù hợp với bệnh viện lớn

**2. Cerner Corporation (Mỹ):**
- Giải pháp toàn diện cho cơ sở y tế
- Hỗ trợ AI và phân tích dữ liệu
- Giao diện thân thiện, dễ sử dụng
- Có phiên bản cho phòng khám nhỏ

**3. Allscripts (Mỹ):**
- Chuyên về Electronic Health Records (EHR)
- Tích hợp với nhiều thiết bị y tế
- Hỗ trợ telemedicine
- Giá cả phù hợp với phòng khám vừa và nhỏ

### 1.4.2. Hệ thống trong nước

**1. eHospital (FPT):**
- Hệ thống quản lý bệnh viện toàn diện
- Đã triển khai tại nhiều bệnh viện lớn
- Hỗ trợ tiếng Việt hoàn chỉnh
- Chi phí cao, phù hợp với bệnh viện

**2. MedPro (Viettel):**
- Giải pháp cho phòng khám và bệnh viện nhỏ
- Tích hợp thanh toán điện tử
- Hỗ trợ báo cáo bảo hiểm y tế
- Giá cả hợp lý

**3. ClinicPro (Startup Việt Nam):**
- Chuyên cho phòng khám tư nhân
- Giao diện đơn giản, dễ sử dụng
- Hỗ trợ đặt lịch online
- Còn hạn chế về tính năng

### 1.4.3. Phân tích so sánh

| Tiêu chí | Hệ thống quốc tế | Hệ thống trong nước | Hệ thống tự phát triển |
|----------|------------------|---------------------|------------------------|
| **Chi phí** | Cao (>$10,000/năm) | Trung bình ($2,000-5,000/năm) | Thấp (<$1,000) |
| **Tính năng** | Rất đầy đủ | Đầy đủ | Cơ bản |
| **Hỗ trợ tiếng Việt** | Hạn chế | Tốt | Hoàn hảo |
| **Tùy chỉnh** | Khó | Trung bình | Dễ |
| **Bảo trì** | Chuyên nghiệp | Tốt | Tự quản lý |
| **Phù hợp** | Bệnh viện lớn | Phòng khám vừa | Phòng khám nhỏ |

### 1.4.4. Kết luận chương 1

Qua phân tích tổng quan về tình hình quản lý phòng khám hiện tại, có thể thấy:

**1. Nhu cầu cấp thiết:**
- Phòng khám cần chuyển đổi từ quản lý thủ công sang số hóa
- Bệnh nhân ngày càng đòi hỏi dịch vụ tiện lợi, hiện đại
- Cạnh tranh thị trường đòi hỏi nâng cao chất lượng dịch vụ

**2. Cơ hội phát triển:**
- Hỗ trợ mạnh mẽ từ chính phủ về chuyển đổi số
- Công nghệ phát triển, chi phí giảm
- Thị trường có nhu cầu lớn chưa được đáp ứng đầy đủ

**3. Thách thức cần giải quyết:**
- Đảm bảo bảo mật thông tin y tế
- Tối ưu chi phí phát triển và vận hành
- Tạo giao diện thân thiện cho người dùng Việt Nam

**4. Định hướng giải pháp:**
- Phát triển hệ thống phù hợp với phòng khám nhỏ và vừa
- Tập trung vào các tính năng cốt lõi: đặt lịch, quản lý hồ sơ, thống kê
- Sử dụng công nghệ mã nguồn mở để giảm chi phí
- Thiết kế giao diện đơn giản, dễ sử dụng

Chương tiếp theo sẽ trình bày về cơ sở lý thuyết và công nghệ được sử dụng để xây dựng hệ thống.

---
# CHƯƠNG 2: CƠ SỞ LÝ THUYẾT VÀ CÔNG NGHỆ

## 2.1. Công nghệ web và Django Framework

### 2.1.1. Tổng quan về phát triển web

**Web Development Evolution:**
Phát triển ứng dụng web đã trải qua nhiều giai đoạn phát triển:

1. **Web 1.0 (1990-2000):** Trang web tĩnh, chỉ hiển thị thông tin
2. **Web 2.0 (2000-2010):** Tương tác người dùng, AJAX, social media
3. **Web 3.0 (2010-nay):** Responsive design, mobile-first, cloud computing
4. **Web 4.0 (tương lai):** AI integration, IoT, real-time collaboration

**Kiến trúc ứng dụng web hiện đại:**
- **Frontend:** Giao diện người dùng (HTML, CSS, JavaScript)
- **Backend:** Xử lý logic nghiệp vụ (Python, Java, PHP, Node.js)
- **Database:** Lưu trữ dữ liệu (MySQL, PostgreSQL, MongoDB)
- **Web Server:** Phục vụ ứng dụng (Apache, Nginx, IIS)

### 2.1.2. Giới thiệu Django Framework

**Django là gì?**
Django là một web framework mã nguồn mở được viết bằng Python, được phát triển bởi Adrian Holovaty và Simon Willison tại Lawrence Journal-World vào năm 2003. Django tuân theo nguyên tắc "Don't Repeat Yourself" (DRY) và "Convention over Configuration".

**Lịch sử phát triển:**
- **2003:** Bắt đầu phát triển tại Lawrence Journal-World
- **2005:** Phát hành mã nguồn mở
- **2008:** Django 1.0 - phiên bản ổn định đầu tiên
- **2019:** Django 3.0 - hỗ trợ Python 3.6+
- **2023:** Django 5.0 - phiên bản hiện tại với nhiều cải tiến

**Triết lý thiết kế:**
1. **Rapid Development:** Phát triển nhanh chóng
2. **DRY Principle:** Không lặp lại code
3. **Explicit is better than implicit:** Rõ ràng hơn ngầm hiểu
4. **Loosely coupled:** Các thành phần độc lập với nhau

### 2.1.3. Ưu điểm của Django

**1. Tốc độ phát triển cao:**
```python
# Tạo model chỉ với vài dòng code
class BenhNhan(models.Model):
    ten = models.CharField(max_length=100)
    email = models.EmailField()
    ngay_sinh = models.DateField()
    
    def __str__(self):
        return self.ten
```

**2. Bảo mật tích hợp sẵn:**
- CSRF protection
- SQL injection prevention
- XSS protection
- Clickjacking protection
- Secure password hashing

**3. Khả năng mở rộng:**
- Hỗ trợ caching (Redis, Memcached)
- Database optimization
- Load balancing
- Horizontal scaling

**4. Cộng đồng lớn:**
- Hơn 70,000 stars trên GitHub
- Tài liệu phong phú, chi tiết
- Nhiều package và plugin
- Hỗ trợ tích cực từ cộng đồng

**5. Batteries included:**
- Admin interface tự động
- ORM mạnh mẽ
- Authentication system
- Form handling
- Internationalization

### 2.1.4. Kiến trúc Django MTV

Django sử dụng kiến trúc MTV (Model-Template-View), một biến thể của MVC:

**Model (Mô hình):**
- Định nghĩa cấu trúc dữ liệu
- Tương tác với cơ sở dữ liệu
- Chứa business logic

```python
# models.py
class HoSoBenhNhan(models.Model):
    nguoi_dung = models.OneToOneField(User, on_delete=models.CASCADE)
    ngay_sinh = models.DateField()
    so_dien_thoai = models.CharField(max_length=15)
    
    def tuoi(self):
        return timezone.now().year - self.ngay_sinh.year
```

**Template (Giao diện):**
- Định nghĩa cách hiển thị dữ liệu
- Sử dụng Django Template Language
- Tách biệt logic và presentation

```html
<!-- template.html -->
<h1>Xin chào, {{ benh_nhan.nguoi_dung.first_name }}!</h1>
<p>Tuổi: {{ benh_nhan.tuoi }} tuổi</p>
<p>Số điện thoại: {{ benh_nhan.so_dien_thoai }}</p>
```

**View (Điều khiển):**
- Xử lý request từ người dùng
- Tương tác với Model
- Render Template

```python
# views.py
def ho_so_benh_nhan(request):
    benh_nhan = request.user.ho_so_benh_nhan
    context = {'benh_nhan': benh_nhan}
    return render(request, 'ho_so.html', context)
```

### 2.1.5. So sánh Django với các framework khác

| Framework | Ngôn ngữ | Ưu điểm | Nhược điểm | Phù hợp |
|-----------|----------|---------|------------|---------|
| **Django** | Python | Rapid development, bảo mật tốt, admin interface | Nặng, ít linh hoạt | Web app lớn, CMS |
| **Flask** | Python | Nhẹ, linh hoạt, dễ học | Ít tính năng built-in | API, microservices |
| **Laravel** | PHP | Elegant syntax, Eloquent ORM | Hiệu năng trung bình | Web app PHP |
| **Spring Boot** | Java | Enterprise-grade, scalable | Phức tạp, học khó | Enterprise app |
| **Express.js** | Node.js | Nhanh, real-time | Callback hell, single-threaded | Real-time app |

**Lý do chọn Django cho dự án:**
1. **Phù hợp với yêu cầu:** Hệ thống quản lý phòng khám cần nhiều tính năng CRUD
2. **Bảo mật:** Thông tin y tế cần bảo mật cao
3. **Admin interface:** Tiết kiệm thời gian phát triển
4. **Python ecosystem:** Dễ tích hợp với các thư viện khác
5. **Tài liệu tốt:** Dễ học và phát triển

## 2.2. Cơ sở dữ liệu và SQLite

### 2.2.1. Khái niệm cơ sở dữ liệu quan hệ

**Relational Database Management System (RDBMS):**
Hệ quản trị cơ sở dữ liệu quan hệ tổ chức dữ liệu thành các bảng (tables) có mối quan hệ với nhau. Mỗi bảng gồm:
- **Rows (Records):** Các bản ghi dữ liệu
- **Columns (Fields):** Các trường thông tin
- **Primary Key:** Khóa chính định danh duy nhất
- **Foreign Key:** Khóa ngoại tạo mối quan hệ

**Các loại quan hệ:**
1. **One-to-One (1:1):** Một bệnh nhân có một hồ sơ
2. **One-to-Many (1:N):** Một bác sĩ có nhiều lịch hẹn
3. **Many-to-Many (M:N):** Nhiều bệnh nhân có thể khám nhiều chuyên khoa

### 2.2.2. Giới thiệu SQLite

**SQLite là gì?**
SQLite là một hệ quản trị cơ sở dữ liệu quan hệ nhúng (embedded), không cần server riêng biệt. Dữ liệu được lưu trong một file duy nhất trên đĩa cứng.

**Đặc điểm của SQLite:**
- **Serverless:** Không cần cài đặt server
- **Zero-configuration:** Không cần cấu hình
- **Cross-platform:** Chạy trên mọi hệ điều hành
- **Compact:** Thư viện nhỏ gọn (~600KB)
- **Reliable:** Đã được kiểm thử kỹ lưỡng

**Ưu điểm:**
1. **Dễ triển khai:** Chỉ cần copy file database
2. **Hiệu năng tốt:** Nhanh với ứng dụng nhỏ và vừa
3. **ACID compliant:** Đảm bảo tính toàn vẹn dữ liệu
4. **Không cần bảo trì:** Tự động tối ưu hóa
5. **Miễn phí:** Public domain license

**Nhược điểm:**
1. **Hạn chế concurrent writes:** Chỉ một process ghi tại một thời điểm
2. **Không có user management:** Không phân quyền người dùng
3. **Giới hạn kích thước:** Tối đa 281TB (thực tế đủ dùng)
4. **Không phù hợp với ứng dụng lớn:** Cần database server cho high-traffic

### 2.2.3. Django ORM (Object-Relational Mapping)

**ORM là gì?**
ORM là kỹ thuật ánh xạ giữa đối tượng trong lập trình hướng đối tượng và bảng trong cơ sở dữ liệu quan hệ.

**Ưu điểm của Django ORM:**
1. **Database agnostic:** Có thể chuyển đổi database dễ dàng
2. **SQL injection prevention:** Tự động escape SQL
3. **Pythonic syntax:** Viết code Python thay vì SQL
4. **Lazy evaluation:** Chỉ thực hiện query khi cần thiết
5. **Caching:** Tự động cache kết quả

**Ví dụ Django ORM:**
```python
# Thay vì viết SQL:
# SELECT * FROM accounts_hosobenhnhan WHERE ngay_sinh > '1990-01-01'

# Django ORM:
benh_nhan_tre = HoSoBenhNhan.objects.filter(
    ngay_sinh__gt=date(1990, 1, 1)
)

# Join tables:
lich_hen = LichHen.objects.select_related('benh_nhan', 'bac_si').filter(
    ngay=timezone.now().date()
)
```

**Migrations:**
Django tự động tạo và quản lý schema database:
```bash
python manage.py makemigrations  # Tạo migration files
python manage.py migrate         # Áp dụng vào database
```

### 2.2.4. Thiết kế cơ sở dữ liệu cho hệ thống

**Nguyên tắc thiết kế:**
1. **Normalization:** Tránh dư thừa dữ liệu
2. **Referential Integrity:** Đảm bảo tính toàn vẹn tham chiếu
3. **Indexing:** Tối ưu hóa truy vấn
4. **Naming Convention:** Đặt tên nhất quán

**Cấu trúc bảng chính:**
```python
# User (Django built-in)
- id, username, password, email, first_name, last_name, is_staff, is_active

# HoSoBenhNhan
- id, nguoi_dung_id (FK), ngay_sinh, gioi_tinh, so_dien_thoai, dia_chi

# HoSoBacSi  
- id, nguoi_dung_id (FK), chuyen_khoa_id (FK), bang_cap, phi_kham

# LichHen
- id, benh_nhan_id (FK), bac_si_id (FK), ngay, gio, trang_thai

# HoSoBenhAn
- id, lich_hen_id (FK), chan_doan, toa_thuoc, ghi_chu
```

## 2.3. HTML, CSS, JavaScript

### 2.3.1. HTML5 - Cấu trúc nội dung

**HTML5 Features:**
HTML5 mang lại nhiều cải tiến so với phiên bản trước:
- **Semantic elements:** `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`
- **Form enhancements:** Input types mới, validation
- **Multimedia:** `<video>`, `<audio>` native support
- **Canvas:** Vẽ graphics động
- **Local Storage:** Lưu trữ dữ liệu client-side

**Semantic HTML trong dự án:**
```html
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Phòng khám ABC</title>
</head>
<body>
    <header>
        <nav class="navbar">
            <div class="nav-brand">Phòng khám ABC</div>
            <ul class="nav-menu">
                <li><a href="/">Trang chủ</a></li>
                <li><a href="/bac-si/">Bác sĩ</a></li>
                <li><a href="/lich-hen/">Lịch hẹn</a></li>
            </ul>
        </nav>
    </header>
    
    <main>
        <section class="hero">
            <h1>Chào mừng đến với Phòng khám ABC</h1>
            <p>Dịch vụ y tế chất lượng cao</p>
        </section>
    </main>
    
    <footer>
        <p>&copy; 2024 Phòng khám ABC. All rights reserved.</p>
    </footer>
</body>
</html>
```

### 2.3.2. CSS3 - Styling và Layout

**CSS3 Advanced Features:**
- **Flexbox:** Layout linh hoạt
- **Grid:** Layout 2D mạnh mẽ
- **Animations:** Hiệu ứng chuyển động
- **Media Queries:** Responsive design
- **Custom Properties:** CSS variables

**Responsive Design:**
```css
/* Mobile First Approach */
.container {
    width: 100%;
    padding: 0 15px;
}

/* Tablet */
@media (min-width: 768px) {
    .container {
        max-width: 750px;
        margin: 0 auto;
    }
}

/* Desktop */
@media (min-width: 1200px) {
    .container {
        max-width: 1170px;
    }
}

/* CSS Grid for Dashboard */
.dashboard {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 20px;
    padding: 20px;
}

.card {
    background: white;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    padding: 20px;
    transition: transform 0.3s ease;
}

.card:hover {
    transform: translateY(-5px);
}
```

### 2.3.3. JavaScript - Tương tác động

**Modern JavaScript (ES6+):**
- **Arrow Functions:** Syntax ngắn gọn
- **Template Literals:** String interpolation
- **Destructuring:** Trích xuất dữ liệu
- **Async/Await:** Xử lý bất đồng bộ
- **Modules:** Tổ chức code

**JavaScript trong dự án:**
```javascript
// Form validation
class FormValidator {
    constructor(form) {
        this.form = form;
        this.errors = {};
    }
    
    validateRequired(field) {
        if (!field.value.trim()) {
            this.addError(field.name, 'Trường này là bắt buộc');
            return false;
        }
        return true;
    }
    
    validateEmail(field) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(field.value)) {
            this.addError(field.name, 'Email không hợp lệ');
            return false;
        }
        return true;
    }
    
    validatePhone(field) {
        const phoneRegex = /^[0-9]{10,11}$/;
        if (!phoneRegex.test(field.value)) {
            this.addError(field.name, 'Số điện thoại không hợp lệ');
            return false;
        }
        return true;
    }
}

// AJAX for dynamic content
async function loadDoctorSchedule(doctorId) {
    try {
        const response = await fetch(`/api/doctor/${doctorId}/schedule/`);
        const data = await response.json();
        
        if (data.success) {
            renderSchedule(data.schedule);
        } else {
            showError(data.message);
        }
    } catch (error) {
        showError('Có lỗi xảy ra khi tải lịch làm việc');
    }
}

// DOM manipulation
function renderSchedule(schedule) {
    const container = document.getElementById('schedule-container');
    container.innerHTML = '';
    
    schedule.forEach(slot => {
        const slotElement = document.createElement('div');
        slotElement.className = `time-slot ${slot.available ? 'available' : 'booked'}`;
        slotElement.innerHTML = `
            <span class="time">${slot.time}</span>
            <span class="status">${slot.available ? 'Còn trống' : 'Đã đặt'}</span>
        `;
        
        if (slot.available) {
            slotElement.addEventListener('click', () => bookAppointment(slot.id));
        }
        
        container.appendChild(slotElement);
    });
}
```

### 2.3.4. Bootstrap Framework

**Tại sao chọn Bootstrap?**
1. **Rapid prototyping:** Phát triển nhanh giao diện
2. **Responsive grid:** Hệ thống lưới linh hoạt
3. **Pre-built components:** Nhiều component có sẵn
4. **Cross-browser compatibility:** Tương thích đa trình duyệt
5. **Large community:** Cộng đồng lớn, nhiều tài liệu

**Bootstrap Components sử dụng:**
```html
<!-- Navigation -->
<nav class="navbar navbar-expand-lg navbar-dark bg-primary">
    <div class="container">
        <a class="navbar-brand" href="/">Phòng khám ABC</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse">
            <span class="navbar-toggler-icon"></span>
        </button>
    </div>
</nav>

<!-- Cards -->
<div class="row">
    <div class="col-md-4">
        <div class="card">
            <div class="card-body">
                <h5 class="card-title">Tổng bệnh nhân</h5>
                <p class="card-text display-4">{{ total_patients }}</p>
            </div>
        </div>
    </div>
</div>

<!-- Forms -->
<form class="needs-validation" novalidate>
    <div class="mb-3">
        <label for="email" class="form-label">Email</label>
        <input type="email" class="form-control" id="email" required>
        <div class="invalid-feedback">
            Vui lòng nhập email hợp lệ.
        </div>
    </div>
    <button type="submit" class="btn btn-primary">Đăng ký</button>
</form>
```

## 2.4. Bảo mật trong ứng dụng web

### 2.4.1. Các mối đe dọa bảo mật phổ biến

**OWASP Top 10 (2021):**
1. **Broken Access Control:** Kiểm soát truy cập kém
2. **Cryptographic Failures:** Lỗi mã hóa
3. **Injection:** SQL injection, XSS
4. **Insecure Design:** Thiết kế không an toàn
5. **Security Misconfiguration:** Cấu hình sai
6. **Vulnerable Components:** Thành phần có lỗ hổng
7. **Authentication Failures:** Lỗi xác thực
8. **Software Integrity Failures:** Lỗi toàn vẹn phần mềm
9. **Logging Failures:** Ghi log kém
10. **Server-Side Request Forgery:** SSRF

### 2.4.2. Bảo mật trong Django

**1. CSRF Protection:**
```python
# settings.py
MIDDLEWARE = [
    'django.middleware.csrf.CsrfViewMiddleware',
]

# template
<form method="post">
    {% csrf_token %}
    <!-- form fields -->
</form>
```

**2. SQL Injection Prevention:**
```python
# WRONG - vulnerable to SQL injection
User.objects.extra(where=["username = '%s'" % username])

# CORRECT - parameterized query
User.objects.filter(username=username)
```

**3. XSS Protection:**
```html
<!-- Django auto-escapes by default -->
<p>{{ user_input }}</p>  <!-- Safe -->

<!-- Manual escaping when needed -->
<p>{{ user_input|escape }}</p>

<!-- Mark as safe only when certain -->
<p>{{ trusted_html|safe }}</p>
```

**4. Authentication & Authorization:**
```python
from django.contrib.auth.decorators import login_required, user_passes_test

@login_required
def protected_view(request):
    return render(request, 'protected.html')

def is_doctor(user):
    return hasattr(user, 'ho_so_bac_si')

@user_passes_test(is_doctor)
def doctor_only_view(request):
    return render(request, 'doctor_dashboard.html')
```

### 2.4.3. Bảo mật thông tin y tế

**HIPAA Compliance (tham khảo):**
Mặc dù HIPAA là quy định của Mỹ, nhưng các nguyên tắc có thể áp dụng:

1. **Access Control:** Chỉ người có quyền mới truy cập được
2. **Audit Logs:** Ghi lại mọi truy cập dữ liệu
3. **Data Encryption:** Mã hóa dữ liệu nhạy cảm
4. **Minimum Necessary:** Chỉ truy cập dữ liệu cần thiết
5. **User Training:** Đào tạo nhân viên về bảo mật

**Triển khai trong dự án:**
```python
# models.py - Audit log
class AuditLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=100)
    model_name = models.CharField(max_length=100)
    object_id = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField()

# middleware.py - Log all access
class AuditMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            AuditLog.objects.create(
                user=request.user,
                action=request.method,
                model_name='Page Access',
                object_id=0,
                ip_address=self.get_client_ip(request)
            )
        
        response = self.get_response(request)
        return response
```

### 2.4.4. HTTPS và SSL/TLS

**Tầm quan trọng của HTTPS:**
- Mã hóa dữ liệu truyền tải
- Xác thực danh tính server
- Đảm bảo tính toàn vẹn dữ liệu
- Cải thiện SEO ranking
- Yêu cầu bắt buộc cho PWA

**Cấu hình HTTPS trong Django:**
```python
# settings.py for production
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
```

### 2.4.5. Kết luận chương 2

Chương này đã trình bày các công nghệ cốt lõi được sử dụng trong dự án:

**1. Django Framework:**
- Lựa chọn phù hợp cho hệ thống quản lý phòng khám
- Cung cấp nhiều tính năng bảo mật tích hợp sẵn
- Hỗ trợ phát triển nhanh với admin interface và ORM

**2. SQLite Database:**
- Phù hợp với quy mô phòng khám nhỏ và vừa
- Dễ triển khai và bảo trì
- Đảm bảo tính toàn vẹn dữ liệu với ACID

**3. Frontend Technologies:**
- HTML5 semantic cho cấu trúc rõ ràng
- CSS3 và Bootstrap cho giao diện responsive
- JavaScript cho tương tác động và UX tốt

**4. Security Measures:**
- Áp dụng các best practices về bảo mật web
- Đặc biệt chú trọng bảo vệ thông tin y tế
- Triển khai logging và audit trail

Chương tiếp theo sẽ trình bày quá trình phân tích yêu cầu và thiết kế hệ thống dựa trên nền tảng công nghệ này.

---
# CHƯƠNG 3: PHÂN TÍCH VÀ THIẾT KẾ HỆ THỐNG

## 3.1. Phân tích yêu cầu

### 3.1.1. Yêu cầu chức năng

**Bảng 3.1: Phân tích yêu cầu chức năng**

| STT | Chức năng | Mô tả | Đối tượng | Độ ưu tiên |
|-----|-----------|-------|-----------|------------|
| **1** | **Quản lý người dùng** | | | |
| 1.1 | Đăng ký bệnh nhân | Bệnh nhân tự đăng ký tài khoản | Bệnh nhân | Cao |
| 1.2 | Đăng nhập/Đăng xuất | Xác thực người dùng | Tất cả | Cao |
| 1.3 | Quản lý hồ sơ cá nhân | Xem/chỉnh sửa thông tin cá nhân | Tất cả | Cao |
| 1.4 | Quản lý bác sĩ | Thêm/xóa/tạm ngưng bác sĩ | Admin | Cao |
| **2** | **Quản lý lịch hẹn** | | | |
| 2.1 | Xem danh sách bác sĩ | Hiển thị bác sĩ theo chuyên khoa | Bệnh nhân | Cao |
| 2.2 | Xem lịch làm việc | Hiển thị lịch trống của bác sĩ | Bệnh nhân | Cao |
| 2.3 | Đặt lịch khám | Đặt lịch hẹn với bác sĩ | Bệnh nhân | Cao |
| 2.4 | Xác nhận lịch hẹn | Bác sĩ xác nhận lịch đã đặt | Bác sĩ | Cao |
| 2.5 | Hủy lịch hẹn | Hủy lịch hẹn đã đặt | Bệnh nhân, Bác sĩ | Trung bình |
| 2.6 | Xem lịch hẹn cá nhân | Xem lịch hẹn của mình | Bệnh nhân, Bác sĩ | Cao |
| **3** | **Quản lý hồ sơ bệnh án** | | | |
| 3.1 | Tạo hồ sơ bệnh án | Ghi chép sau khi khám | Bác sĩ | Cao |
| 3.2 | Xem hồ sơ bệnh án | Xem chi tiết hồ sơ | Bệnh nhân, Bác sĩ | Cao |
| 3.3 | Lịch sử khám bệnh | Xem danh sách hồ sơ đã khám | Bệnh nhân, Bác sĩ | Cao |
| **4** | **Dashboard và báo cáo** | | | |
| 4.1 | Dashboard bệnh nhân | Tổng quan lịch hẹn, hồ sơ | Bệnh nhân | Trung bình |
| 4.2 | Dashboard bác sĩ | Thống kê lịch hẹn, bệnh nhân | Bác sĩ | Trung bình |
| 4.3 | Dashboard admin | Thống kê tổng thể hệ thống | Admin | Trung bình |
| **5** | **Bảo mật và phân quyền** | | | |
| 5.1 | Phân quyền truy cập | Kiểm soát quyền theo vai trò | Hệ thống | Cao |
| 5.2 | Bảo mật thông tin | Mã hóa dữ liệu nhạy cảm | Hệ thống | Cao |
| 5.3 | Audit log | Ghi lại hoạt động người dùng | Hệ thống | Thấp |

### 3.1.2. Yêu cầu phi chức năng

**Bảng 3.2: Phân tích yêu cầu phi chức năng**

| STT | Yêu cầu | Mô tả | Chỉ số mục tiêu |
|-----|---------|-------|-----------------|
| **1** | **Hiệu năng (Performance)** | | |
| 1.1 | Thời gian phản hồi | Thời gian tải trang | < 3 giây |
| 1.2 | Throughput | Số request xử lý đồng thời | 100 users |
| 1.3 | Thời gian khởi động | Thời gian start server | < 30 giây |
| **2** | **Khả năng sử dụng (Usability)** | | |
| 2.1 | Giao diện thân thiện | Dễ sử dụng cho mọi đối tượng | 90% user hài lòng |
| 2.2 | Responsive design | Tương thích đa thiết bị | Mobile, Tablet, Desktop |
| 2.3 | Hỗ trợ tiếng Việt | Giao diện và nội dung tiếng Việt | 100% |
| **3** | **Độ tin cậy (Reliability)** | | |
| 3.1 | Uptime | Thời gian hoạt động | 99% |
| 3.2 | Error handling | Xử lý lỗi graceful | Không crash |
| 3.3 | Data integrity | Tính toàn vẹn dữ liệu | 100% |
| **4** | **Bảo mật (Security)** | | |
| 4.1 | Authentication | Xác thực người dùng | Strong password |
| 4.2 | Authorization | Phân quyền truy cập | Role-based |
| 4.3 | Data encryption | Mã hóa dữ liệu nhạy cảm | HTTPS, Hash password |
| **5** | **Khả năng mở rộng (Scalability)** | | |
| 5.1 | Horizontal scaling | Mở rộng theo chiều ngang | Hỗ trợ load balancer |
| 5.2 | Database scaling | Mở rộng cơ sở dữ liệu | Migration to PostgreSQL |
| 5.3 | Code maintainability | Dễ bảo trì và phát triển | Clean code, documentation |

### 3.1.3. Use Case Diagram

**Hình 3.1: Use Case Diagram tổng thể**

```
                    Hệ thống Quản lý Phòng khám
    
    Bệnh nhân                           Bác sĩ                          Admin
        |                                |                               |
        |-- Đăng ký tài khoản            |-- Đăng nhập                   |-- Quản lý bác sĩ
        |-- Đăng nhập                    |-- Quản lý hồ sơ cá nhân       |-- Xem thống kê
        |-- Quản lý hồ sơ cá nhân        |-- Xem lịch hẹn               |-- Quản lý hệ thống
        |-- Xem danh sách bác sĩ         |-- Xác nhận lịch hẹn          |-- Phân quyền
        |-- Xem lịch làm việc bác sĩ     |-- Tạo hồ sơ bệnh án          |
        |-- Đặt lịch khám               |-- Xem hồ sơ bệnh án          |
        |-- Xem lịch hẹn của mình        |-- Lịch sử khám bệnh          |
        |-- Hủy lịch hẹn                |-- Dashboard bác sĩ           |
        |-- Xem hồ sơ bệnh án           |                               |
        |-- Lịch sử khám bệnh           |                               |
        |-- Dashboard bệnh nhân         |                               |
```

**Chi tiết Use Case chính:**

**UC01: Đặt lịch khám**
- **Actor:** Bệnh nhân
- **Precondition:** Bệnh nhân đã đăng nhập
- **Main Flow:**
  1. Bệnh nhân chọn "Danh sách bác sĩ"
  2. Hệ thống hiển thị danh sách bác sĩ hoạt động
  3. Bệnh nhân chọn bác sĩ
  4. Hệ thống hiển thị lịch làm việc của bác sĩ
  5. Bệnh nhân chọn khung giờ trống
  6. Bệnh nhân nhập triệu chứng và xác nhận
  7. Hệ thống tạo lịch hẹn với trạng thái "Chờ xác nhận"
  8. Hệ thống gửi thông báo thành công
- **Alternative Flow:**
  - 4a. Không có lịch trống: Hiển thị thông báo
  - 6a. Thông tin không hợp lệ: Hiển thị lỗi validation
- **Postcondition:** Lịch hẹn được tạo trong hệ thống

**UC02: Xác nhận lịch hẹn**
- **Actor:** Bác sĩ
- **Precondition:** Bác sĩ đã đăng nhập, có lịch hẹn chờ xác nhận
- **Main Flow:**
  1. Bác sĩ truy cập "Lịch hẹn của tôi"
  2. Hệ thống hiển thị danh sách lịch hẹn
  3. Bác sĩ chọn lịch hẹn cần xác nhận
  4. Bác sĩ nhấn "Xác nhận"
  5. Hệ thống cập nhật trạng thái thành "Đã xác nhận"
  6. Hệ thống gửi thông báo cho bệnh nhân
- **Alternative Flow:**
  - 4a. Bác sĩ hủy lịch hẹn: Cập nhật trạng thái "Đã hủy"
- **Postcondition:** Lịch hẹn được xác nhận

### 3.1.4. Phân tích Actor

**1. Bệnh nhân (Patient):**
- **Đặc điểm:** Người cần dịch vụ y tế, có thể không am hiểu công nghệ
- **Mục tiêu:** Đặt lịch khám thuận tiện, theo dõi sức khỏe
- **Nhu cầu:**
  - Giao diện đơn giản, dễ sử dụng
  - Thông tin bác sĩ chi tiết, đáng tin cậy
  - Đặt lịch nhanh chóng, linh hoạt
  - Theo dõi lịch sử khám bệnh

**2. Bác sĩ (Doctor):**
- **Đặc điểm:** Chuyên gia y tế, bận rộn, cần hiệu quả
- **Mục tiêu:** Quản lý lịch hẹn hiệu quả, ghi chép bệnh án nhanh
- **Nhu cầu:**
  - Dashboard tổng quan rõ ràng
  - Tạo hồ sơ bệnh án nhanh chóng
  - Quản lý lịch làm việc linh hoạt
  - Truy cập thông tin bệnh nhân dễ dàng

**3. Quản trị viên (Admin):**
- **Đặc điểm:** Nhân viên IT hoặc quản lý phòng khám
- **Mục tiêu:** Quản lý hệ thống, theo dõi hoạt động
- **Nhu cầu:**
  - Công cụ quản lý bác sĩ mạnh mẽ
  - Báo cáo thống kê chi tiết
  - Kiểm soát quyền truy cập
  - Giám sát hoạt động hệ thống

## 3.2. Thiết kế cơ sở dữ liệu

### 3.2.1. Sơ đồ ERD (Entity Relationship Diagram)

**Hình 3.2: Sơ đồ ERD của hệ thống**

```
    User (Django built-in)
    ┌─────────────────────┐
    │ id (PK)            │
    │ username           │
    │ password           │
    │ email              │
    │ first_name         │
    │ last_name          │
    │ is_staff           │
    │ is_active          │
    │ date_joined        │
    └─────────────────────┘
            │
            │ 1:1
            ▼
    ┌─────────────────────┐         ┌─────────────────────┐
    │   HoSoBenhNhan     │         │    HoSoBacSi       │
    │ ─────────────────── │         │ ─────────────────── │
    │ id (PK)            │         │ id (PK)            │
    │ nguoi_dung_id (FK) │         │ nguoi_dung_id (FK) │
    │ ngay_sinh          │         │ chuyen_khoa_id (FK)│
    │ gioi_tinh          │         │ mo_ta              │
    │ so_dien_thoai      │         │ bang_cap           │
    │ dia_chi            │         │ so_dien_thoai      │
    │ anh_dai_dien       │         │ phi_kham           │
    └─────────────────────┘         │ anh_dai_dien       │
            │                       └─────────────────────┘
            │ 1:N                           │
            │                               │ N:1
            ▼                               ▼
    ┌─────────────────────┐         ┌─────────────────────┐
    │      LichHen       │         │    ChuyenKhoa      │
    │ ─────────────────── │         │ ─────────────────── │
    │ id (PK)            │         │ id (PK)            │
    │ benh_nhan_id (FK)  │         │ ten                │
    │ bac_si_id (FK)     │         │ mo_ta              │
    │ lich_lam_viec_id   │         └─────────────────────┘
    │ ngay               │
    │ gio                │                 ▲
    │ trang_thai         │                 │ N:1
    │ trieu_chung        │                 │
    │ ngay_tao           │         ┌─────────────────────┐
    │ ngay_cap_nhat      │         │   LichLamViec      │
    └─────────────────────┘         │ ─────────────────── │
            │                       │ id (PK)            │
            │ 1:1                   │ bac_si_id (FK)     │
            ▼                       │ ngay               │
    ┌─────────────────────┐         │ gio_bat_dau        │
    │   HoSoBenhAn       │         │ gio_ket_thuc       │
    │ ─────────────────── │         │ con_trong          │
    │ id (PK)            │         └─────────────────────┘
    │ lich_hen_id (FK)   │
    │ chan_doan          │
    │ ghi_chu            │         ┌─────────────────────┐
    │ ngay_tao           │         │      Thuoc         │
    │ ngay_cap_nhat      │         │ ─────────────────── │
    └─────────────────────┘         │ id (PK)            │
            │                       │ ten_thuoc          │
            │ 1:N                   │ don_vi             │
            ▼                       └─────────────────────┘
    ┌─────────────────────┐                 ▲
    │     ToaThuoc       │                 │ N:1
    │ ─────────────────── │                 │
    │ id (PK)            │─────────────────┘
    │ ho_so_benh_an_id   │
    │ thuoc_id (FK)      │
    │ so_luong           │
    │ ghi_chu            │
    └─────────────────────┘
```

### 3.2.2. Mô tả các bảng

**Bảng 3.3: Mô tả các bảng trong cơ sở dữ liệu**

| Tên bảng | Mô tả | Khóa chính | Khóa ngoại |
|----------|-------|------------|------------|
| **User** | Thông tin đăng nhập (Django built-in) | id | - |
| **ChuyenKhoa** | Danh mục chuyên khoa y tế | id | - |
| **HoSoBenhNhan** | Hồ sơ chi tiết bệnh nhân | id | nguoi_dung_id → User.id |
| **HoSoBacSi** | Hồ sơ chi tiết bác sĩ | id | nguoi_dung_id → User.id<br>chuyen_khoa_id → ChuyenKhoa.id |
| **LichLamViec** | Lịch làm việc của bác sĩ | id | bac_si_id → HoSoBacSi.id |
| **LichHen** | Lịch hẹn khám bệnh | id | benh_nhan_id → HoSoBenhNhan.id<br>bac_si_id → HoSoBacSi.id<br>lich_lam_viec_id → LichLamViec.id |
| **HoSoBenhAn** | Hồ sơ bệnh án sau khám | id | lich_hen_id → LichHen.id |
| **Thuoc** | Danh mục thuốc | id | - |
| **ToaThuoc** | Chi tiết toa thuốc | id | ho_so_benh_an_id → HoSoBenhAn.id<br>thuoc_id → Thuoc.id |

### 3.2.3. Ràng buộc toàn vẹn

**1. Ràng buộc thực thể (Entity Constraints):**
- Mỗi User phải có username duy nhất
- Email phải có định dạng hợp lệ
- Số điện thoại phải có 10-11 chữ số
- Ngày sinh phải nhỏ hơn ngày hiện tại

**2. Ràng buộc tham chiếu (Referential Constraints):**
- HoSoBenhNhan.nguoi_dung_id phải tồn tại trong User.id
- HoSoBacSi.chuyen_khoa_id phải tồn tại trong ChuyenKhoa.id
- LichHen.benh_nhan_id phải tồn tại trong HoSoBenhNhan.id
- HoSoBenhAn.lich_hen_id phải tồn tại trong LichHen.id

**3. Ràng buộc nghiệp vụ (Business Rules):**
- Một User chỉ có thể là bệnh nhân HOẶC bác sĩ, không thể là cả hai
- Lịch hẹn chỉ có thể đặt trong tương lai
- Bác sĩ chỉ có thể xác nhận lịch hẹn của mình
- Hồ sơ bệnh án chỉ được tạo sau khi lịch hẹn hoàn thành

**4. Ràng buộc trạng thái:**
```python
# LichHen.trang_thai
TRANG_THAI_CHOICES = [
    ('pending', 'Chờ xác nhận'),
    ('approved', 'Đã xác nhận'),
    ('canceled', 'Đã hủy'),
    ('completed', 'Hoàn thành'),
]

# Quy tắc chuyển trạng thái:
# pending → approved (bác sĩ xác nhận)
# pending → canceled (bệnh nhân/bác sĩ hủy)
# approved → completed (sau khi khám)
# approved → canceled (hủy lịch đã xác nhận)
```

### 3.2.4. Indexing Strategy

**Các index cần thiết:**
```sql
-- Index cho tìm kiếm thường xuyên
CREATE INDEX idx_lichhen_ngay ON appointments_lichhen(ngay);
CREATE INDEX idx_lichhen_trangthai ON appointments_lichhen(trang_thai);
CREATE INDEX idx_lichhen_bacsi ON appointments_lichhen(bac_si_id);
CREATE INDEX idx_lichhen_benhnhan ON appointments_lichhen(benh_nhan_id);

-- Composite index cho query phức tạp
CREATE INDEX idx_lichhen_bacsi_ngay ON appointments_lichhen(bac_si_id, ngay);
CREATE INDEX idx_lichlamviec_bacsi_ngay ON appointments_lichlamviec(bac_si_id, ngay);

-- Index cho foreign keys
CREATE INDEX idx_hosobenhan_nguoidung ON accounts_hosobenhnhan(nguoi_dung_id);
CREATE INDEX idx_hosobacsi_nguoidung ON accounts_hosobacsi(nguoi_dung_id);
```

## 3.3. Thiết kế giao diện

### 3.3.1. Nguyên tắc thiết kế UI/UX

**1. User-Centered Design:**
- Đặt người dùng làm trung tâm
- Hiểu rõ nhu cầu và hành vi người dùng
- Thiết kế dựa trên user journey

**2. Accessibility (Khả năng tiếp cận):**
- Hỗ trợ người khuyết tật
- Contrast ratio đạt chuẩn WCAG
- Keyboard navigation
- Screen reader friendly

**3. Mobile-First Design:**
- Thiết kế cho mobile trước
- Progressive enhancement
- Touch-friendly interface

**4. Consistency (Tính nhất quán):**
- Màu sắc, font chữ thống nhất
- Layout pattern giống nhau
- Terminology nhất quán

### 3.3.2. Color Scheme và Typography

**Color Palette:**
```css
:root {
    /* Primary Colors - Medical Theme */
    --primary-color: #2c5aa0;      /* Professional Blue */
    --primary-light: #4a7bc8;     /* Light Blue */
    --primary-dark: #1e3d6f;      /* Dark Blue */
    
    /* Secondary Colors */
    --secondary-color: #28a745;    /* Success Green */
    --warning-color: #ffc107;      /* Warning Yellow */
    --danger-color: #dc3545;       /* Error Red */
    --info-color: #17a2b8;         /* Info Cyan */
    
    /* Neutral Colors */
    --white: #ffffff;
    --light-gray: #f8f9fa;
    --gray: #6c757d;
    --dark-gray: #343a40;
    --black: #000000;
    
    /* Background Colors */
    --bg-primary: #f4f6f9;
    --bg-card: #ffffff;
    --bg-hover: #e9ecef;
}
```

**Typography:**
```css
/* Font Stack */
body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    font-size: 16px;
    line-height: 1.5;
    color: var(--dark-gray);
}

/* Headings */
h1 { font-size: 2.5rem; font-weight: 700; }
h2 { font-size: 2rem; font-weight: 600; }
h3 { font-size: 1.75rem; font-weight: 600; }
h4 { font-size: 1.5rem; font-weight: 500; }
h5 { font-size: 1.25rem; font-weight: 500; }
h6 { font-size: 1rem; font-weight: 500; }

/* Body Text */
.lead { font-size: 1.25rem; font-weight: 300; }
.small { font-size: 0.875rem; }
.text-muted { color: var(--gray); }
```

### 3.3.3. Wireframes chính

**Hình 3.3: Wireframe giao diện chính**

**1. Trang đăng nhập:**
```
┌─────────────────────────────────────────┐
│              HEADER                     │
│  [Logo] Phòng khám ABC                  │
└─────────────────────────────────────────┘
│                                         │
│         ĐĂNG NHẬP HỆ THỐNG             │
│                                         │
│  ┌─────────────────────────────────┐    │
│  │ Username: [________________]    │    │
│  │ Password: [________________]    │    │
│  │                                 │    │
│  │ [x] Ghi nhớ đăng nhập          │    │
│  │                                 │    │
│  │     [ĐĂNG NHẬP]                │    │
│  │                                 │    │
│  │ Chưa có tài khoản?             │    │
│  │ [Đăng ký bệnh nhân]            │    │
│  └─────────────────────────────────┘    │
│                                         │
└─────────────────────────────────────────┘
```

**2. Dashboard bệnh nhân:**
```
┌─────────────────────────────────────────┐
│ [Logo] | Trang chủ | Bác sĩ | Lịch hẹn  │ [User] ▼
└─────────────────────────────────────────┘
│                                         │
│  Xin chào, [Tên bệnh nhân]             │
│                                         │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐   │
│  │ Lịch hẹn│ │Tổng lịch│ │ Đã khám │   │
│  │ sắp tới │ │  hẹn    │ │         │   │
│  │   [3]   │ │  [15]   │ │  [12]   │   │
│  └─────────┘ └─────────┘ └─────────┘   │
│                                         │
│  LỊCH HẸN SẮP TỚI                      │
│  ┌─────────────────────────────────┐   │
│  │ 25/12 - 09:00 | BS. Nguyễn A   │   │
│  │ Nội khoa      | Đã xác nhận     │   │
│  └─────────────────────────────────┘   │
│                                         │
│  [ĐẶT LỊCH KHÁM MỚI]                   │
│                                         │
└─────────────────────────────────────────┘
```

**3. Danh sách bác sĩ:**
```
┌─────────────────────────────────────────┐
│              NAVIGATION                 │
└─────────────────────────────────────────┘
│                                         │
│  DANH SÁCH BÁC SĨ                      │
│                                         │
│  Lọc theo chuyên khoa: [Tất cả ▼]      │
│                                         │
│  ┌─────────────────────────────────┐   │
│  │ [Ảnh] BS. Nguyễn Văn A         │   │
│  │       Nội khoa                  │   │
│  │       ⭐⭐⭐⭐⭐ (4.8/5)          │   │
│  │       Phí khám: 200,000đ        │   │
│  │       [XEM LỊCH]               │   │
│  └─────────────────────────────────┘   │
│                                         │
│  ┌─────────────────────────────────┐   │
│  │ [Ảnh] BS. Trần Thị B           │   │
│  │       Nhi khoa                  │   │
│  │       ⭐⭐⭐⭐⭐ (4.9/5)          │   │
│  │       Phí khám: 250,000đ        │   │
│  │       [XEM LỊCH]               │   │
│  └─────────────────────────────────┘   │
│                                         │
└─────────────────────────────────────────┘
```

### 3.3.4. Responsive Design

**Breakpoints:**
```css
/* Mobile First */
/* Extra small devices (phones, 576px and down) */
@media (max-width: 575.98px) {
    .container { padding: 0 10px; }
    .card { margin-bottom: 15px; }
    .btn { width: 100%; margin-bottom: 10px; }
}

/* Small devices (landscape phones, 576px and up) */
@media (min-width: 576px) {
    .container { max-width: 540px; }
}

/* Medium devices (tablets, 768px and up) */
@media (min-width: 768px) {
    .container { max-width: 720px; }
    .dashboard-grid { 
        display: grid; 
        grid-template-columns: repeat(2, 1fr); 
        gap: 20px; 
    }
}

/* Large devices (desktops, 992px and up) */
@media (min-width: 992px) {
    .container { max-width: 960px; }
    .dashboard-grid { 
        grid-template-columns: repeat(3, 1fr); 
    }
}

/* Extra large devices (large desktops, 1200px and up) */
@media (min-width: 1200px) {
    .container { max-width: 1140px; }
    .dashboard-grid { 
        grid-template-columns: repeat(4, 1fr); 
    }
}
```

## 3.4. Kiến trúc hệ thống

### 3.4.1. Kiến trúc tổng thể

**Hình 3.4: Kiến trúc tổng thể hệ thống**

```
┌─────────────────────────────────────────────────────────┐
│                    PRESENTATION LAYER                   │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐     │
│  │   Web UI    │  │  Mobile UI  │  │   Admin UI  │     │
│  │  (Browser)  │  │ (Responsive)│  │  (Django)   │     │
│  └─────────────┘  └─────────────┘  └─────────────┘     │
└─────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────┐
│                   APPLICATION LAYER                     │
│  ┌─────────────────────────────────────────────────┐   │
│  │              Django Web Framework               │   │
│  │  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌────────┐ │   │
│  │  │  Views  │ │Templates│ │  Forms  │ │  URLs  │ │   │
│  │  └─────────┘ └─────────┘ └─────────┘ └────────┘ │   │
│  └─────────────────────────────────────────────────┘   │
│                                                         │
│  ┌─────────────────────────────────────────────────┐   │
│  │                Middleware                       │   │
│  │  • Authentication  • CSRF Protection           │   │
│  │  • Session        • Security Headers           │   │
│  │  • Logging        • Error Handling             │   │
│  └─────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────┐
│                    BUSINESS LAYER                       │
│  ┌─────────────────────────────────────────────────┐   │
│  │                Django Models                    │   │
│  │  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌────────┐ │   │
│  │  │  User   │ │ Patient │ │ Doctor  │ │Appointment│ │
│  │  │ Models  │ │ Models  │ │ Models  │ │ Models │ │   │
│  │  └─────────┘ └─────────┘ └─────────┘ └────────┘ │   │
│  └─────────────────────────────────────────────────┘   │
│                                                         │
│  ┌─────────────────────────────────────────────────┐   │
│  │              Business Logic                     │   │
│  │  • Appointment Scheduling  • User Management   │   │
│  │  • Medical Records        • Notifications      │   │
│  │  • Reporting & Analytics  • Audit Logging      │   │
│  └─────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────┐
│                     DATA LAYER                          │
│  ┌─────────────────────────────────────────────────┐   │
│  │                Django ORM                       │   │
│  │  • Query Optimization  • Migration Management  │   │
│  │  • Connection Pooling  • Transaction Handling  │   │
│  └─────────────────────────────────────────────────┘   │
│                            │                           │
│                            ▼                           │
│  ┌─────────────────────────────────────────────────┐   │
│  │              SQLite Database                    │   │
│  │  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌────────┐ │   │
│  │  │  Users  │ │Patients │ │ Doctors │ │Appointments│ │
│  │  │  Table  │ │  Table  │ │  Table  │ │  Table │ │   │
│  │  └─────────┘ └─────────┘ └─────────┘ └────────┘ │   │
│  └─────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────┘
```

### 3.4.2. Kiến trúc Django MTV

**Model Layer:**
```python
# models.py - Data representation
class HoSoBenhNhan(models.Model):
    nguoi_dung = models.OneToOneField(User, on_delete=models.CASCADE)
    ngay_sinh = models.DateField()
    # ... other fields
    
    def tuoi(self):
        """Business logic method"""
        return timezone.now().year - self.ngay_sinh.year
    
    class Meta:
        verbose_name = "Hồ sơ bệnh nhân"
```

**View Layer:**
```python
# views.py - Business logic controller
@login_required
def dat_lich_kham(request, lich_lam_viec_id):
    # Authentication & Authorization
    if not hasattr(request.user, 'ho_so_benh_nhan'):
        return redirect('dang_nhap')
    
    # Business logic
    lich_lam_viec = get_object_or_404(LichLamViec, id=lich_lam_viec_id)
    
    if request.method == 'POST':
        form = DatLichForm(request.POST)
        if form.is_valid():
            # Create appointment
            lich_hen = form.save(commit=False)
            lich_hen.benh_nhan = request.user.ho_so_benh_nhan
            lich_hen.save()
            return redirect('lich_hen_cua_toi')
    
    # Render template
    return render(request, 'dat_lich.html', context)
```

**Template Layer:**
```html
<!-- templates/dat_lich.html - Presentation -->
{% extends 'base.html' %}

{% block content %}
<div class="container">
    <h2>Đặt lịch khám với {{ bac_si.nguoi_dung.get_full_name }}</h2>
    
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit" class="btn btn-primary">Đặt lịch</button>
    </form>
</div>
{% endblock %}
```

### 3.4.3. Security Architecture

**1. Authentication Flow:**
```
User Request → Django Auth Middleware → Session Check → View Access
     ↓                    ↓                   ↓            ↓
Login Required?    Session Valid?      User Active?   Permission Check
     ↓                    ↓                   ↓            ↓
Redirect Login     Create Session      Allow Access   Execute View
```

**2. Authorization Matrix:**
```python
# permissions.py
class PermissionMixin:
    def dispatch(self, request, *args, **kwargs):
        if not self.has_permission(request.user):
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class PatientRequiredMixin(PermissionMixin):
    def has_permission(self, user):
        return hasattr(user, 'ho_so_benh_nhan')

class DoctorRequiredMixin(PermissionMixin):
    def has_permission(self, user):
        return hasattr(user, 'ho_so_bac_si')

class AdminRequiredMixin(PermissionMixin):
    def has_permission(self, user):
        return user.is_staff and not hasattr(user, 'ho_so_benh_nhan') and not hasattr(user, 'ho_so_bac_si')
```

### 3.4.4. Deployment Architecture

**Development Environment:**
```
Developer Machine
├── Python 3.14
├── Django 5.2.8
├── SQLite Database
├── Static Files (Local)
└── Media Files (Local)
```

**Production Environment (Future):**
```
Load Balancer (Nginx)
├── Web Server 1 (Django + Gunicorn)
├── Web Server 2 (Django + Gunicorn)
├── Database Server (PostgreSQL)
├── Static Files (CDN/S3)
├── Media Files (S3)
├── Cache Server (Redis)
└── Monitoring (Sentry)
```

### 3.4.5. Kết luận chương 3

Chương này đã trình bày chi tiết về phân tích và thiết kế hệ thống:

**1. Phân tích yêu cầu:**
- Xác định được 5 nhóm chức năng chính với 20 yêu cầu cụ thể
- Phân tích yêu cầu phi chức năng về hiệu năng, bảo mật, khả năng sử dụng
- Vẽ use case diagram và phân tích chi tiết các actor

**2. Thiết kế cơ sở dữ liệu:**
- Thiết kế ERD với 8 bảng chính và các mối quan hệ
- Định nghĩa ràng buộc toàn vẹn và quy tắc nghiệp vụ
- Lên kế hoạch indexing để tối ưu hiệu năng

**3. Thiết kế giao diện:**
- Áp dụng nguyên tắc User-Centered Design
- Thiết kế responsive cho đa thiết bị
- Tạo wireframe cho các màn hình chính

**4. Kiến trúc hệ thống:**
- Sử dụng kiến trúc Django MTV phân lớp rõ ràng
- Thiết kế security architecture với authentication/authorization
- Lên kế hoạch deployment cho cả development và production

Chương tiếp theo sẽ trình bày quá trình triển khai hệ thống dựa trên thiết kế này.

---
# CHƯƠNG 4: TRIỂN KHAI HỆ THỐNG

## 4.1. Cài đặt môi trường phát triển

### 4.1.1. Yêu cầu hệ thống

**Phần cứng tối thiểu:**
- CPU: Intel Core i3 hoặc AMD equivalent
- RAM: 4GB (khuyến nghị 8GB)
- Ổ cứng: 2GB 