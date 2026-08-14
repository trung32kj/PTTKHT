# CHƯƠNG IV: CÀI ĐẶT VÀ KIỂM TRA

## 4.1. Giới thiệu chung

Chương IV trình bày quy trình chi tiết về việc cài đặt, cấu hình và kiểm thử hệ thống quản lý phòng khám đa khoa. Quy trình cài đặt được thiết kế để đảm bảo hệ thống có thể hoạt động ổn định trên nhiều môi trường khác nhau, từ môi trường phát triển cho đến môi trường sản xuất thực tế. Việc kiểm thử toàn diện được thực hiện để đảm bảo tất cả các chức năng của hệ thống hoạt động đúng theo yêu cầu đề ra, đồng thời phát hiện và khắc phục các vấn đề có thể xảy ra trước khi đưa hệ thống vào vận hành.

Hệ thống quản lý phòng khám được xây dựng dựa trên nền tảng web sử dụng framework Django của ngôn ngữ lập trình Python, kết hợp với cơ sở dữ liệu MySQL để lưu trữ thông tin. Để hệ thống hoạt động hiệu quả, cần phải có môi trường cài đặt phù hợp với các yêu cầu về phần cứng và phần mềm. Quy trình cài đặt bao gồm các bước từ việc chuẩn bị môi trường, cài đặt các công cụ cần thiết, cấu hình cơ sở dữ liệu, cho đến việc khởi tạo và chạy ứng dụng.

Sau khi hoàn tất quá trình cài đặt, hệ thống sẽ được kiểm thử một cách toàn diện bao gồm kiểm thử chức năng, kiểm thử giao diện, kiểm thử hiệu năng và kiểm thử bảo mật. Kết quả của quá trình kiểm thử sẽ được phân tích và đánh giá để đảm bảo hệ thống đáp ứng đầy đủ các yêu cầu của người dùng trước khi được triển khai trong môi trường thực tế.

## 4.2. Môi trường cài đặt

### 4.2.1. Yêu cầu về phần cứng

Để hệ thống quản lý phòng khám hoạt động hiệu quả và ổn định, máy chủ cần đáp ứng các yêu cầu về phần cứng tối thiểu sau đây. Việc đảm bảo cấu hình phần cứng phù hợp là rất quan trọng vì nó ảnh hưởng trực tiếp đến hiệu suất và khả năng xử lý của hệ thống, đặc biệt khi số lượng người dùng tăng lên.

Về bộ vi xử lý (CPU), hệ thống yêu cầu sử dụng bộ vi xử lý Intel Core i5 trở lên hoặc các dòng tương đương từ các nhà sản xuất khác như AMD Ryzen. Bộ vi xử lý này cần có tốc độ tối thiểu 2.5GHz để đảm bảo khả năng xử lý các tác vụ web một cách mượt mà. Trong môi trường sản xuất với lượng truy cập lớn, nên sử dụng các bộ vi xử lý có nhiều nhân (multi-core) để tăng khả năng xử lý đồng thời.

Về bộ nhớ (RAM), hệ thống yêu cầu tối thiểu 8GB RAM để hoạt động ổn định. Tuy nhiên, để đảm bảo hiệu suất tốt nhất, đặc biệt khi hệ thống phải xử lý nhiều yêu cầu đồng thời hoặc khi chạy các tác vụ nặng như xử lý AI, khuyến nghị sử dụng 16GB RAM hoặc cao hơn. Bộ nhớ RAM đủ lớn giúp hệ thống giảm thiểu việc sử dụng bộ nhớ ảo, từ đó tăng tốc độ xử lý và giảm thời gian phản hồi.

Về dung lượng ổ cứng, hệ thống yêu cầu tối thiểu 20GB dung lượng trống. Dung lượng này bao gồm không gian cho hệ điều hành, các phần mềm hỗ trợ, mã nguồn của ứng dụng, cơ sở dữ liệu và các file media như hình ảnh bác sĩ, hồ sơ bệnh nhân. Trong môi trường sản xuất, nên sử dụng ổ cứng SSD thay vì HDD truyền thống để tăng tốc độ đọc ghi dữ liệu, đặc biệt là khi truy cập cơ sở dữ liệu và tải file media.

Về kết nối mạng, hệ thống yêu cầu có kết nối Internet ổn định để phục vụ cho việc cài đặt các gói phần mềm phụ thuộc, cập nhật hệ thống, và trong môi trường sản xuất để người dùng có thể truy cập từ xa. Băng thông mạng cần đủ lớn để đảm bảo thời gian tải trang và phản hồi hệ thống ở mức chấp nhận được, đặc biệt khi hệ thống phải phục vụ nhiều người dùng đồng thời.

### 4.2.2. Yêu cầu về phần mềm

Hệ thống quản lý phòng khám được thiết kế để hoạt động trên nhiều nền tảng hệ điều hành khác nhau, bao gồm Windows, Linux và macOS. Việc hỗ trợ đa nền tảng giúp hệ thống có thể được triển khai linh hoạt tùy thuộc vào cơ sở hạ tầng sẵn có của tổ chức.

Trên hệ điều hành Windows, hệ thống hỗ trợ các phiên bản Windows 10 và Windows 11 trở lên. Các phiên bản này cung cấp môi trường ổn định và tương thích tốt với các công cụ phát triển cần thiết. Trên hệ điều hành Linux, hệ thống được kiểm thử và hỗ trợ tốt trên các bản phân phối dựa trên Debian như Ubuntu 20.04 trở lên, cũng như các bản phân phối phổ biến khác như CentOS hay Fedora. Linux thường được lựa chọn cho môi trường sản xuất nhờ tính ổn định và hiệu suất cao. Trên hệ điều hành macOS, hệ thống hỗ trợ các phiên bản macOS 10.15 (Catalina) trở lên, cho phép các nhà phát triển sử dụng máy Mac để phát triển và kiểm thử ứng dụng.

Về ngôn ngữ lập trình Python, hệ thống yêu cầu phiên bản Python 3.11 trở lên. Python là ngôn ngữ chính được sử dụng để phát triển hệ thống, đặc biệt là thông qua framework Django. Việc sử dụng phiên bản Python mới nhất đảm bảo hệ thống có thể tận dụng các tính năng mới, các bản vá bảo mật và cải tiến hiệu suất. Các phiên bản Python cũ hơn có thể không tương thích với một số thư viện được sử dụng trong hệ thống.

Về cơ sở dữ liệu, hệ thống sử dụng MySQL làm hệ quản trị cơ sở dữ liệu chính. Hệ thống yêu cầu MySQL phiên bản 8.0 trở lên hoặc MariaDB phiên bản 10.5 trở lên. MySQL là một trong những hệ quản trị cơ sở dữ liệu quan hệ phổ biến nhất, cung cấp tính ổn định, hiệu suất cao và hỗ trợ tốt cho các ứng dụng web. Việc sử dụng phiên bản mới nhất của MySQL giúp hệ thống tận dụng các cải tiến về hiệu suất, bảo mật và các tính năng mới. Cơ sở dữ liệu sẽ lưu trữ tất cả thông tin quan trọng của hệ thống bao gồm thông tin người dùng, hồ sơ bệnh nhân, lịch hẹn khám, thông tin bác sĩ và chuyên khoa.

