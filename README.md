# photobooth_on_rasp
---
# **Code này để nịnh cô chủ nhiệm**
1. Mô tả
   - Đây là một đoạn mã mô phỏng một cái photobooth trong mô lập trình nhúng của cô Thanh
2. Thực hiện
   - Lắp đặt phần cứng
     - lắp đặt picamera vào rasp
       ![Lắp cam](https://github.com/truong020402/photobooth_on_rasp/blob/main/connect-camera.gif?raw=true)
     - Lắp đặt nút nhấn
       ![ Lắp nút nhấn](https://github.com/truong020402/photobooth_on_rasp/blob/main/ukGkEy7SChx2k7stu6aaxT.png?raw=true)

   - Cài đặt phần cứng
     - Enabled camera
       
       ![enabled1](https://github.com/truong020402/photobooth_on_rasp/blob/main/pi-configuration-menu.png?raw=true)

       ![enbled2](https://github.com/truong020402/photobooth_on_rasp/blob/main/pi-configuration-interfaces-annotated.png?raw=true)

       Hoặc

       ![enbled3](https://github.com/truong020402/photobooth_on_rasp/blob/main/Capture.PNG?raw=true)

       Kiểm tra xem camera đã hoạt động hay chưa nếu in ra kết quả như màn hình là ok!

       ![check camera](https://github.com/truong020402/photobooth_on_rasp/blob/main/Capture4.PNG?raw=true)

      - Cài đặt phần mềm
         - git clone https://github.com/truong020402/cv2_test1.git để tải về các file background và file detect khuôn mặt
         - Có thể sửa chữ trên ảnh trong code

3. Kết quả
   - Sau khi nhấn nút camera sẽ chụp lại hình ảnh và detect ra khuông mặt để gắn thêm hình ảnh
     ![kết quả](https://github.com/truong020402/photobooth_on_rasp/blob/main/1.png?raw=true)
     
