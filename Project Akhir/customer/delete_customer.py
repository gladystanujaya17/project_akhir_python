import os # Dibutuhkan untuk fungsi remove dan rename

def delete_customer():
    try:

        found = False

        search = input('Masukkan kode pelanggan untuk dihapus: ')

        customer_file = open('customers.txt', 'r')
        temp_file = open('temp.txt', 'w')

        kode_pelanggan = customer_file.readline()

        while kode_pelanggan != '':
            name = customer_file.readline()
            no_telp = customer_file.readline()
            place = customer_file.readline()

            kode_pelanggan = kode_pelanggan.rstrip('\n')
            name = name.rstrip('\n')
            no_telp = no_telp.rstrip('\n')
            place = place.rstrip('\n')

            if kode_pelanggan != search:
                temp_file.write(kode_pelanggan + '\n')
                temp_file.write(name + '\n')
                temp_file.write(no_telp + '\n')
                temp_file.write(place + '\n')

            else:
                found = True

            kode_pelanggan = customer_file.readline()

        customer_file.close()
        temp_file.close()

        os.remove('customers.txt')
        os.rename('temp.txt', 'customers.txt')

        if found:
            print('File telah diperbaharui.')

        else:
            print('Karyawan tersebut tidak ditemukan dalam file.')

    except FileNotFoundError:
        print("File customers.txt tidak ditemukan.")

    except IOError as e:
        print(f"Terjadi kesalahan saat mengakses file: {e}")

    except Exception as e:
        print(f"Terjadi kesalahan yang tidak terduga: {e}")