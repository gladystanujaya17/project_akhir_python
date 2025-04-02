# Import
from customer.add_customer import add_customer
from customer.show_customer import show_customer
from customer.search_customer import search_customer
from customer.modify_customer import modify_customer
from customer.delete_customer import delete_customer
from customer.keluar_customer import keluar_customer

def customers():
    answer = True
    while answer:
        print("|| ================================================= ||")
        print('|| Manajemen Data Pelanggan                          ||')
        print('|| 1. Tambah Pelanggan                               ||')
        print('|| 2. Tampilkan Pelanggan                            ||')
        print('|| 3. Cari Pelanggan                                 ||')
        print('|| 4. Ubah Pelanggan                                 ||')
        print('|| 5. Hapus Pelanggan                                ||')
        print('|| 6. Keluar                                         ||')
        print("|| ================================================= ||")

        choice = input('Masukkan pilihan Anda: ')

        try:
            if choice == '1':
                add_customer()

            elif choice == '2':
                show_customer()

            elif choice == '3':
                search_customer()

            elif choice == '4':
                modify_customer()

            elif choice == '5':
                delete_customer()

            elif choice == '6':
                keluar_customer()
                answer = False

            else:
                print('Pilihan tidak valid. Silakan coba lagi.')

        except Exception as e:
            print(f"Terjadi kesalahan yang tidak terduga: {e}")