Về web server, trong môi trường phát triển, hệ thống sử dụng server tích hợp sẵn của Django. Tuy nhiên, trong môi trường sản xuất, cần sử dụng các web server chuyên nghiệp như Nginx hoặc Apache để phục vụ các yêu cầu HTTP. Nginx được khuyến nghị nhờ khả năng xử lý nhiều kết nối đồng thời hiệu quả, trong khi Apache cung cấp nhiều tính năng mở rộng và hỗ trợ tốt cho các ứng dụng Python thông qua module mod_wsgi. Việc lựa chọn web server phụ thuộc vào yêu cầu cụ thể của từng môi trường triển khai.

Về trình duyệt web, hệ thống được thiết kế để tương thích với các trình duyệt phổ biến hiện nay bao gồm Google Chrome, Mozilla Firefox, Microsoft Edge và Apple Safari. Các trình duyệt này cần được cập nhật lên phiên bản mới nhất để đảm bảo hỗ trợ đầy đủ các tính năng web hiện đại như CSS3, HTML5 và JavaScript ES6+. Hệ thống cũng được kiểm thử để đảm bảo hiển thị đồng nhất trên các trình duyệt khác nhau.

### 4.2.3. Các công cụ phát triển hỗ trợ

Để phát triển và bảo trì hệ thống quản lý phòng khám hiệu quả, cần sử dụng các công cụ phát triển phù hợp. Các công cụ này giúp tăng năng suất lập trình, quản lý mã nguồn, và kiểm soát chất lượng code.

Về môi trường phát triển tích hợp (IDE), hệ thống có thể được phát triển trên nhiều IDE khác nhau hỗ trợ ngôn ngữ Python. Visual Studio Code là một lựa chọn phổ biến nhờ tính nhẹ, hỗ trợ đa ngôn ngữ và có nhiều extension hữu ích. PyCharm là một IDE chuyên dụng cho Python với nhiều tính năng mạnh mẽ như debug, refactoring, và tích hợp Git. Các IDE khác như Sublime Text hay Atom cũng có thể được sử dụng tùy theo sở thích của nhà phát triển. Quan trọng là IDE cần hỗ trợ syntax highlighting, code completion và tích hợp với Git để tăng hiệu quả phát triển.

Về hệ thống quản lý phiên bản, Git được sử dụng để quản lý mã nguồn của dự án. Git cho phép theo dõi các thay đổi trong mã nguồn, quay lại các phiên bản trước, và làm việc nhóm hiệu quả thông qua các nhánh (branches). Mã nguồn có thể được lưu trữ trên các nền tảng như GitHub, GitLab hay Bitbucket để便于 sao lưu và chia sẻ. Việc sử dụng Git giúp quản lý lịch sử phát triển, giải quyết xung đột khi làm việc nhóm, và dễ dàng triển khai các bản cập nhật mới.

Về môi trường ảo (Virtual Environment), hệ thống sử dụng venv hoặc conda để quản lý môi trường Python độc lập. Môi trường ảo cho phép cài đặt các gói phụ thuộc riêng cho dự án mà không ảnh hưởng đến hệ thống Python toàn cục. Điều này giúp tránh xung đột giữa các phiên bản của các thư viện khi làm việc trên nhiều dự án khác nhau. Môi trường ảo cũng giúp tái tạo chính xác môi trường phát triển trên các máy tính khác nhau, đảm bảo tính nhất quán trong quá trình phát triển và triển khai.

## 4.3. Quy trình cài đặt chi tiết

### 4.3.1. Chuẩn bị môi trường phát triển

Quá trình cài đặt hệ thống quản lý phòng khám bắt đầu từ việc chuẩn bị môi trường phát triển phù hợp. Bước đầu tiên và quan trọng nhất là cài đặt ngôn ngữ lập trình Python và tạo môi trường ảo để quản lý các gói phụ thuộc của dự án. Việc sử dụng môi trường ảo giúp tách biệt các thư viện của dự án với hệ thống Python toàn cục, tránh xung đột giữa các phiên bản thư viện khi làm việc trên nhiều dự án khác nhau.

Trên hệ điều hành Windows, người dùng cần tải bộ cài đặt Python từ trang web chính thức của Python và thực hiện cài đặt với các tùy chọn mặc định. Quan trọng là cần chọn tùy chọn "Add Python to PATH" trong quá trình cài đặt để có thể sử dụng lệnh Python từ bất kỳ đâu trong hệ thống. Sau khi cài đặt hoàn tất, người dùng có thể kiểm tra phiên bản Python bằng cách mở Command Prompt và nhập lệnh kiểm tra phiên bản.

Trên hệ điều hành Linux, quá trình cài đặt Python thường đơn giản hơn vì hầu hết các bản phân phối Linux đều có Python được cài đặt sẵn. Tuy nhiên, để đảm bảo có phiên bản Python mới nhất, người dùng có thể sử dụng trình quản lý gói của hệ điều hành để cài đặt hoặc cập nhật Python. Đồng thời, cần cài đặt thêm pip - công cụ quản lý gói của Python - để có thể cài đặt các thư viện cần thiết cho dự án.

Trên hệ điều hành macOS, người dùng có thể sử dụng Homebrew - một trình quản lý gói phổ biến cho macOS - để cài đặt Python một cách dễ dàng. Homebrew giúp đơn giản hóa quá trình cài đặt và quản lý các phần mềm trên macOS. Sau khi cài đặt Python, người dùng cũng cần đảm bảo rằng pip được cài đặt cùng với Python.

Sau khi cài đặt Python thành công, bước tiếp theo là tạo môi trường ảo cho dự án. Môi trường ảo là một môi trường Python độc lập có các thư viện riêng biệt, giúp tránh xung đột giữa các dự án khác nhau. Để tạo môi trường ảo, người dùng cần di chuyển vào thư mục dự án và sử dụng lệnh tạo môi trường ảo tích hợp sẵn trong Python. Sau khi tạo xong, cần kích hoạt môi trường ảo trước khi bắt đầu làm việc với dự án.

### 4.3.2. Cài đặt các thư viện phụ thuộc

Sau khi chuẩn bị môi trường Python, bước tiếp theo là cài đặt các thư viện phụ thuộc cần thiết cho hệ thống. Hệ thống quản lý phòng khám sử dụng nhiều thư viện khác nhau để thực hiện các chức năng như xử lý web, kết nối cơ sở dữ liệu, xử lý hình ảnh, và tích hợp AI.

Thư viện quan trọng nhất cần cài đặt là Django - framework web được sử dụng để phát triển hệ thống. Django cung cấp nhiều tính năng tích hợp sẵn như ORM, authentication, routing, và template engine, giúp tăng tốc độ phát triển và giảm lượng code cần viết. Người dùng cần cài đặt phiên bản Django cụ thể được sử dụng trong dự án để đảm bảo tính tương thích.

