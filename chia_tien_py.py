from PIL import Image

def nhap_du_lieu():
    thanh_vien = []
    so_tien = []

    while True:
        ten = input("Nhập tên thành viên (hoặc nhấn Enter để kết thúc): ")
        if not ten:
            break
        while True:
            try:
                tien = float(input(f"Nhập số tiền món ăn của {ten}: "))
                if tien < 0:
                    print("Số tiền không thể là số âm. Vui lòng nhập lại.")
                    continue
                break
            except ValueError:
                print("Vui lòng nhập một số hợp lệ cho số tiền.")
        thanh_vien.append(ten)
        so_tien.append(tien)
    
    return thanh_vien, so_tien

def hien_thi_ma_qr(filename):
    img = Image.open(filename)
    img.show()

def main():
    # Lựa chọn phương thức chia tiền
    while True:
        phuong_thuc_chia = input("Bạn có muốn chia đều tiền (nhập 'chia đều') hay nhập chi tiết từng người (nhập 'chi tiết')? ").strip().lower()
        if phuong_thuc_chia in ["chia đều", "chi tiết"]:
            break
        else:
            print("Vui lòng nhập 'chia đều' hoặc 'chi tiết'.")

    if phuong_thuc_chia == "chi tiết":
        # Nhập dữ liệu chi tiết từng người
        thanh_vien, so_tien = nhap_du_lieu()
        tong_tien_mon_an = sum(so_tien)
    else:
        # Nhập dữ liệu chia đều
        while True:
            try:
                so_thanh_vien = int(input("Nhập số lượng thành viên trong team: "))
                if so_thanh_vien <= 0:
                    print("Số thành viên phải là một số nguyên dương. Vui lòng nhập lại.")
                    continue
                break
            except ValueError:
                print("Vui lòng nhập một số nguyên hợp lệ cho số lượng thành viên.")
        
        while True:
            try:
                tong_tien_mon_an = float(input("Nhập tổng tiền món ăn: "))
                if tong_tien_mon_an < 0:
                    print("Tổng tiền không thể là số âm. Vui lòng nhập lại.")
                    continue
                break
            except ValueError:
                print("Vui lòng nhập một số hợp lệ cho tổng tiền.")
        
        thanh_vien = ["Thành viên " + str(i + 1) for i in range(so_thanh_vien)]
        so_tien = [tong_tien_mon_an / so_thanh_vien] * so_thanh_vien

    # Nhập loại giảm giá
    while True:
        loai_giam_gia = input("Nhập loại giảm giá (tiền hoặc %): ").strip().lower()
        if loai_giam_gia in ["tiền", "%"]:
            break
        else:
            print("Vui lòng nhập 'tiền' hoặc '%'.")

    # Nhập giá trị giảm giá
    while True:
        try:
            giam_gia = float(input("Nhập giá trị giảm giá: "))
            if giam_gia < 0:
                print("Giảm giá không thể là số âm. Vui lòng nhập lại.")
                continue
            break
        except ValueError:
            print("Vui lòng nhập một số hợp lệ cho giảm giá.")

    # Tính tổng tiền sau khi áp dụng giảm giá
    if loai_giam_gia == "tiền":
        tong_tien_sau_giam_gia = tong_tien_mon_an - giam_gia
    elif loai_giam_gia == "%":
        tong_tien_sau_giam_gia = tong_tien_mon_an * (1 - giam_gia / 100)

    if tong_tien_sau_giam_gia < 0:
        print("Tổng tiền sau khi giảm giá không thể là số âm.")
        return

    # Tính toán số tiền thực tế mỗi người phải thanh toán
    so_tien_thanh_toan = [(tien / tong_tien_mon_an) * tong_tien_sau_giam_gia for tien in so_tien]

    # Hiển thị kết quả
    for ten, tien_phai_tra in zip(thanh_vien, so_tien_thanh_toan):
        print(f"{ten} phải trả: {tien_phai_tra:.2f} VND")

    # Hiển thị mã QR đã có
    hien_thi_ma_qr("QR thanh toan.jpg")
    print("Mã QR đã được hiển thị.")

if __name__ == "__main__":
    main()
