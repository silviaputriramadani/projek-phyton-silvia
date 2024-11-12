while True :
    print('='*50)
    print('1. penjumlahan')
    print('2. pengurangan')
    print('3. penjumlahan')
    print('4. pengurangan')
    print('5. perkalian')
    print('6. pembagian')

    try:
        inputUser = int(input('masukkan pilihan operasi (1/2/3/4/5/6):'))
        num1 = float(input('masukkan angka pertama:'))
        num2 = float(input('masukkan angka kedua:'))
        print('')

        if inputUser == 1:
            hasil = num1 + num2
            print(f'Hasil penjumlahan: {hasil}')
        elif inputUser == 2:
            hasil = num1 - num2
            print(f'hasil pengurangan: {hasil}')
        elif inputUser == 3:
            hasil = num1 * num2
            print(f'hasil perkalian: {hasil}')
        elif inputUser == 4:
            if num1 == 0 and num2 == 0:
                print('tidak terhhingga.')
            elif num2 == 0:
                print('error: pembagian tidak diperbolehkan menggunakan 0.')
            else:
                hasil = num1 / num2
                print(f'hasil pembagian: {hasil}')
        else:
            print('masukkan angka operasi dengan benar.')

    except ValueError:
        print('')
        print('masukkan angka dengan benar.')

    print('')
    kondisi = input('apakah anada ingin keluar(y/n)')
    if kondisi == 'y':
      break

            
            
            

           