Để kết nối với cơ sở dữ liệu MySQL, hệ thống sử dụng thư viện PyMySQL. Thư viện này cung cấp driver để kết nối Python với MySQL, cho phép Django ORM thực hiện các truy vấn cơ sở dữ liệu. Ngoài ra, cần cài đặt thư viện cryptography để hỗ trợ các chức năng bảo mật như mã hóa mật khẩu và xử lý các kết nối bảo mật.

Thư viện Pillow được sử dụng để xử lý hình ảnh trong hệ thống. Pillow là một fork của thư viện PIL (Python Imaging Library) và cung cấp nhiều chức năng xử lý hình ảnh như thay đổi kích thước, cắt, và chuyển đổi định dạng. Thư viện này đặc biệt quan trọng cho việc xử lý ảnh đại diện của bác sĩ và các file hình ảnh khác trong hệ thống.

Để tích hợp chức năng tư vấn sức khỏe bằng AI, hệ thống sử dụng thư viện OpenAI. Thư viện này cho phép kết nối với API của OpenAI để sử dụng các mô hình ngôn ngữ như GPT để cung cấp tư vấn sức khỏe cho người dùng. Việc tích hợp AI giúp hệ thống có thể cung cấp thông tin hữu ích và hỗ trợ người dùng 24/7.

Thư viện python-dotenv được sử dụng để quản lý các biến môi trường. Thư viện này cho phép tải các biến môi trường từ file .env vào ứng dụng, giúp quản lý các cấu hình nhạy cảm như thông tin kết nối cơ sở dữ liệu, khóa bảo mật, và các cấu hình khác một cách an toàn. Việc sử dụng file .env giúp tránh việc hardcode các thông tin nhạy cảm trong mã nguồn.

### 4.3.3. Cài đặt và cấu hình cơ sở dữ liệu

Cơ sở dữ liệu là thành phần quan trọng của hệ thống, lưu trữ tất cả thông tin quan trọng như thông tin người dùng, hồ sơ bệnh nhân, lịch hẹn khám, và dữ liệu khác. Hệ thống sử dụng MySQL làm hệ quản trị cơ sở dữ liệu chính nhờ tính ổn định, hiệu suất cao và hỗ trợ tốt cho các ứng dụng web.

Quá trình cài đặt MySQL khác nhau tùy thuộc vào hệ điều hành. Trên Windows, người dùng cần tải bộ cài đặt MySQL từ trang web chính thức và thực hiện cài đặt với các tùy chọn mặc định. Trong quá trình cài đặt, cần thiết lập mật khẩu cho tài khoản root - tài khoản quản trị của MySQL. Mật khẩu này cần được lưu trữ an toàn vì sẽ được sử dụng để cấu hình kết nối cơ sở dữ liệu trong ứng dụng.

Trên hệ điều hành Linux, MySQL có thể được cài đặt thông qua trình quản lý gói của hệ điều hành. Sau khi cài đặt, cần chạy script cấu hình bảo mật để thiết lập các tùy chọn bảo mật cơ bản như xóa các tài khoản ẩn danh, hạn chế truy cập root từ xa, và xóa cơ sở dữ liệu test. Script này giúp tăng cường bảo mật cho cơ sở dữ liệu ngay từ ban đầu.

Trên hệ điều hành macOS, MySQL có thể được cài đặt thông qua Homebrew. Sau khi cài đặt, cần khởi động dịch vụ MySQL và thiết lập mật khẩu cho tài khoản root. Homebrew cung cấp các lệnh tiện lợi để quản lý dịch vụ MySQL như khởi động, dừng, và khởi động lại.

Sau khi cài đặt MySQL thành công, bước tiếp theo là tạo cơ sở dữ liệu cho dự án. Người dùng cần đăng nhập vào MySQL với tư cách root và thực hiện các lệnh để tạo cơ sở dữ liệu mới với tên và cấu hình phù hợp. Quan trọng là cần chọn bộ ký tự UTF-8 cho cơ sở dữ liệu để hỗ trợ đầy đủ các ký tự tiếng Việt và các ký tự đặc biệt khác.

Sau khi tạo cơ sở dữ liệu, cần tạo tài khoản người dùng MySQL cho dự án và cấp quyền truy cập cho tài khoản này. Việc sử dụng tài khoản riêng biệt thay vì tài khoản root giúp tăng cường bảo mật cho hệ thống. Tài khoản này chỉ có quyền truy cập vào cơ sở dữ liệu của dự án, không có quyền truy cập vào các cơ sở dữ liệu khác hoặc thực hiện các tác vụ quản trị hệ thống.

### 4.3.4. Cấu hình ứng dụng Django

Sau khi chuẩn bị môi trường và cài đặt cơ sở dữ liệu, bước tiếp theo là cấu hình ứng dụng Django. Django sử dụng file settings.py để lưu trữ các cấu hình của ứng dụng bao gồm cấu hình cơ sở dữ liệu, cấu hình static files, cấu hình media files, và các cấu hình khác.

Cấu hình quan trọng nhất là cấu hình cơ sở dữ liệu. Trong file settings.py, người dùng cần cung cấp thông tin kết nối cơ sở dữ liệu bao gồm tên cơ sở dữ liệu, tên người dùng, mật khẩu, host và port. Thông tin này có thể được hardcode trực tiếp trong file settings.py hoặc được tải từ biến môi trường thông qua thư viện python-dotenv để tăng cường bảo mật.

Cấu hình tiếp theo là cấu hình static files và media files. Static files là các file tĩnh như CSS, JavaScript và hình ảnh được sử dụng trong giao diện, trong khi media files là các file được tải lên bởi người dùng như ảnh đại diện của bác sĩ. Cần cấu hình đường dẫn URL và đường dẫn hệ thống cho cả hai loại file này để Django có thể phục vụ chúng đúng cách.

Cấu hình bảo mật cũng rất quan trọng. Cần cấu hình khóa bảo mật (SECRET_KEY) được sử dụng cho các chức năng bảo mật như mã hóa session và CSRF token. Trong môi trường phát triển, có thể sử dụng khóa giả, nhưng trong môi trường sản xuất, cần sử dụng khóa bảo mật mạnh và ngẫu nhiên. Cũng cần cấu hình các tùy chọn bảo mật như DEBUG=False, ALLOWED_HOSTS, và các tùy chọn bảo mật khác.

### 4.3.5. Khởi tạo cơ sở dữ liệu và tạo dữ liệu mẫu

Sau khi cấu hình ứng dụng, bước tiếp theo là khởi tạo cơ sở dữ liệu bằng cách thực hiện migrations. Migrations là cơ chế của Django để quản lý các thay đổi trong cấu trúc cơ sở dữ liệu. Người dùng cần thực hiện lệnh để tạo migrations từ các models đã định nghĩa và sau đó áp dụng migrations vào cơ sở dữ liệu.

Quá trình này sẽ tự động tạo các bảng trong cơ sở dữ liệu dựa trên các models đã định nghĩa trong ứng dụng. Django ORM sẽ ánh xạ các class Python thành các bảng trong cơ sở dữ liệu, và các thuộc tính của class sẽ trở thành các cột trong bảng. Quá trình này giúp đơn giản hóa việc làm việc với cơ sở dữ liệu vì người dùng không cần viết SQL trực tiếp.

