from product.add_product import add_product
from product.show_product import show_product
from product.search_product import search_product
from product.modify_product import modify_product
from product.delete_product import delete_product
from product.keluar_product import keluar_product

def products():
    answer = True
    while answer:
        print("|| ================================================= ||")
        print('|| Manajemen Data Barang                             ||')
        print('|| 1. Tambah Barang                                  ||')
        print('|| 2. Tampilkan Barang                               ||')
        print('|| 3. Cari Barang                                    ||')
        print('|| 4. Ubah Barang                                    ||')
        print('|| 5. Hapus Barang                                   ||')
        print('|| 6. Keluar                                         ||')
        print("|| ================================================= ||")

        choice = input('Masukkan pilihan Anda: ')

        try:
            if choice == '1':
                add_product()

            elif choice == '2':
                 show_product()

            elif choice == '3':
                 search_product()

            elif choice == '4':
                 modify_product()

            elif choice == '5':
                 delete_product()

            elif choice == '6':
                keluar_product()
                answer = False

            else:
                print('Pilihan tidak valid. Silakan coba lagi.')

        except Exception as e:
            print(f"Terjadi kesalahan yang tidak terduga: {e}")