def search_payments():
    try:
        found = False

        keyword = input('Masukkan nama barang untuk pencarian: ')
        payment_file = open('payments.txt', 'r')

        t_name = payment_file.readline()

        while t_name != '':
            t_qty = payment_file.readline()
            t_harga = payment_file.readline()
            t_total = payment_file.readline()

            t_name = t_name.rstrip('\n')
            t_qty = t_qty.rstrip('\n')
            t_harga = t_harga.rstrip('\n')
            t_total = t_total.rstrip('\n')

            if t_name == keyword:
                print('Nama Barang:', t_name)
                print('Kuantitas Barang:', t_qty)
                print('Harga Barang:', t_harga)
                print('Total Barang:', t_total)
                print()

                found = True

            t_name = payment_file.readline()

        payment_file.close()

        if not found:
            print('Barang tersebut tidak ditemukan dalam file.')

    except FileNotFoundError:
        print("File payments.txt tidak ditemukan.")

    except IOError as e:
        print(f"Terjadi kesalahan saat mengakses file: {e}")

    except Exception as e:
        print(f"Terjadi kesalahan yang tidak terduga: {e}")