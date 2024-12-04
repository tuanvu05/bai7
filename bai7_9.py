def copy_file(source_path, destination_path):
    try:
        with open(source_path, 'r', encoding='utf-8') as source_file:
            content = source_file.read()  
       
        with open(destination_path, 'w', encoding='utf-8') as destination_file:
            destination_file.write(content)  

        print(f"Đã sao chép nội dung từ {source_path} sang {destination_path} thành công.")
    except FileNotFoundError:
        print(f"Tệp {source_path} không tồn tại.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")
source_path = input("Nhập đường dẫn tệp nguồn: ")
destination_path = input("Nhập đường dẫn tệp đích: ")
copy_file(source_path, destination_path)
