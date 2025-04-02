from payment.add_payments import add_payments
from payment.search_payments import search_payments
from payment.keluar_payments import keluar_payments

def payments():
    answer = True
    while answer:
        print("|| ================================================= ||")
        print('|| Transaksi Barang                                  ||')
        print('|| 1. Tambah Transaksi                               ||')
        print('|| 2. Cari Transaksi                                 ||')
        print('|| 3. Keluar                                         ||')
        print("|| ================================================= ||")

        choice = input('Masukkan pilihan Anda: ')

        try:
            if choice == '1':
                add_payments()

            elif choice == '2':
                search_payments()

            elif choice == '3':
                keluar_payments()
                answer = False

            else:
                print('Pilihan tidak valid. Silakan coba lagi.')

        except Exception as e:
            print(f"Terjadi kesalahan yang tidak terduga: {e}")