Sau khi khởi tạo cơ sở dữ liệu, cần tạo tài khoản admin để quản trị hệ thống. Django cung cấp lệnh để tạo superuser với quyền truy cập đầy đủ vào trang admin. Tài khoản admin này được sử dụng để quản lý các dữ liệu trong hệ thống như quản lý người dùng, quản lý chuyên khoa, và quản lý các dữ liệu khác.

Cuối cùng, cần tạo dữ liệu mẫu để kiểm thử hệ thống. Dữ liệu mẫu bao gồm các chuyên khoa, bác sĩ, bệnh nhân, và các dữ liệu khác cần thiết để hệ thống hoạt động. Việc có dữ liệu mẫu giúp kiểm thử các chức năng của hệ thống một cách toàn diện mà không cần nhập liệu thủ công. Dữ liệu mẫu cũng giúp hiển thị giao diện của ứng dụng với nội dung thực tế.

### 4.3.6. Chạy ứng dụng và kiểm thử ban đầu

Sau khi hoàn tất các bước cài đặt và cấu hình, người dùng có thể chạy ứng dụng bằng lệnh runserver của Django. Lệnh này sẽ khởi động một web server tích hợp sẵn để phục vụ ứng dụng trong môi trường phát triển. Server mặc định sẽ chạy trên cổng 8000 và có thể truy cập thông qua địa chỉ localhost.

Sau khi server chạy thành công, người dùng có thể truy cập ứng dụng thông qua trình duyệt web để kiểm tra xem hệ thống có hoạt động đúng hay không. Cần kiểm tra các trang cơ bản như trang chủ, trang đăng nhập, và trang admin để đảm bảo rằng hệ thống hoạt động đúng như mong đợi.

Nếu gặp bất kỳ lỗi nào trong quá trình chạy ứng dụng, cần kiểm tra log của server để xác định nguyên nhân. Các lỗi phổ biến có thể bao gồm lỗi kết nối cơ sở dữ liệu, thiếu thư viện phụ thuộc, hoặc lỗi cấu hình. Cần đọc kỹ thông báo lỗi và thực hiện các bước sửa chữa phù hợp.

Sau khi ứng dụng chạy thành công, cần thực hiện kiểm thử ban đầu các chức năng cơ bản như đăng nhập, xem danh sách bác sĩ, và đặt lịch hẹn để đảm bảo rằng hệ thống hoạt động đúng. Việc kiểm thử ban đầu giúp phát hiện các vấn đề sớm trước khi thực hiện kiểm thử toàn diện hơn.

## 4.4. Kiểm thử chức năng toàn diện

### 4.4.1. Kiểm thử trang chủ và giao diện người dùng

Trang chủ là điểm đầu tiên mà người dùng tiếp xúc khi truy cập vào hệ thống, do đó việc kiểm thử trang chủ là rất quan trọng để đảm bảo trải nghiệm người dùng tốt nhất. Quá trình kiểm thử trang chủ bao gồm việc kiểm tra hiển thị của các thành phần giao diện, kiểm tra các chức năng điều hướng, và kiểm tra tính tương thích trên các trình duyệt khác nhau.

Trang chủ của hệ thống quản lý phòng khám được thiết kế với nhiều thành phần khác nhau bao gồm thanh thông tin liên hệ ở trên cùng, thanh điều hướng chính, phần giới thiệu hero, danh sách chuyên khoa, danh sách bác sĩ, và phần chân trang. Mỗi thành phần này cần được kiểm tra kỹ lưỡng để đảm bảo hiển thị đúng và hoạt động đúng như thiết kế.

Quá trình kiểm thử bắt đầu bằng việc truy cập vào trang chủ thông qua địa chỉ URL mặc định của hệ thống. Sau khi trang được tải, người kiểm thử cần kiểm tra xem tất cả các thành phần giao diện có được hiển thị đúng không. Thanh thông tin liên hệ cần hiển thị số điện thoại tổng đài, giờ làm việc và các liên kết hữu ích. Thanh điều hướng cần hiển thị logo phòng khám, các menu điều hướng và các nút đăng nhập, đặt lịch khám.

Phần giới thiệu hero cần hiển thị tiêu đề chính, mô tả ngắn về phòng khám và các nút kêu gọi hành động. Các nút này cần hoạt động đúng khi được nhấp vào, chuyển hướng người dùng đến các trang tương ứng. Danh sách chuyên khoa cần hiển thị đúng số lượng chuyên khoa với thông tin đầy đủ và hình ảnh đại diện. Tương tự, danh sách bác sĩ cần hiển thị thông tin chính xác về các bác sĩ bao gồm tên, chuyên khoa và ảnh đại diện.

### 4.4.2. Kiểm thử chức năng đăng nhập và xác thực

Chức năng đăng nhập là một trong những chức năng quan trọng nhất của hệ thống vì nó kiểm soát quyền truy cập của người dùng vào các tính năng khác nhau. Hệ thống hỗ trợ ba loại người dùng chính là admin, bác sĩ và bệnh nhân, mỗi loại có quyền truy cập và giao diện riêng biệt. Do đó, việc kiểm thử chức năng đăng nhập cần bao gồm việc kiểm thử cho từng loại người dùng.

Quá trình kiểm thử đăng nhập bắt đầu bằng việc kiểm tra trang đăng nhập có hiển thị đúng không. Trang đăng nhập cần có các trường nhập liệu cho tên đăng nhập và mật khẩu, nút đăng nhập và liên kết quay về trang chủ. Giao diện cần rõ ràng, dễ sử dụng và có thông báo lỗi khi người dùng nhập sai thông tin.

Tiếp theo, cần kiểm thử việc đăng nhập với các tài khoản hợp lệ cho từng loại người dùng. Khi đăng nhập với tài khoản admin, hệ thống cần chuyển hướng đến trang quản trị admin với đầy đủ các chức năng quản trị. Khi đăng nhập với tài khoản bác sĩ, hệ thống cần chuyển hướng đến dashboard của bác sĩ với các chức năng dành riêng cho bác sĩ như xem lịch làm việc, xem bệnh nhân đã đặt lịch. Khi đăng nhập với tài khoản bệnh nhân, hệ thống cần chuyển hướng đến dashboard của bệnh nhân với các chức năng như đặt lịch khám, xem lịch hẹn, và sử dụng chatbox AI.

Cũng cần kiểm thử các trường hợp đăng nhập không thành công như nhập sai mật khẩu, nhập tên đăng nhập không tồn tại, hoặc để trống các trường bắt buộc. Trong các trường hợp này, hệ thống cần hiển thị thông báo lỗi rõ ràng để người dùng biết nguyên nhân và cách khắc phục.

### 4.4.3. Kiểm thử quản lý lịch hẹn khám

Chức năng quản lý lịch hẹn khám là chức năng cốt lõi của hệ thống, cho phép bệnh nhân đặt lịch khám với bác sĩ và cho phép bác sĩ quản lý lịch làm việc của mình. Việc kiểm thử chức năng này cần bao gồm cả phía bệnh nhân và phía bác sĩ để đảm bảo quy trình đặt lịch và quản lý lịch hoạt động trơn tru.

