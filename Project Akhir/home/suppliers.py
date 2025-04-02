from supplier.add_supplier import add_supplier
from supplier.show_supplier import show_supplier
from supplier.search_supplier import search_supplier
from supplier.modify_supplier import modify_supplier
from supplier.delete_supplier import delete_supplier
from supplier.keluar_supplier import keluar_supplier

def suppliers():
    answer = True
    while answer:
        print("|| ================================================= ||")
        print('|| Manajemen Data Pemasok                            ||')
        print('|| 1. Tambah Pemasok                                 ||')
        print('|| 2. Tampilkan Pemasok                              ||')
        print('|| 3. Cari Pemasok                                   ||')
        print('|| 4. Ubah Pemasok                                   ||')
        print('|| 5. Hapus Pemasok                                  ||')
        print('|| 6. Keluar                                         ||')
        print("|| ================================================= ||")

        choice = input('Masukkan pilihan Anda: ')

        try:
            if choice == '1':
                add_supplier()

            elif choice == '2':
                show_supplier()

            elif choice == '3':
                search_supplier()

            elif choice == '4':
                modify_supplier()

            elif choice == '5':
                delete_supplier()

            elif choice == '6':
                keluar_supplier()
                answer = False

            else:
                print('Pilihan tidak valid. Silakan coba lagi.')

        except Exception as e:
            print(f"Terjadi kesalahan yang tidak terduga: {e}")