team = ['cadangan', 'inti']
hari = ['selasa', 'rabu', 'jumat', 'minggu']
jadwal = []

print('-------jadwal latihan--------')
print('\nsilahkan pilih:')

while True:
    main = input('---1.team---\n---2.hari---\n masukan angka(1/2):')
    if main == '1':
        print('\nteam')
        print('pilih')
        while True:
            for ii in range(0, len(team)):
                print(f'{ii+1}. {team}')
            list_tim = int(input('pilih :'))
            if list_tim == 1:
                jadwal.append(team[0])
                print('\n--jadwal latihan--')
                for a in range(0, len(jadwal)):
                    print(f'{a+1}. {jadwal[a]}')
                break
            elif list_tim == 2:
                jadwal.append(team[1])
                print('\n--jadwal latihan--')
                for a in range(0, len(jadwal)):
                    print(f'{a+1}. {jadwal[a]}')
                break
            else:
                print('pilihan salah')
                continue
    elif main == '2':
        print('\nhari')
        print('pilih')
        while True:
            for ii in range(0, len(hari)):
                print(f'{ii+1}. {hari}')
            list_hari = int(input('pilih :'))
            if list_hari == 1:
                jadwal.append(hari[0])
                print('\n--jadwal latihan--')
                for a in range(0, len(jadwal)):
                    print(f'{a+1}. {jadwal[a]} latihan')
                break
            elif list_hari == 2:
                jadwal.append(hari[1]) 
                print('\n--jadwal latihan--')
                for a in range(0, len(jadwal)):
                    print(f'{a+1}. {jadwal[a]} latihan')
                break
            elif list_hari == 3:
                jadwal.append(hari[2])
                print('\n--jadwal latihan--')
                for a in range(0, len(jadwal)):
                    print(f'{a+1}. {jadwal[a]} fisik di pantai')
                break
            elif list_hari == 4:
                jadwal.append(hari[3])
                print('\n--jadwal latihan--')
                for a in range(0, len(jadwal)):
                    print(f'{a+1}. {jadwal[a]} sparing')
                break
            else:
                print('libur')
                break
    
    tambah = input('ada yang lain y/n?')
    if tambah == 'y':
        continue
    else:
        print('-')
        break