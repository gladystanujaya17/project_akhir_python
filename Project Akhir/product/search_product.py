def search_product():
    try:
        found = False

        keyword = input('Masukkan nama barang untuk pencarian: ')
        product_file = open('products.txt', 'r')

        p_name = product_file.readline()

        while p_name != '':
            p_qty = product_file.readline()
            p_harga = product_file.readline()
            p_satuan = product_file.readline()

            p_name = p_name.rstrip('\n')
            p_qty = p_qty.rstrip('\n')
            p_harga = p_harga.rstrip('\n')
            p_satuan = p_satuan.rstrip('\n')

            if p_name == keyword:
                print('Nama Barang: ', p_name)
                print('Kuantitas Barang:', p_qty)
                print('Harga Barang: ', p_harga)
                print('Satuan Barang:', p_satuan)
                print()

                found = True

            name = product_file.readline()

        product_file.close()

        if not found:
            print('Barang tersebut tidak ditemukan dalam file.')

    except FileNotFoundError:
        print("File products.txt tidak ditemukan.")

    except IOError as e:
        print(f"Terjadi kesalahan saat mengakses file: {e}")

    except Exception as e:
        print(f"Terjadi kesalahan yang tidak terduga: {e}")