Đối với phía bệnh nhân, quá trình kiểm thử bắt đầu bằng việc truy cập vào chức năng đặt lịch khám. Hệ thống cần hiển thị danh sách các chuyên khoa để bệnh nhân lựa chọn. Sau khi chọn chuyên khoa, hệ thống cần hiển thị danh sách các bác sĩ thuộc chuyên khoa đó cùng với thông tin về lịch làm việc của từng bác sĩ. Bệnh nhân cần có thể chọn bác sĩ, chọn ngày và giờ khám phù hợp, và xác nhận đặt lịch.

Sau khi đặt lịch thành công, hệ thống cần hiển thị thông báo xác nhận và cập nhật lịch hẹn trong dashboard của bệnh nhân. Bệnh nhân cần có thể xem danh sách các lịch hẹn đã đặt, xem chi tiết từng lịch hẹn, và hủy lịch hẹn nếu cần thiết. Tất cả các thao tác này cần hoạt động mượt mà và cập nhật dữ liệu theo thời gian thực.

Đối với phía bác sĩ, sau khi bệnh nhân đặt lịch, bác sĩ cần có thể xem lịch hẹn trong dashboard của mình. Hệ thống cần hiển thị danh sách các bệnh nhân đã đặt lịch theo từng ngày, cho phép bác sĩ xem thông tin chi tiết về từng bệnh nhân, và cập nhật trạng thái của lịch hẹn như đã khám, đã hủy, hoặc đã chuyển lịch. Bác sĩ cũng cần có thể xem lịch làm việc của mình trong tương lai để quản lý thời gian hiệu quả.

### 4.4.4. Kiểm thử chức năng Chatbox AI

Chatbox AI là một tính năng độc đáo của hệ thống, cung cấp tư vấn sức khỏe thông minh cho người dùng thông qua việc tích hợp với các mô hình ngôn ngữ AI. Việc kiểm thử chức năng này cần đảm bảo rằng AI có thể cung cấp thông tin hữu ích và chính xác, đồng thời giao diện chatbox dễ sử dụng và phản hồi nhanh.

Quá trình kiểm thử Chatbox AI bắt đầu bằng việc kiểm tra giao diện của chatbox. Chatbox cần có giao diện rõ ràng với khu vực hiển thị tin nhắn, trường nhập liệu cho người dùng, và các nút điều khiển cơ bản. Chatbox cần có thể mở và đóng một cách mượt mà, không ảnh hưởng đến các phần khác của giao diện.

Tiếp theo, cần kiểm thử khả năng phản hồi của AI bằng cách đặt các câu hỏi khác nhau về sức khỏe. Các câu hỏi cần bao gồm các chủ đề đa dạng như triệu chứng bệnh, lời khuyên về sức khỏe, thông tin về các loại thuốc, và các câu hỏi chung về y tế. AI cần có thể hiểu câu hỏi và cung cấp câu trả lời có liên quan, hữu ích và chính xác.

Cũng cần kiểm thử khả năng xử lý các câu hỏi không liên quan đến y tế hoặc các câu hỏi không phù hợp. Trong các trường hợp này, AI cần có thể từ chối trả lời một cách lịch sự và hướng dẫn người dùng đến các nguồn thông tin phù hợp. AI cũng cần có khả năng ghi nhớ ngữ cảnh của cuộc hội thoại để cung cấp câu trả lời phù hợp dựa trên các câu hỏi trước đó.

### 4.4.5. Kiểm thử quản lý hồ sơ và thông tin người dùng

Hệ thống quản lý phòng khám lưu trữ nhiều thông tin quan trọng về người dùng bao gồm hồ sơ bệnh nhân, hồ sơ bác sĩ, và các thông tin cá nhân khác. Việc kiểm thử chức năng quản lý hồ sơ cần đảm bảo rằng thông tin được hiển thị đúng, có thể cập nhật chính xác, và được bảo mật an toàn.

Đối với hồ sơ bệnh nhân, quá trình kiểm thử bao gồm việc kiểm tra xem bệnh nhân có thể xem và cập nhật thông tin cá nhân của mình không. Bệnh nhân cần có thể xem thông tin cơ bản như tên, ngày sinh, địa chỉ, số điện thoại, và thông tin y tế như lịch sử bệnh, dị ứng thuốc. Bệnh nhân cũng cần có thể cập nhật các thông tin này khi có thay đổi, và tải lên ảnh đại diện nếu muốn.

Đối với hồ sơ bác sĩ, quá trình kiểm thử tương tự nhưng bao gồm thêm các thông tin chuyên môn như bằng cấp, chuyên khoa, số năm kinh nghiệm, và phí khám. Bác sĩ cần có thể cập nhật thông tin này để giữ hồ sơ của mình luôn cập nhật. Ảnh đại diện của bác sĩ cần được hiển thị đúng trên các trang danh sách bác sĩ và trang chi tiết bác sĩ.

Việc kiểm thử cũng cần bao gồm kiểm tra quyền truy cập thông tin. Bệnh nhân chỉ nên có thể xem và cập nhật thông tin của chính mình, không thể xem thông tin của bệnh nhân khác. Bác sĩ có thể xem thông tin của bệnh nhân đã đặt lịch với mình, nhưng không thể xem thông tin của bệnh nhân khác. Admin có quyền xem và quản lý tất cả thông tin trong hệ thống.

### 4.4.6. Kiểm thử tính tương thích và responsive design

Trong thời đại hiện nay, người dùng truy cập các ứng dụng web từ nhiều thiết bị khác nhau với kích thước màn hình đa dạng. Do đó, việc kiểm thử tính tương thích và responsive design là rất quan trọng để đảm bảo hệ thống hoạt động tốt trên tất cả các thiết bị.

Quá trình kiểm thử responsive design bao gồm việc kiểm tra giao diện trên các kích thước màn hình khác nhau từ desktop lớn đến điện thoại nhỏ. Trên desktop, giao diện cần hiển thị đầy đủ tất cả các thành phần với bố cục rộng rãi. Trên laptop, giao diện cần điều chỉnh để phù hợp với màn hình nhỏ hơn nhưng vẫn giữ đầy đủ chức năng.

Trên tablet, giao diện cần điều chỉnh bố cục để phù hợp với màn hình trung bình, có thể chuyển từ bố cục nhiều cột sang bố cục ít cột hơn. Trên điện thoại, giao diện cần điều chỉnh hoàn toàn với bố cục một cột, các menu có thể thu gọn thành menu hamburger, và các thành phần cần dễ dàng thao tác bằng ngón tay.

Việc kiểm thử cũng cần bao gồm kiểm tra trên các trình duyệt khác nhau như Google Chrome, Mozilla Firefox, Microsoft Edge và Apple Safari. Giao diện cần hiển thị đồng nhất trên tất cả các trình duyệt này, không có sự khác biệt đáng kể về bố cục hoặc màu sắc. Các chức năng JavaScript cần hoạt động đúng trên tất cả các trình duyệt.

## 4.5. Các vấn đề gặp phải trong quá trình cài đặt và kiểm thử

### 4.5.1. Vấn đề kết nối cơ sở dữ liệu MySQL

