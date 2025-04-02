import os

def delete_supplier():
    try:
        found = False

        keyword = input('Masukkan nama pemasok untuk pencarian: ')

        supplier_file = open('suppliers.txt', 'r')
        temp_file = open('temp1.txt', 'w')

        sp_name = supplier_file.readline()

        while sp_name != '':
            sp_address = supplier_file.readline()
            sp_contact = supplier_file.readline()

            sp_name = sp_name.rstrip('\n')
            sp_address = sp_address.rstrip('\n')
            sp_contact = sp_contact.rstrip('\n')

            if sp_name != keyword:
                temp_file.write(sp_name + '\n')
                temp_file.write(sp_address + '\n')
                temp_file.write(sp_contact + '\n')

            else:
                found = True

            sp_name = supplier_file.readline()

        supplier_file.close()
        temp_file.close()

        os.remove('suppliers.txt')
        os.rename('temp1.txt', 'suppliers.txt')

        if found:
            print('File telah diperbaharui.')

        else:
            print('Pemasok tersebut tidak ditemukan dalam file.')

    except FileNotFoundError:
        print("File suppliers.txt tidak ditemukan.")

    except IOError as e:
        print(f"Terjadi kesalahan saat mengakses file: {e}")

    except Exception as e:
        print(f"Terjadi kesalahan yang tidak terduga: {e}")
