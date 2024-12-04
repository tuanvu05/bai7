def count_lines(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()  
            return len(lines)  
    except FileNotFoundError:
        print(f"Tệp {file_path} không tồn tại.")
        return 0
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")
        return 0
file_path = input("Nhập đường dẫn tệp văn bản: ")
line_count = count_lines(file_path)
print(f"Số dòng trong tệp là: {line_count}")
