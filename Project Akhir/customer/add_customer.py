def add_customer():
    try:
        jawaban = 'Y'

        # Buka file customers.txt
        customer_file = open('customers.txt', 'a')

        while jawaban == 'Y':
            print('Masukkan data pelanggan berikut: ')

            # Minta data pelanggan
            name = input('Nama: ')
            no_telp = input('Nomor Telepon: ')
            place = input('Daerah Tempat Tinggal: ')

            # Tulis data ke dalam file customers.txt
            customer_file.write(name + '\n')
            customer_file.write(no_telp + '\n')
            customer_file.write(place + '\n')

            # Tanya mau tambah lagi atau tidak
            print('Apakah Anda ingin menambahkan data lain?')
            jawaban = input('Y = Ya, T = Tidak: ').upper()

        # kalau jawabannya T (Tidak), looping while berhenti, baru file ditutup
        customer_file.close()

        # Pesan data berhasil ditambahkan
        print('Data ditambahkan ke customers.txt')

    except IOError as e:
        print(f"Terjadi kesalahan saat mengakses file: {e}")

    except Exception as e:
        print(f"Terjadi kesalahan yang tidak terduga: {e}")