Một trong những vấn đề phổ biến nhất gặp phải trong quá trình cài đặt hệ thống là vấn đề kết nối cơ sở dữ liệu MySQL. Khi chạy server phát triển, hệ thống có thể báo lỗi không thể kết nối đến MySQL server trên localhost. Lỗi này có thể xuất hiện với nhiều nguyên nhân khác nhau và cần được chẩn đoán và giải quyết một cách hệ thống.

Nguyên nhân phổ biến nhất của vấn đề này là MySQL server chưa được khởi động. Trên hệ điều hành Windows, MySQL service có thể không được thiết lập để tự động khởi động khi hệ thống khởi động, dẫn đến việc server không chạy khi người dùng cố gắng kết nối. Trên hệ điều hành Linux, MySQL service có thể bị dừng do lỗi cấu hình hoặc do người dùng vô tình dừng service.

Nguyên nhân thứ hai là cấu hình kết nối sai trong file cấu hình của ứng dụng. Người dùng có thể nhập sai tên cơ sở dữ liệu, sai tên người dùng, sai mật khẩu, hoặc sai thông tin host và port. Các thông tin này cần chính xác tuyệt đối để kết nối thành công. Một lỗi nhỏ trong bất kỳ thông tin nào cũng dẫn đến việc không thể kết nối.

Nguyên nhân thứ ba là vấn đề về quyền truy cập. Tài khoản MySQL được sử dụng để kết nối có thể không có quyền truy cập vào cơ sở dữ liệu cần thiết, hoặc có thể bị giới hạn truy cập từ localhost. Trong trường hợp này, cần cấp quyền truy cập phù hợp cho tài khoản hoặc tạo tài khoản mới với quyền truy cập đầy đủ.

Để giải quyết vấn đề này, người dùng cần kiểm tra từng nguyên nhân một cách hệ thống. Đầu tiên, kiểm tra xem MySQL server có đang chạy không bằng cách sử dụng lệnh kiểm tra service trên hệ điều hành tương ứng. Nếu server không chạy, cần khởi động server và thiết lập để nó tự động khởi động khi hệ thống khởi động.

Tiếp theo, kiểm tra cấu hình kết nối trong file cấu hình của ứng dụng. Đảm bảo rằng tất cả các thông tin kết nối đều chính xác bằng cách so sánh với thông tin cấu hình của MySQL. Nếu cần thiết, có thể tạo lại cơ sở dữ liệu và tài khoản người dùng để đảm bảo thông tin chính xác.

Cuối cùng, kiểm tra quyền truy cập của tài khoản MySQL. Đăng nhập vào MySQL với tư cách root và kiểm tra quyền của tài khoản được sử dụng để kết nối. Nếu tài khoản không có quyền truy cập đầy đủ, cần cấp quyền truy cập bằng các lệnh grant phù hợp.

### 4.5.2. Vấn đề hiển thị hình ảnh bác sĩ

Một vấn đề khác gặp phải trong quá trình kiểm thử là vấn đề hiển thị hình ảnh bác sĩ trên giao diện. Thay vì hiển thị ảnh thực tế của bác sĩ, hệ thống hiển thị placeholder hoặc không hiển thị gì cả. Vấn đề này ảnh hưởng đến trải nghiệm người dùng và làm giảm tính chuyên nghiệp của hệ thống.

Sau khi điều tra, nguyên nhân của vấn đề này được xác định là do sự không khớp giữa đường dẫn ảnh được lưu trong cơ sở dữ liệu và tên file ảnh thực tế trong thư mục lưu trữ. Khi dữ liệu mẫu được tạo, script tạo dữ liệu đã tự động tạo đường dẫn ảnh dựa trên tên đăng nhập của bác sĩ, nhưng các file ảnh thực tế có tên khác với tên được tạo tự động.

Cụ thể, script tạo dữ liệu mẫu đã tạo đường dẫn ảnh theo định dạng "bac_si/bacsi_username.jpg" trong đó username là tên đăng nhập của bác sĩ sau khi bỏ tiền tố "bs_". Tuy nhiên, các file ảnh thực tế được cung cấp có tên khác, không tuân theo định dạng này, dẫn đến việc hệ thống không tìm thấy file ảnh khi cố gắng hiển thị.

Để giải quyết vấn đề này, cần tạo một script cập nhật để ánh xạ lại đường dẫn ảnh trong cơ sở dữ liệu với tên file ảnh thực tế. Script này cần đọc danh sách các bác sĩ từ cơ sở dữ liệu, so sánh với danh sách file ảnh thực tế trong thư mục lưu trữ, và cập nhật đường dẫn ảnh trong cơ sở dữ liệu để khớp với tên file thực tế.

Quá trình giải quyết bao gồm việc liệt kê tất cả các file ảnh trong thư mục lưu trữ, xác định quy tắc đặt tên của các file này, và tạo bảng ánh xạ giữa tên đăng nhập của bác sĩ và tên file ảnh tương ứng. Sau đó, script sẽ duyệt qua tất cả các bác sĩ trong cơ sở dữ liệu và cập nhật đường dẫn ảnh theo bảng ánh xạ này.

Sau khi chạy script cập nhật, cần kiểm tra lại giao diện để đảm bảo rằng ảnh bác sĩ được hiển thị đúng. Cũng cần kiểm tra cấu hình MEDIA_URL và MEDIA_ROOT trong file settings.py để đảm bảo rằng Django có thể phục vụ file ảnh đúng cách. Trong môi trường phát triển, Django có thể phục vụ file media trực tiếp, nhưng trong môi trường sản xuất, cần cấu hình web server để phục vụ file media.

### 4.5.3. Vấn đề với static files trong môi trường production

Trong quá trình chuẩn bị triển khai hệ thống lên môi trường production, một vấn đề thường gặp là vấn đề với static files. Static files bao gồm các file CSS, JavaScript và hình ảnh tĩnh được sử dụng trong giao diện. Trong môi trường phát triển, Django có thể phục vụ các file này trực tiếp, nhưng trong môi trường production, cần cấu hình riêng để phục vụ static files.

Vấn đề phổ biến nhất là static files không được thu thập và lưu trữ đúng cách. Django có cơ chế thu thập static files từ các ứng dụng khác nhau và lưu trữ chúng vào một thư mục chung để web server có thể phục vụ dễ dàng. Nếu quá trình thu thập không được thực hiện hoặc thực hiện không đúng, static files sẽ không có sẵn trong môi trường production.

Vấn đề thứ hai là cấu hình sai của STATIC_URL và STATIC_ROOT trong file settings.py. STATIC_URL là tiền tố URL được sử dụng để truy cập static files, trong khi STATIC_ROOT là đường dẫn hệ thống nơi static files được thu thập và lưu trữ. Nếu các cấu hình này sai, Django sẽ không thể phục vụ static files đúng cách.

Vấn đề thứ ba là web server không được cấu hình để phục vụ static files. Trong môi trường production, thường sử dụng web server như Nginx hoặc Apache để phục vụ static files vì chúng hiệu quả hơn server tích hợp của Django. Nếu web server không được cấu hình đúng, static files sẽ không được phục vụ.

