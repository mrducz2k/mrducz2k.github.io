import os

def rename_images(start_id: int):
    # Các đuôi file ảnh thường gặp
    image_exts = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp')

    # Lấy tất cả file ảnh trong thư mục hiện tại
    files = [f for f in os.listdir('.') if f.lower().endswith(image_exts)]

    # Sắp xếp cho ổn định (tránh rename lung tung)
    files.sort()

    current_id = start_id

    for file in files:
        ext = os.path.splitext(file)[1]  # lấy phần .jpg / .png
        new_name = f"{current_id}{ext}"

        # Tránh rename đè chính nó
        if file != new_name:
            os.rename(file, new_name)

        current_id += 1

    print(f"Đã đổi tên {len(files)} ảnh, bắt đầu từ ID {start_id}.")

if __name__ == "__main__":
    start = int(input("Nhập ID bắt đầu: "))
    rename_images(start)
