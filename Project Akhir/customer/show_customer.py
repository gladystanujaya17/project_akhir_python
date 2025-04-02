def show_customer():
    try:
        customer_file = open('customers.txt', 'r')

        name = customer_file.readline()

        while name != '':
            no_telp = customer_file.readline()
            place = customer_file.readline()

            name = name.rstrip('\n')
            no_telp = no_telp.rstrip('\n')
            place = place.rstrip('\n')

            print('Nama:', name)
            print('Nomor Telepon:', no_telp)
            print('Daerah Tempat Tinggal:', place)
            print()  # Baris kosong untuk memisahkan data

            name = customer_file.readline()

        customer_file.close()

    except FileNotFoundError:
        print("File customers.txt tidak ditemukan.")

    except IOError as e:
        print(f"Terjadi kesalahan saat mengakses file: {e}")

    except Exception as e:
        print(f"Terjadi kesalahan yang tidak terduga: {e}")