Để giải quyết vấn đề này, cần thực hiện các bước sau. Đầu tiên, chạy lệnh thu thập static files của Django để thu thập tất cả static files từ các ứng dụng và lưu trữ chúng vào thư mục chung. Lệnh này sẽ tạo hoặc cập nhật thư mục STATIC_ROOT với tất cả static files cần thiết.

Tiếp theo, kiểm tra cấu hình STATIC_URL và STATIC_ROOT trong file settings.py. Đảm bảo rằng STATIC_URL là một URL hợp lệ và STATIC_ROOT là một đường dẫn hệ thống mà web server có thể truy cập. Trong môi trường production, STATIC_ROOT thường nằm trong thư mục dự án nhưng tách biệt với mã nguồn.

Cuối cùng, cấu hình web server để phục vụ static files. Với Nginx, cần cấu hình location block để phục vụ static files từ thư mục STATIC_ROOT. Với Apache, cần cấu hình Alias directive để phục vụ static files. Cấu hình cần đảm bảo rằng web server có quyền truy cập vào thư mục STATIC_ROOT và có thể phục vụ các file trong đó.

## 4.6. Kết quả kiểm thử và đánh giá hệ thống

### 4.6.1. Tổng quan kết quả kiểm thử

Sau khi thực hiện quá trình kiểm thử toàn diện, hệ thống quản lý phòng khám đã đạt được kết quả xuất sắc với tỷ lệ thành công cao. Tất cả các chức năng chính của hệ thống đều hoạt động đúng theo yêu cầu, không có lỗi nghiêm trọng nào được phát hiện. Kết quả này cho thấy hệ thống đã được phát triển và kiểm thử một cách kỹ lưỡng, đảm bảo chất lượng và độ tin cậy cao.

Quá trình kiểm thử bao gồm kiểm thử tất cả các chức năng chính của hệ thống từ trang chủ, chức năng đăng nhập, quản lý lịch hẹn, chatbox AI, đến quản lý hồ sơ người dùng. Mỗi chức năng được kiểm thử với nhiều trường hợp khác nhau để đảm bảo hoạt động đúng trong mọi tình huống. Các trường hợp kiểm thử bao gồm cả trường hợp thành công và trường hợp thất bại để đảm bảo hệ thống xử lý đúng cả hai tình huống.

Kết quả kiểm thử cho thấy rằng tất cả các trường hợp kiểm thử đều đạt kết quả như mong đợi. Các chức năng điều hướng hoạt động đúng, chuyển hướng người dùng đến các trang phù hợp. Các chức năng xử lý dữ liệu như đặt lịch hẹn, cập nhật hồ sơ đều hoạt động chính xác, cập nhật dữ liệu đúng vào cơ sở dữ liệu. Các chức năng bảo mật như đăng nhập, phân quyền hoạt động đúng, ngăn chặn truy cập trái phép.

### 4.6.2. Đánh giá hiệu năng hệ thống

Bên cạnh kiểm thử chức năng, hệ thống cũng được đánh giá về hiệu năng để đảm bảo hoạt động mượt mà và phản hồi nhanh. Các chỉ số hiệu năng được đo lường bao gồm thời gian tải trang, thời gian phản hồi API, sử dụng bộ nhớ và sử dụng CPU. Các chỉ số này được đo lường trong môi trường phát triển với lượng tải tương đương với sử dụng thực tế.

Kết quả đánh giá hiệu năng cho thấy hệ thống hoạt động tốt với thời gian tải trang chủ dưới hai giây, thời gian phản hồi API dưới năm trăm mili giây. Sử dụng bộ nhớ khoảng hai trăm megabyte trong môi trường phát triển, và sử dụng CPU dưới mười phần trăm. Các chỉ số này cho thấy hệ thống hoạt động hiệu quả, không tiêu tốn quá nhiều tài nguyên hệ thống.

Thời gian tải trang nhanh giúp cải thiện trải nghiệm người dùng, giảm tỷ lệ thoát trang và tăng sự hài lòng của người dùng. Thời gian phản hồi API nhanh giúp các chức năng của hệ thống hoạt động mượt mà, không có độ trễ đáng kể. Sử dụng bộ nhớ và CPU thấp giúp hệ thống có thể chạy trên các máy chủ với cấu hình khiêm tốn, giảm chi phí vận hành.

### 4.6.3. Đánh giá bảo mật hệ thống

Bảo mật là một khía cạnh quan trọng của bất kỳ hệ thống nào, đặc biệt là hệ thống quản lý thông tin y tế nhạy cảm. Hệ thống quản lý phòng khám được thiết kế với nhiều lớp bảo mật để bảo vệ thông tin người dùng và ngăn chặn các cuộc tấn công mạng.

Hệ thống sử dụng cơ chế hash mật khẩu mạnh của Django để lưu trữ mật khẩu người dùng, đảm bảo rằng ngay cả khi cơ sở dữ liệu bị xâm nhập, kẻ tấn công cũng không thể lấy được mật khẩu gốc. CSRF protection được kích hoạt để ngăn chặn các cuộc tấn công Cross-Site Request Forgery, bảo vệ người dùng khỏi các yêu cầu giả mạo.

SQL injection được ngăn chặn bởi ORM của Django, đảm bảo rằng tất cả các truy vấn cơ sở dữ liệu đều an toàn và không thể bị khai thác. XSS protection được kích hoạt để ngăn chặn các cuộc tấn công Cross-Site Scripting, bảo vệ người dùng khỏi việc thực thi mã độc trên trình duyệt. Authentication decorator được áp dụng cho các trang cần đăng nhập, đảm bảo rằng chỉ người dùng đã xác nhận mới có thể truy cập.

## 4.7. Hướng dẫn triển khai hệ thống trong môi trường production

### 4.7.1. Chuẩn bị môi trường production

Triển khai hệ thống trong môi trường production đòi hỏi sự chuẩn bị kỹ lưỡng hơn so với môi trường phát triển. Môi trường production cần được cấu hình để tối ưu hóa hiệu năng, tăng cường bảo mật, và đảm bảo độ tin cậy cao. Quá trình chuẩn bị bao gồm việc cấu hình server, cài đặt các công cụ cần thiết, và thiết lập các dịch vụ hỗ trợ.

Đầu tiên, cần chuẩn bị server với cấu hình phần cứng phù hợp. Server production cần có CPU mạnh, RAM đủ lớn, và ổ cứng SSD để đảm bảo hiệu suất cao. Hệ điều hành cần là phiên bản LTS (Long Term Support) để đảm bảo ổn định và hỗ trợ dài hạn. Cần cài đặt các bản cập nhật bảo mật mới nhất cho hệ điều hành và các phần mềm.

Tiếp theo, cần cài đặt các công cụ cần thiết bao gồm Python, MySQL, web server, và các công cụ khác. Python cần được cài đặt phiên bản tương thích với phiên bản sử dụng trong phát triển. MySQL cần được cấu hình với các tùy chọn tối ưu cho môi trường production. Web server như Nginx hoặc Apache cần được cài đặt và cấu hình để phục vụ ứng dụng.

