import os

def modify_supplier():
    try:
        found = False

        search = input('Masukkan kode pemasok untuk pencarian: ')

        supplier_file = open('suppliers.txt', 'r')
        temp_file = open('temp1.txt', 'w')

        sp_kode = supplier_file.readline()

        while sp_kode != '':
            sp_name = supplier_file.readline()
            sp_address = supplier_file.readline()
            sp_contact = supplier_file.readline()

            sp_kode = sp_kode.rstrip('\n')
            sp_name = sp_name.rstrip('\n')
            sp_address = sp_address.rstrip('\n')
            sp_contact = sp_contact.rstrip('\n')

            if sp_kode == search:
                print("1. Alamat")
                print("2. Kontak Pemasok")
                print("3. Ganti Kedua Data")
                change_data = input("Masukkan data yang akan diganti: ")

                if change_data == "1":
                    new_sp_address = input(f"Masukkan alamat terbaru dari pemasok {sp_name}: ")

                    temp_file.write(sp_kode + '\n')
                    temp_file.write(sp_name + '\n')
                    temp_file.write(new_sp_address + '\n')
                    temp_file.write(sp_contact + '\n')
                    found = True

                elif change_data == "2":
                    new_sp_contact = input(f'Masukkan kontak baru dari pemasok {sp_name}: ')

                    temp_file.write(sp_kode + '\n')
                    temp_file.write(sp_name + '\n')
                    temp_file.write(sp_address + '\n')
                    temp_file.write(new_sp_contact + '\n')
                    found = True

                elif change_data == "3":
                    new_sp_address = input(f"Masukkan alamat terbaru dari pemasok {sp_name}: ")
                    new_sp_contact = input(f'Masukkan kontak baru dari pemasok {sp_name}: ')

                    temp_file.write(sp_kode + '\n')
                    temp_file.write(sp_name + '\n')
                    temp_file.write(new_sp_address + '\n')
                    temp_file.write(new_sp_contact + '\n')
                    found = True

                else:
                    print("Layanan nomor tidak tersedia")

            else:
                # Kalau datanya tidak ada yang sama seperti di keyword, data akan
                # tetap ditulis ke dalam temp1.txt lewat temp_file
                temp_file.write(sp_kode + '\n')
                temp_file.write(sp_name + '\n')
                temp_file.write(sp_address + '\n')
                temp_file.write(sp_contact + '\n')

            sp_kode = supplier_file.readline()

        supplier_file.close()

        temp_file.close()

        os.remove('suppliers.txt')
        os.rename('temp1.txt', 'suppliers.txt')

        if found:
            print('File telah diperbaharui. ')

        else:
            print('Pemasok tersebut tidak ditemukan ke dalam file.')

    except FileNotFoundError:
        print("File customers.txt tidak ditemukan.")

    except IOError as e:
        print(f"Terjadi kesalahan saat mengakses file: {e}")

    except Exception as e:
        print(f"Terjadi kesalahan yang tidak terduga: {e}")