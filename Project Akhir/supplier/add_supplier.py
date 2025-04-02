def add_supplier():
    try:
        jawaban = "Y"

        # Buka file suppliers.txt
        supplier_file = open("suppliers.txt", "a")

        while jawaban == "Y":
            print("Masukkan data pemasok berikut: ")

            sp_name = input("Nama pemasok: ")
            sp_address = input("Alamat pemasok: ")
            sp_contact = input("Kontak pemasok: ")

            # Tulis data ke dalam suppliers.txt
            supplier_file.write(sp_name + '\n')
            supplier_file.write(sp_address + '\n')
            supplier_file.write(sp_contact + '\n')

            # Tanya mau tambah lagi atau tidak
            print('Apakah Anda ingin menambahkan data lain?')
            jawaban = input("Y = Ya, T = Tidak: ").upper()

        # kalau jawabannya T (Tidak), looping while berhenti, baru file ditutup
        supplier_file.close()

        # Pesan data berhasil ditambahkan
        print('Data ditambahkan ke suppliers.txt')

    except IOError as e:
        print(f"Terjadi kesalahan saat mengakses file: {e}")

    except Exception as e:
        print(f"Terjadi kesalahan yang tidak terduga: {e}")



