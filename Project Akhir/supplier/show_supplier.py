def show_supplier():
    try:
        supplier_file = open("suppliers.txt", "r")

        # Baca baris pertama dari file suppliers.txt
        sp_name = supplier_file.readline()

        while sp_name != '':
            # Setelah nama pemasok tidak kosong, baru baca data lain
            sp_address = supplier_file.readline()
            sp_contact = supplier_file.readline()

            sp_name = sp_name.rstrip('\n')
            sp_address = sp_address.rstrip('\n')
            sp_contact = sp_contact.rstrip('\n')

            print(f"Nama pemasok: {sp_name}")
            print(f"Alamat pemasok: {sp_address}")
            print(f"Kontak pemasok: {sp_contact}")
            print()

            # Buat cek lagi apakah namanya sudah habis atau masih ada
            sp_name = supplier_file.readline()

        supplier_file.close()

    except FileNotFoundError:
        print("File suppliers.txt tidak ditemukan.")

    except IOError as e:
        print(f"Terjadi kesalahan saat mengakses file: {e}")

    except Exception as e:
        print(f"Terjadi kesalahan yang tidak terduga: {e}")
