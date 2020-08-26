#!/usr/bin/env python
# coding: utf-8

# In[62]:


from itertools import permutations
from itertools import combinations
data = {'kamu':'S', 'aku':'S', 'ernia':'S', 'adik':'S', 'rifa':'S',
        'sangat suka minum':'P', 'suka makan':'P', 'sedang makan':'P', 'minum':'P', 'ingin pergi':'P', 'makan':'P',
        'donat':'O', 'susu':'O', 'coklat':'O',
        'di rumah':'Ket', 'di sekolah':'Ket', 'ke pasar':'Ket',
        'ketika':'Konj', 'sedangkan':'Konj'}
cocok = {'sedang makan':'Makan', 'donat':'Makan', 'suka makan':'Makan', 'coklat':'Makan',
        'minum':'Minum', 'susu':'Minum', 'sangat suka minum':'Minum'}
j_kata = {'S':0, 'P':0, 'Ket':0, 'Konj':0, 'O':0}

# contoh = 'di sekolah susu adik minum ernia sedang makan donat ketika di rumah'
# contoh = 'suka kamu aku'
# contoh = 'ingin pergi aku ke pasar'
contoh = 'sangat suka minum susu aku rifa sedangkan coklat suka makan'
kalimat2 = ['S', 'P', 'O', 'K', 'Konj', 'S', 'P', 'O', 'K']
y = ''
count = j_kata
jenis = {}
Subjek, Predikat, Keterangan, Konjungsi, Objek = [], [], [], [], []
flag = 0
for i, x in enumerate(contoh):
    if flag == 0:
        y += str(x)
    flag = 0
    if  y in data or (i==len(contoh)-1):
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

# print(count)
# print(jenis)
# print(Subjek)
# print(Predikat)
# print(Keterangan)

Subjek_per = list(permutations(Subjek, len(Subjek)))
Predikat_per = list(permutations(Predikat, len(Predikat)))
Keterangan_per= list(permutations(Keterangan, len(Keterangan)))
Konjungsi_per = list(permutations(Konjungsi, len(Konjungsi)))
Objek_per = list(permutations(Objek, len(Objek)))


# print(Subjek_per)
# print(Predikat_per)
Gabungan_per = [[x, y, j, z, a] for x in Subjek_per for y in Predikat_per 
                for j in Objek_per for z in Keterangan_per for a in Konjungsi_per]
# print(Gabungan_per)
total = []
for i in Gabungan_per:
    gabung = []
    for j in i:
        for k in j:
            gabung.append(k)
    total.append(gabung)
# print(total)


print('Kalimat ngacak:')
print(contoh)
print('')
print('Hasil:')
for i in total:
#     print(i)
    hasil_kal = ''
    flag = 1
    temps = [j for j in i if j[0]=='S']
    tempp = [j for j in i if j[0]=='P']
    tempo = [j for j in i if j[0]=='O']
    tempket = [j for j in i if j[:3]=='Ket']
    tempkonj = [j for j in i if j[:4]=='Konj']
    for x in kalimat2:
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
    print(hasil_kal)


# In[250]:


Subjek_per = permutations(Subjek, len(Subjek))
# print(list(Subjek_per)) #permutasi di dalam permutasi

# for i in list(Subjek_per):
#     print(i)
#     print(i[0], i[1])

# kata1 = 'SPOK'
# for i in list(Subjek_per):
#     kalimat=''
#     ke = 0
#     for x in kata1:
#         if x=='S' or x=='O':
#             kalimat += str(jenis[i[ke]])
#         if ke+1<len(i):
#             ke += 1
#         if x=='P':
#             kalimat += str(jenis['P1'])
#         kalimat += ' '
#     print(kalimat)


# In[48]:


jenis_kata = 'L'
jenis_kata = 'MM'
print(jenis_kata)


# In[ ]:




