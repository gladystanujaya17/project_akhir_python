def add_product():
    try:
        jawaban = 'Y'

        product_file = open('products.txt', 'a')

        while jawaban == 'Y':
            print("Masukkan data barang berikut: ")

            p_kode = input("Kode Barang: ")
            p_name = input("Nama barang: ")
            p_qty = input("Kuantitas barang: ")
            p_harga = input("Harga barang: ")
            p_satuan = input("Satuan barang: ")

            # Tulis ke dalam products.txt
            product_file.write(p_kode + '\n')
            product_file.write(p_name + '\n')
            product_file.write(p_qty + '\n')
            product_file.write(p_harga + '\n')
            product_file.write(p_satuan + '\n')

            # Tanya mau tambah lagi atau tidak
            print('Apakah Anda ingin menambahkan data lain?')
            jawaban = input("Y = Ya, T = Tidak: ").upper()

        # kalau jawabannya T (Tidak), looping while berhenti, baru file ditutup
        product_file.close()

        # Pesan data berhasil ditambahkan
        print('Data ditambahkan ke products.txt')

    except IOError as e:
        print(f"Terjadi kesalahan saat mengakses file: {e}")

    except Exception as e:
        print(f"Terjadi kesalahan yang tidak terduga: {e}")
