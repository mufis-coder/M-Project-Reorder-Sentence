#!/usr/bin/env python
# coding: utf-8

# In[6]:


from itertools import permutations
from itertools import combinations

def permutasi_jenis_kata(Subjek, Predikat, Keterangan, Konjungsi, Objek):
    Subjek_per = list(permutations(Subjek, len(Subjek)))
    Predikat_per = list(permutations(Predikat, len(Predikat)))
    Keterangan_per= list(permutations(Keterangan, len(Keterangan)))
    Konjungsi_per = list(permutations(Konjungsi, len(Konjungsi)))
    Objek_per = list(permutations(Objek, len(Objek)))
    return Subjek_per, Predikat_per, Keterangan_per, Konjungsi_per, Objek_per

def list_kombinasi_kata(Gabungan_per):
    total = []
    for i in Gabungan_per:
        gabung = []
        for j in i:
            for k in j:
                gabung.append(k)
        total.append(gabung)
    return total

def pemisah_kalimat(data, kalimat, count_jenis_kata):
    count, jenis, y, flag = j_kata, {}, '', 0
    Subjek, Predikat, Keterangan, Konjungsi, Objek = [], [], [], [], []
    for i, x in enumerate(kalimat):
        if flag == 0:
            y += str(x)
        flag = 0
        if  y in data or (i==len(kalimat)-1):
            count[data[y]] += 1
            jenis.update({str(data[y])+str(count[data[y]]):y})
            if data[y] == 'S':
                Subjek.append(str(data[y])+str(count[data[y]]))
            if data[y] == 'P':
                Predikat.append(str(data[y])+str(count[data[y]]))
            if data[y] == 'Ket':
                Keterangan.append(str(data[y])+str(count[data[y]]))
            if data[y] == 'Konj':
                Konjungsi.append(str(data[y])+str(count[data[y]]))
            if data[y] == 'O':
                Objek.append(str(data[y])+str(count[data[y]]))
            flag = 1
            y = ''
            continue
    return count, jenis, Subjek, Predikat, Keterangan, Konjungsi, Objek

def susun_kalimat(kombinasi_kata, struktur_kalimat):
    hasil_kalimat_total = []
    for i in kombinasi_kata:
    #     print(i)
        hasil_kal = ''
        flag = 1
        temps = [j for j in i if j[0]=='S']
        tempp = [j for j in i if j[0]=='P']
        tempo = [j for j in i if j[0]=='O']
        tempket = [j for j in i if j[:3]=='Ket']
        tempkonj = [j for j in i if j[:4]=='Konj']
        for x in struktur_kalimat:
            if (x=='S') and (len(temps) != 0):
                hasil_kal += str(jenis[temps[0]])
                temps.remove(temps[0])
                hasil_kal +=' '
            if (x=='P') and (len(tempp) != 0):
                predikat = str(jenis[tempp[0]])
                hasil_kal += str(jenis[tempp[0]])
                tempp.remove(tempp[0])
                hasil_kal +=' '
            if (x=='K') and (len(tempket) != 0):
                hasil_kal += str(jenis[tempket[0]])
                tempket.remove(tempket[0])
                hasil_kal +=' '
            if (x == 'Konj') and (len(tempkonj) != 0):
                hasil_kal += str(jenis[tempkonj[0]])
                tempkonj.remove(tempkonj[0])
                hasil_kal +=' '
            if (x=='O') and (len(tempo) != 0):
                if ((predikat in cocok) and (str(jenis[tempo[0]]) in cocok) 
                    and (cocok[predikat] != cocok[str(jenis[tempo[0]])])):
                    flag = 0
                hasil_kal += str(jenis[tempo[0]])
                tempo.remove(tempo[0])
                hasil_kal +=' '
        if flag == 0:
            continue
        hasil_kalimat_total.append(hasil_kal)
    return hasil_kalimat_total

data = {'kamu':'S', 'aku':'S', 'ernia':'S', 'adik':'S', 'rifa':'S',
        'sangat suka minum':'P', 'suka makan':'P', 'sedang makan':'P', 'minum':'P', 'ingin pergi':'P', 'makan':'P',
        'donat':'O', 'susu':'O', 'coklat':'O',
        'di rumah':'Ket', 'di sekolah':'Ket', 'ke pasar':'Ket',
        'ketika':'Konj', 'sedangkan':'Konj'}
cocok = {'sedang makan':'Makan', 'donat':'Makan', 'suka makan':'Makan', 'coklat':'Makan',
        'minum':'Minum', 'susu':'Minum', 'sangat suka minum':'Minum'}
j_kata = {'S':0, 'P':0, 'Ket':0, 'Konj':0, 'O':0}

#masalah
# contoh = 'suka kamu aku'

#jadi
# contoh = 'di sekolah susu adik minum ernia sedang makan donat ketika di rumah'
# contoh = 'ingin pergi aku ke pasar'
# contoh = 'sangat suka minum susu aku rifa sedangkan coklat suka makan'
kalimat2 = ['S', 'P', 'O', 'K', 'Konj', 'S', 'P', 'O', 'K']

count, jenis, Subjek, Predikat, Keterangan, Konjungsi, Objek = pemisah_kalimat(data, contoh, j_kata)
# print(count)
# print(jenis)
# print(Subjek)
# print(Predikat)
# print(Keterangan)

(Subjek_per, Predikat_per, Keterangan_per, 
Konjungsi_per, Objek_per) = permutasi_jenis_kata(Subjek, Predikat, Keterangan, Konjungsi, Objek)
# print(Subjek_per)
# print(Predikat_per)

Gabungan_per = [[x, y, j, z, a] for x in Subjek_per for y in Predikat_per 
                for j in Objek_per for z in Keterangan_per for a in Konjungsi_per]
# print(Gabungan_per)

total = list_kombinasi_kata(Gabungan_per)
# print(total)

print('Kalimat ngacak:')
print(contoh)
print('')
print('Hasil:')
hasil_kalimat = susun_kalimat(total, kalimat2)
for x in hasil_kalimat:
    print(x)


# In[ ]:




