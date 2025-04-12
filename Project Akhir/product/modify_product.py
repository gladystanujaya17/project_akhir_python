import os

def modify_product():
    try:
        found = False

        search = input('Masukkan kode produk untuk pencarian: ')

        product_file = open('products.txt', 'r')
        temp_file = open('temp2.txt', 'w')

        p_kode = product_file.readline()

        while p_kode != '':
            p_name = product_file.readline()
            p_qty = product_file.readline()
            p_harga = product_file.readline()
            p_satuan = product_file.readline()

            p_kode = p_kode.rstrip('\n')
            p_name = p_name.rstrip('\n')
            p_qty = p_qty.rstrip('\n')
            p_harga = p_harga.rstrip('\n')
            p_satuan = p_satuan.rstrip('\n')

            if p_kode == search:
                print("1. Kuantitas Barang")
                print("2. Harga Barang")
                print("3. Ganti Kedua Data")
                change_data = input("Masukkan data yang akan diganti: ")

                if change_data == "1":
                    new_p_qty = input(f"Masukkan kuantitas terbaru dari barang {p_name}: ")

                    temp_file.write(p_kode + '\n')
                    temp_file.write(p_name + '\n')
                    temp_file.write(new_p_qty + '\n')
                    temp_file.write(p_harga + '\n')
                    temp_file.write(p_satuan + '\n')
                    found = True

                elif change_data == "2":
                    new_p_harga = input(f'Masukkan harga terbaru dari barang {p_name}: ')

                    temp_file.write(p_kode + '\n')
                    temp_file.write(p_name + '\n')
                    temp_file.write(p_qty + '\n')
                    temp_file.write(new_p_harga + '\n')
                    temp_file.write(p_satuan + '\n')
                    found = True

                elif change_data == "3":
                    new_p_qty = input(f"Masukkan kuantitas terbaru dari barang {p_name}: ")
                    new_p_harga = input(f'Masukkan harga terbaru dari barang {p_name}: ')

                    temp_file.write(p_kode + '\n')
                    temp_file.write(p_name + '\n')
                    temp_file.write(new_p_qty + '\n')
                    temp_file.write(new_p_harga + '\n')
                    temp_file.write(p_satuan + '\n')
                    found = True

                else:
                    print("Layanan nomor tidak tersedia")

            else:
                # Kalau datanya tidak ada yang sama seperti di keyword, data akan
                # tetap ditulis ke dalam temp1.txt lewat temp_file
                temp_file.write(p_kode + '\n')
                temp_file.write(p_name + '\n')
                temp_file.write(p_qty + '\n')
                temp_file.write(p_harga + '\n')
                temp_file.write(p_satuan + '\n')

            p_kode = product_file.readline()

        product_file.close()

        temp_file.close()

        os.remove('products.txt')
        os.rename('temp2.txt', 'products.txt')

        if found:
            print('File telah diperbaharui. ')

        else:
            print('Produk tersebut tidak ditemukan ke dalam file.')

    except FileNotFoundError:
        print("File products.txt tidak ditemukan.")

    except IOError as e:
        print(f"Terjadi kesalahan saat mengakses file: {e}")

    except Exception as e:
        print(f"Terjadi kesalahan yang tidak terduga: {e}")