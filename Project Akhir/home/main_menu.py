from customers import customers
from suppliers import suppliers
from products import products
from payments import payments
from keluar_main_menu import keluar_main_menu

def menu():

    print("|| ================================================= ||")
    print('|| Selamat Datang di Toko Listrik XYZ                ||')
    print('|| Pilih Layanan Anda!                               ||')
    print('|| 1. Layanan Customer                               ||')
    print('|| 2. Layanan Supplier                               ||')
    print('|| 3. Layanan Produk                                 ||')
    print('|| 4. Layanan Pembayaran                             ||')
    print('|| 5. Keluar                                         ||')
    print("|| ================================================= ||")

    choice = input('Masukkan pilihan Anda: ')

    try:

        if choice == '1':
            customers()

        elif choice == '2':
            suppliers()

        elif choice == '3':
            products()
            
        elif choice == '4':
            payments()

        elif choice == '5':
            keluar_main_menu()

    except Exception as e:
        print(f"Terjadi kesalahan yang tidak terduga: {e}")


# Memanggil fungsi utama.

if __name__ == "__main__":
    menu()