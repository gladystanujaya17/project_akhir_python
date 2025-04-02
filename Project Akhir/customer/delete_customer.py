import os # Dibutuhkan untuk fungsi remove dan rename

def delete_customer():
    try:

        found = False

        search = input('Masukkan nama pelanggan untuk dihapus: ')

        customer_file = open('customers.txt', 'r')
        temp_file = open('temp.txt', 'w')

        name = customer_file.readline()

        while name != '':
            no_telp = customer_file.readline()
            place = customer_file.readline()

            name = name.rstrip('\n')
            no_telp = no_telp.rstrip('\n')
            place = place.rstrip('\n')

            if name != search:
                temp_file.write(name + '\n')
                temp_file.write(no_telp + '\n')
                temp_file.write(place + '\n')

            else:
                found = True

            name = customer_file.readline()

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