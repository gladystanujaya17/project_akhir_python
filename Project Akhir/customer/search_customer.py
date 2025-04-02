def search_customer():
    try:
        found = False

        keyword = input('Masukkan nama pelanggan untuk pencarian: ')
        customer_file = open('customers.txt', 'r')

        name = customer_file.readline()

        while name != '':
            no_telp = customer_file.readline()
            place = customer_file.readline()

            name = name.rstrip('\n')
            no_telp = no_telp.rstrip('\n')
            place = place.rstrip('\n')

            if name == keyword:
                print('Nama: ', name)
                print('Nomor Telepon:', no_telp)
                print('Daerah Tempat Tinggal:', place)
                print()

                found = True

            name = customer_file.readline()

        customer_file.close()

        if not found:
            print('Pelanggan tersebut tidak ditemukan dalam file.')

    except FileNotFoundError:
        print("File customers.txt tidak ditemukan.")

    except IOError as e:
        print(f"Terjadi kesalahan saat mengakses file: {e}")

    except Exception as e:
        print(f"Terjadi kesalahan yang tidak terduga: {e}")