import os # Dibutuhkan untuk fungsi remove dan rename

def add_payments():
    try:
        found = False

        search = input('Masukkan kode produk yang ingin dibeli: ')

        product_file = open('products.txt', 'r')
        temp_file = open('temp.txt', 'w')
        payment_file = open('payments.txt', 'a')

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
                print(f'Produk yang akan dibeli adalah {p_name}')
                t_qty = int(input(f'Kuantitas produk yang akan dibeli: '))
                if int(p_qty) >= t_qty:
                    # Simpan ke file payment
                    payment_file.write(p_name + '\n')
                    payment_file.write(str(t_qty) + '\n')
                    payment_file.write(p_harga + '\n')

                    # Total 1 produk
                    total_harga = t_qty * int(p_harga)

                    payment_file.write(str(total_harga) + '\n')

                    # Kurangi QTY
                    new_p_qty = int(p_qty) - t_qty

                    # Tulis ke temp_file untuk products.txt
                    temp_file.write(p_kode + '\n')
                    temp_file.write(p_name + '\n')
                    temp_file.write(str(new_p_qty) + '\n')
                    temp_file.write(p_harga + '\n')
                    temp_file.write(p_satuan + '\n')

                    # Tampilkan di console
                    print("|| ============== TRANSAKSI PENJUALAN ============== ||")
                    print(f"Nama Barang: {p_name}")
                    print(f"Kuantitas Barang: {t_qty}")
                    print(f"Harga Barang: {p_harga}")
                    print(f"Total Barang: {total_harga}")
                    print("|| ================================================= ||")
                    print()
                    print('Transaksi telah ditambahkan ke dalam payments.txt')
                    print()

                    # Mengubah found menjadi bernilai True
                    found = True

                elif int(p_qty) == 0:
                    print(f'Mohon maaf, stok produk {p_name} sudah habis')
                    print()

                    # Mengubah found menjadi bernilai True
                    found = True

                    # Kalau produknya sudah habis, data akan
                    # tetap ditulis ke dalam temp.txt lewat temp_file
                    temp_file.write(p_kode + '\n')
                    temp_file.write(p_name + '\n')
                    temp_file.write(str(0) + '\n')
                    temp_file.write(p_harga + '\n')
                    temp_file.write(p_satuan + '\n')

                elif int(p_qty) < t_qty:
                    print(f'Mohon maaf, stok produk {p_name} tersisa {p_qty} saja')
                    print(f'Produk yang akan dimasukkan ke dalam transaksi hanya sejumlah {p_qty} barang saja')
                    print()

                    # Simpan ke file payment
                    payment_file.write(p_name + '\n')
                    payment_file.write(str(p_qty) + '\n')
                    payment_file.write(p_harga + '\n')

                    # Total 1 produk
                    total_harga = int(p_qty) * int(p_harga)

                    payment_file.write(str(total_harga) + '\n')

                    # Tulis ke temp_file untuk products.txt
                    temp_file.write(p_kode + '\n')
                    temp_file.write(p_name + '\n')
                    temp_file.write(str(0) + '\n')
                    temp_file.write(p_harga + '\n')
                    temp_file.write(p_satuan + '\n')

                    # Tampilkan di console
                    print("|| ============== TRANSAKSI PENJUALAN ============== ||")
                    print(f"Nama Barang: {p_name}")
                    print(f"Kuantitas Barang: {p_qty}")
                    print(f"Harga Barang: {p_harga}")
                    print(f"Total Barang: {total_harga}")
                    print("|| ================================================= ||")
                    print()
                    print('Transaksi telah ditambahkan ke dalam payments.txt')
                    print()

                    # Mengubah found menjadi bernilai True
                    found = True

                else:
                    print('Produk tidak tersedia, mohon masukkan kembali nama produk yang ingin dibeli!')

            else:
                # Kalau datanya tidak ada yang sama seperti di keyword, data akan
                # tetap ditulis ke dalam temp.txt lewat temp_file
                temp_file.write(p_kode + '\n')
                temp_file.write(p_name + '\n')
                temp_file.write(p_qty + '\n')
                temp_file.write(p_harga + '\n')
                temp_file.write(p_satuan + '\n')

            p_kode = product_file.readline()

        product_file.close()
        temp_file.close()
        payment_file.close()

        os.remove('products.txt')
        os.rename('temp.txt', 'products.txt')

        if found:
            print('File payments.txt telah diperbaharui. ')

        else:
            print('Produk tersebut tidak ditemukan ke dalam file.')

    except FileNotFoundError:
        print("File payments.txt tidak ditemukan.")

    except IOError as e:
        print(f"Terjadi kesalahan saat mengakses file: {e}")

    except Exception as e:
        print(f"Terjadi kesalahan yang tidak terduga: {e}")