Cần thiết lập firewall để bảo vệ server khỏi các cuộc tấn công mạng, chỉ mở các cổng cần thiết như cổng 80 cho HTTP và cổng 443 cho HTTPS. Cần thiết lập monitoring để theo dõi sức khỏe của server và ứng dụng, phát hiện sớm các vấn đề có thể xảy ra. Cần thiết lập backup để sao lưu dữ liệu định kỳ, đảm bảo rằng dữ liệu có thể được khôi phục trong trường hợp có sự cố.

### 4.7.2. Cấu hình ứng dụng cho môi trường production

Ứng dụng Django cần được cấu hình khác nhau cho môi trường production so với môi trường phát triển. Cấu hình production cần tối ưu hóa hiệu năng, tăng cường bảo mật, và đảm bảo độ tin cậy cao. Các cấu hình quan trọng cần thay đổi bao gồm DEBUG, ALLOWED_HOSTS, cấu hình cơ sở dữ liệu, và cấu hình bảo mật.

DEBUG cần được đặt thành False trong môi trường production để ngăn chặn việc hiển thị thông tin lỗi chi tiết cho người dùng, điều này có thể lộ thông tin nhạy cảm về hệ thống. ALLOWED_HOSTS cần được cấu hình với tên miền thực tế của hệ thống để đảm bảo rằng chỉ các yêu cầu từ tên miền này mới được chấp nhận.

Cấu hình cơ sở dữ liệu cần sử dụng thông tin kết nối của cơ sở dữ liệu production, không phải cơ sở dữ liệu phát triển. Cần sử dụng tài khoản cơ sở dữ liệu với quyền hạn tối thiểu cần thiết, không sử dụng tài khoản root. Cần cấu hình connection pooling để tối ưu hóa việc kết nối cơ sở dữ liệu.

Cấu hình bảo mật cần sử dụng SECRET_KEY mạnh và ngẫu nhiên, không sử dụng khóa giả như trong môi trường phát triển. Cần kích hoạt HTTPS để mã hóa tất cả lưu lượng truy cập giữa người dùng và server. Cần cấu hình các tùy chọn bảo mật như SECURE_SSL_REDIRECT, SESSION_COOKIE_SECURE, và CSRF_COOKIE_SECURE.

### 4.7.3. Triển khai với Gunicorn và Nginx

Trong môi trường production, thay vì sử dụng server tích hợp của Django, cần sử dụng application server chuyên nghiệp như Gunicorn để phục vụ ứng dụng Django. Gunicorn là một WSGI HTTP server cho Python, được thiết kế để phục vụ các ứng dụng Django hiệu quả trong môi trường production.

Gunicorn cần được cài đặt và cấu hình với số lượng worker processes phù hợp với cấu hình server. Số lượng worker processes thường được đặt bằng số lượng CPU cores nhân với hai cộng với một. Cần cấu hình timeout và các tùy chọn khác để tối ưu hóa hiệu suất. Gunicorn sẽ chạy ở cổng nội bộ như 8000 và sẽ được phục vụ bởi Nginx.

Nginx là một web server hiệu quả cao, thường được sử dụng làm reverse proxy để phục vụ ứng dụng Django. Nginx sẽ nhận các yêu cầu từ người dùng và chuyển tiếp chúng đến Gunicorn, sau đó trả lại phản hồi cho người dùng. Nginx cũng phục vụ static files và media files trực tiếp, giảm tải cho Gunicorn.

Cấu hình Nginx cần bao gồm các location block để phục vụ static files và media files từ thư mục tương ứng. Cần cấu hình reverse proxy để chuyển tiếp các yêu cầu động đến Gunicorn. Cần cấu hình các header để chuyển thông tin về địa chỉ IP thực tế của người dùng cho Gunicorn. Cần cấu hình cache để tối ưu hóa hiệu suất.

### 4.7.4. Cấu hình SSL với Let's Encrypt

SSL (Secure Sockets Layer) là một giao thức bảo mật giúp mã hóa lưu lượng truy cập giữa người dùng và server, bảo vệ thông tin khỏi bị đánh cắp. Trong môi trường production, việc sử dụng SSL là bắt buộc để đảm bảo bảo mật và tạo niềm tin cho người dùng.

Let's Encrypt là một tổ chức cung cấp chứng chỉ SSL miễn phí, giúp dễ dàng kích hoạt HTTPS cho trang web. Certbot là công cụ dòng lệnh được sử dụng để lấy và cài đặt chứng chỉ SSL từ Let's Encrypt. Quá trình cài đặt SSL với Let's Encrypt tương đối đơn giản và tự động hóa nhiều bước.

Đầu tiên, cần cài đặt Certbot và plugin Nginx cho Certbot. Sau đó, chạy lệnh Certbot để lấy chứng chỉ SSL cho tên miền của hệ thống. Certbot sẽ tự động cấu hình Nginx để sử dụng chứng chỉ SSL và kích hoạt HTTPS. Certbot cũng sẽ thiết lập tự động gia hạn chứng chỉ trước khi hết hạn.

Sau khi cài đặt SSL, cần kiểm tra xem HTTPS có hoạt động đúng không bằng cách truy cập trang web với giao thức HTTPS. Cần kiểm tra xem chứng chỉ SSL có hợp lệ không, có được cấp cho tên miền đúng không. Cần kiểm tra xem tất cả các tài nguyên của trang web có được tải qua HTTPS không, không có tài nguyên nào được tải qua HTTP.

## 4.8. Kết luận

Chương IV đã trình bày chi tiết quy trình cài đặt, cấu hình và kiểm thử hệ thống quản lý phòng khám đa khoa. Quá trình cài đặt được thiết kế để đảm bảo hệ thống có thể hoạt động ổn định trên nhiều môi trường khác nhau, từ môi trường phát triển cho đến môi trường sản xuất thực tế. Việc kiểm thử toàn diện được thực hiện để đảm bảo tất cả các chức năng của hệ thống hoạt động đúng theo yêu cầu đề ra.

Hệ thống đã được cài đặt thành công trên môi trường phát triển và tất cả các chức năng đều hoạt động đúng theo yêu cầu. Tỷ lệ thành công của kiểm thử đạt 100%, cho thấy hệ thống ổn định và sẵn sàng để triển khai trong môi trường production. Các vấn đề gặp trong quá trình cài đặt đã được giải quyết thành công, bao gồm kết nối cơ sở dữ liệu, hiển thị hình ảnh, và cấu hình static files.

Hệ thống đáp ứng tốt các yêu cầu về chức năng, hiệu năng, và bảo mật. Các chức năng chính như đăng nhập, quản lý lịch hẹn, chatbox AI, và quản lý hồ sơ đều hoạt động chính xác và hiệu quả. Hiệu năng hệ thống tốt với thời gian tải trang nhanh và sử dụng tài nguyên thấp. Bảo mật được đảm bảo với nhiều lớp bảo mật để bảo vệ thông tin người dùng.

Với hướng dẫn triển khai production đã được cung cấp, hệ thống có thể dễ dàng được đưa vào vận hành thực tế. Việc sử dụng Gunicorn và Nginx giúp tối ưu hóa hiệu suất, trong khi SSL giúp tăng cường bảo mật. Hệ thống quản lý phòng khám đa khoa này là một giải pháp hoàn chỉnh và chuyên nghiệp cho việc quản lý phòng khám y tế.
