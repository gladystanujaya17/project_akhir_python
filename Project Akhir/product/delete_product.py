import os

def delete_product():
    try:
        found = False

        keyword = input('Masukkan nama barang untuk pencarian: ')

        product_file = open('products.txt', 'r')
        temp_file = open('temp2.txt', 'w')

        p_name = product_file.readline()

        while p_name != '':
            p_qty = product_file.readline()
            p_harga = product_file.readline()
            p_satuan = product_file.readline()

            p_name = p_name.rstrip('\n')
            p_qty = p_qty.rstrip('\n')
            p_harga = p_harga.rstrip('\n')
            p_satuan = p_satuan.rstrip('\n')

            if p_name != keyword:
                temp_file.write(p_name + '\n')
                temp_file.write(p_qty + '\n')
                temp_file.write(p_harga + '\n')
                temp_file.write(p_satuan + '\n')

            else:
                found = True

            p_name = product_file.readline()

        product_file.close()
        temp_file.close()

        os.remove('../products.txt')
        os.rename('temp2.txt', '../products.txt')

        if found:
            print('File telah diperbaharui.')

        else:
            print('Barang tersebut tidak ditemukan dalam file.')

    except FileNotFoundError:
        print("File products.txt tidak ditemukan.")

    except IOError as e:
        print(f"Terjadi kesalahan saat mengakses file: {e}")

    except Exception as e:
        print(f"Terjadi kesalahan yang tidak terduga: {e}")
