def search_supplier():
    try:
        found = False

        keyword = input('Masukkan kode pemasok untuk pencarian: ')
        supplier_file = open('suppliers.txt', 'r')

        sp_kode = supplier_file.readline()

        while sp_kode != '':
            sp_name = supplier_file.readline()
            sp_address = supplier_file.readline()
            sp_contact = supplier_file.readline()

            sp_kode = sp_kode.rstrip('\n')
            sp_name = sp_name.rstrip('\n')
            sp_address = sp_address.rstrip('\n')
            sp_contact = sp_contact.rstrip('\n')

            if sp_kode == keyword:
                print(f'Kode Pemasok: {sp_kode}')
                print(f'Nama: {sp_name}')
                print(f"Alamat Pemasok: {sp_address}")
                print(f"Kontak Pemasok: {sp_contact}")
                print()

                found = True

            sp_kode = supplier_file.readline()

        supplier_file.close()

        if not found:
            print('Pemasok tersebut tidak ditemukan dalam file.')

    except FileNotFoundError:
        print("File suppliers.txt tidak ditemukan.")

    except IOError as e:
        print(f"Terjadi kesalahan saat mengakses file: {e}")

    except Exception as e:
        print(f"Terjadi kesalahan yang tidak terduga: {e}")