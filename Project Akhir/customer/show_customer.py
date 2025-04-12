def show_customer():
    try:
        customer_file = open('customers.txt', 'r')

        kode_pelanggan = customer_file.readline()

        while kode_pelanggan != '':
            name = customer_file.readline()
            no_telp = customer_file.readline()
            place = customer_file.readline()

            kode_pelanggan = kode_pelanggan.rstrip('\n')
            name = name.rstrip('\n')
            no_telp = no_telp.rstrip('\n')
            place = place.rstrip('\n')

            print('Kode Pelanggan: ', kode_pelanggan)
            print('Nama:', name)
            print('Nomor Telepon:', no_telp)
            print('Daerah Tempat Tinggal:', place)
            print()  # Baris kosong untuk memisahkan data

            kode_pelanggan = customer_file.readline()

        customer_file.close()

    except FileNotFoundError:
        print("File customers.txt tidak ditemukan.")

    except IOError as e:
        print(f"Terjadi kesalahan saat mengakses file: {e}")

    except Exception as e:
        print(f"Terjadi kesalahan yang tidak terduga: {e}")