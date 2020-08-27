#!/usr/bin/env python
# coding: utf-8

# In[23]:


from itertools import permutations
from itertools import combinations
import itertools

def minimum_jenis_kata(count):
    minim = []
    for x, y in count.items():
        if (y != 0) and (x != 'Konj'):
            minim.append(y)
    return min(minim)

class Solution(object):
   def combinationSum(self, candidates, target):
      result = []
      unique={}
      candidates = list(set(candidates))
      self.solve(candidates,target,result,unique)
      return result
   def solve(self,candidates,target,result,unique,i = 0,current=[]):
      if target == 0:
         temp = [i for i in current]
         temp1 = temp
         temp.sort()
         temp = tuple(temp)
         if temp not in unique:
            unique[temp] = 1
            result.append(temp1)
         return
      if target <0:
         return
      for x in range(i,len(candidates)):
         current.append(candidates[x])
         self.solve(candidates,target-candidates[x],result,unique,i,current)
         current.pop(len(current)-1)

def cek_frasa(data, frasa):
    for x in frasa:
        if x not in data:
            return False
    return True

def seleksi_kombinasi(kombi_angka, kombi_frasa):
    angka = kombi_angka.copy()
    frasa = kombi_frasa.copy()
    for x, y in zip(kombi_angka, kombi_frasa):
        if (len(x) != len(y)):
            angka.remove(x)
            frasa.remove(y)
    return angka, frasa
        
def cari_frasa(lista, minim, data):
    panjang = len(lista)
    i = panjang
    iterlist = [i for i in range(1,panjang+1)]
    ob1 = Solution()
    kombi = ob1.combinationSum(iterlist,panjang)
    #masih bisa dikombinasi
    kombi = [xx for xx in kombi if len(xx)==minim]
    hasil_frasa_list = []
    hasil_frasa_ori = []
    while i>0:
        sementara = list(permutations(lista, i))
        for k in sementara:
            frasa_list = []
            frasa_ori = ''
            for x, y in enumerate(k):
                frasa_list.append(y)
                frasa_ori += str(y)
                if x != len(k)-1:
                    frasa_ori += ' '
            if frasa_ori in data:
                hasil_frasa_ori.append(frasa_ori)
                hasil_frasa_list.append(frasa_list)
        i -= 1
    hasil_total = []
    for mm in kombi:
        temp = []
        for i, xx in enumerate(mm):
            hasil = []
            for yy, zz in zip(hasil_frasa_list, hasil_frasa_ori):
                if (len(yy) == xx):
                    hasil.append(zz)
            if len(hasil) != 0:
                temp.append(hasil)
        hasil_total.append(temp)
    kombi, hasil_total = seleksi_kombinasi(kombi, hasil_total)
    return (hasil_total)

def susun_jenis_kata(jumlah_jk, jenis_kata, minim, data):
    temps, tempp, tempo, tempket, tempkonj = [], [], [], [], []
    for x, y in jenis_kata.items():
        if x[0]=='S':
            temps.append(y)
        if x[0]=='P':
            tempp.append(y)
        if x[0]=='O':
            tempo.append(y)
        if x[:3]=='Ket':
            tempket.append(y)
        if x[:4]=='Konj':
            tempkonj.append(y)
#     print('temps, tempp, tempo, tempket, tempkonj',temps, tempp, tempo, tempket, tempkonj)

    if len(temps) > minim:
        hasil_subjek = cari_frasa(temps, minim, data)
    elif len(temps) <= minim:
        hasil_subjek = []
        hasil_subjek.append(temps)
    if len(tempp) > minim:
        hasil_predikat = cari_frasa(tempp, minim, data)
    elif len(tempp) <= minim:
        hasil_predikat = []
        hasil_predikat.append(tempp)
    if len(tempo) > minim:
        hasil_obejk = cari_frasa(tempo, minim, data)
    elif len(tempo) <= minim:
        hasil_objek = []
        hasil_objek.append(tempo)
    if len(tempket) > minim:
        hasil_keterangan = cari_frasa(tempket, minim, data)
    elif len(tempket) <= minim:
        hasil_keterangan = []
        hasil_keterangan.append(tempket)
    if len(tempkonj) > minim:
        hasil_konjungsi = cari_frasa(tempkonj, minim, data)
    elif len(tempkonj) <= minim:
        hasil_konjungsi = []
        hasil_konjungsi.append(tempkonj)
    return hasil_subjek, hasil_predikat, hasil_objek, hasil_keterangan, hasil_konjungsi

def permutasi_jenis_kata(Subjek, Predikat, Keterangan, Konjungsi, Objek):
    Subjek_per = list(permutations(Subjek, len(Subjek)))
    Predikat_per = list(permutations(Predikat, len(Predikat)))
    Keterangan_per= list(permutations(Keterangan, len(Keterangan)))
    Konjungsi_per = list(permutations(Konjungsi, len(Konjungsi)))
    Objek_per = list(permutations(Objek, len(Objek)))
    return Subjek_per, Predikat_per, Keterangan_per, Konjungsi_per, Objek_per

def hitung_jumlah_kata (jumlah_frasa_kata, huruf, dict_frasa):
    count, jumlah_frasa = 1, []
    for x in jumlah_frasa_kata:
        dict_frasa.update({huruf+str(count):x})
        jumlah_frasa.append(huruf+str(count))
        count += 1
    return jumlah_frasa, dict_frasa

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
    count, jenis, y, panjang, flag = j_kata, {}, '', len(kalimat), 0
    for i, x in enumerate(kalimat):
        if (x != ' '):
            y += str(x)
        if (i==panjang-1) or (x==' '):
            flag = 1
        if (y in data) and (flag==1):
            count[data[y]] += 1
            jenis.update({str(data[y])+str(count[data[y]]):y})
            y = ''
            flag = 0
            continue
    return count, jenis

def susun_kalimat(kombinasi_kata, struktur_kalimat, jenis, cocok):
    hasil_kalimat_total = []
    for i in kombinasi_kata:
        hasil_kal = ''
        flag = 1
        temps, tempp, tempo, tempket, tempkonj = [], [], [], [], []
        for j in i:
            if j[0]=='S':
                temps.append(j)
            if j[0]=='P':
                tempp.append(j)
            if j[0]=='O':
                tempo.append(j)
            if j[:3]=='Ket':
                tempket.append(j)
            if j[:4]=='Konj':
                tempkonj.append(j)
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

def permutasi_jenis_frasa_kata(lista, long):
    fres = list(itertools.product(*lista))
    hasil = []
    for x in fres:
        hasil.append(list(x))
    return hasil

def permutasi_kata(lista, data):
    i = 1
    SS, SP, SKet, SKonj, SO = ['#*1'], ['#*2'], ['#*3'], ['#*4'], ['#*5']
    Subjek, Predikat, Keterangan, Konjungsi, Objek = [], [], [], [], []
    for x in lista:
        for y in x:
            for z in y:
                if (data[z]=='S'):
                    Subjek.append(y)
                    break
                if (data[z]=='P'):
                    Predikat.append(y)
                    break
                if (data[z]=='Ket'):
                    Keterangan.append(y)
                    break
                if (data[z]=='Konj'):
                    Konjungsi.append(y)
                    break
                if (data[z]=='O'):
                    Objek.append(y)
                    break
    if len(Subjek) == 0:
        Subjek.append(SS)
    if len(Predikat) == 0:
        Predikat.append(SP)
    if len(Keterangan) == 0:
        Keterangan.append(SKet)
    if len(Konjungsi) == 0:
        Konjungsi.append(SKonj)
    if len(Objek) == 0:
        Objek.append(SO)
    hasil_return = [[a, b, c, d, e] for a in Subjek for b in Predikat for c in Keterangan
           for d in Konjungsi for e in Objek]
    return hasil_return

def fungsi_bedain_jenis_kal(kalimat, data):
    Subjek, Predikat, Keterangan, Konjungsi, Objek = [], [], [], [], []
    for x in kalimat:
        for z in x:
            if (z in data) and (data[z]=='S'):
                Subjek = x
                break
            if (z in data) and (data[z]=='P'):
                Predikat = x
                break
            if (z in data) and (data[z]=='Ket'):
                Keterangan = x
                break
            if (z in data) and (data[z]=='Konj'):
                Konjungsi = x
                break
            if (z in data) and (data[z]=='O'):
                Objek = x
                break
    return (Subjek, Predikat, Keterangan, Konjungsi, Objek)

def kalimat_to_list(hasil):
    hasila, y = [], ''
    for x in hasil:
        if x!= ' ':
            y += str(x)
        else:
            if (len(y) > 0):
                hasila.append(y)
            y = ''
    if (len(y) > 0):
        hasila.append(y)
    return hasila

def cek_apakah_sama(hasil, ori):
    hasila = kalimat_to_list(hasil)
    oria = kalimat_to_list(ori)
    
    hasilax = hasila.copy()
    oriax = oria.copy()
    for x in hasila:
        if x in oriax:
            oriax.remove(x)
        else:
            return False
            break
    return True           

def fungsi_hasil_awal (hasil_subjek, hasil_predikat, hasil_keterangan, hasil_konjungsi, 
                       hasil_objek, kalimat_ori, cocok):
    jenis = {}
    Subjek, jenis = hitung_jumlah_kata (hasil_subjek, 'S', jenis)
    Predikat, jenis = hitung_jumlah_kata (hasil_predikat, 'P', jenis)
    Objek, jenis = hitung_jumlah_kata (hasil_objek, 'O', jenis)
    Keterangan, jenis = hitung_jumlah_kata (hasil_keterangan, 'Ket', jenis)
    Konjungsi, jenis = hitung_jumlah_kata (hasil_konjungsi, 'Konj', jenis)


    (Subjek_per, Predikat_per, Keterangan_per, 
    Konjungsi_per, Objek_per) = permutasi_jenis_kata(Subjek, Predikat, Keterangan, Konjungsi, Objek)

    Gabungan_per = [[x, y, j, z, a] for x in Subjek_per for y in Predikat_per 
                    for j in Objek_per for z in Keterangan_per for a in Konjungsi_per]

    total = list_kombinasi_kata(Gabungan_per)
    hasil_kalimat = susun_kalimat(total, kalimat2, jenis, cocok)
    hasil_semua_sementara = []
    for x in hasil_kalimat:
        if cek_apakah_sama(x, kalimat_ori) == True:
            hasil_semua_sementara.append(x)
    return hasil_semua_sementara

data = {'kamu':'S', 'aku':'S', 'ernia':'S', 'adik':'S', 'rifa':'S',
        'suka':'P', 'minum':'P', 'makan':'P', 'sangat':'P', 'sedang':'P', 'ingin':'P', 'pergi':'P',
        'ingin pergi':'P', 'suka makan':'P', 'sedang makan':'P', 'suka minum':'P', 'sedang minum':'P',
        'sangat suka makan':'P', 'sangat suka minum':'P', 'sedang suka makan':'P',
        'donat':'O', 'susu':'O', 'coklat':'O',
        'di':'Ket', 'rumah':'Ket', 'sekolah':'Ket', 'ke':'Ket', 'pasar':'Ket',
        'di rumah':'Ket', 'di sekolah':'Ket', 'ke pasar':'Ket',
        'ketika':'Konj', 'sedangkan':'Konj'}
cocok = {'sedang makan':'Makan', 'donat':'Makan', 'suka makan':'Makan', 'coklat':'Makan',
        'minum':'Minum', 'susu':'Minum', 'sangat suka minum':'Minum', 'sedang minum':'Minum', 'suka minum':'Minum'}
j_kata = {'S':0, 'P':0, 'Ket':0, 'Konj':0, 'O':0}

#masalah
#objek dan subjek
#aku bisa jadi objek dan subjek dll
#minimum
# contoh = 'suka kamu aku'
# contoh = 'makan makan suka makan'
# contoh = 'sedang makan suka minum'

#jadi
# contoh = 'di sekolah susu adik minum ernia sedang makan donat ketika di rumah'
# contoh = 'ingin pergi aku ke pasar'
# contoh = 'sangat suka minum susu aku rifa sedangkan coklat suka makan'
# contoh = 'aku donat suka makan di sangat rumah'
contoh = 'sangat minum suka susu aku suka rifa sedangkan coklat makan'
kalimat2 = ['S', 'P', 'O', 'K', 'Konj', 'S', 'P', 'O', 'K']

count, jenis = pemisah_kalimat(data, contoh, j_kata)

### masih sedikit bermasalah
minimum = minimum_jenis_kata(count)
# minimum = 2

hasil_subjek, hasil_predikat, hasil_objek, hasil_keterangan, hasil_konjungsi = susun_jenis_kata(count, jenis, minimum, data)
permutasi_awal = [[i, j, k, l, m] for i in hasil_subjek for j in hasil_predikat 
                  for k in hasil_objek for l in hasil_keterangan for m in hasil_konjungsi]
hasil_final_total = []
for x in permutasi_awal:
#     print('xxx', x) #awallll jgn di sini!!!
    semua_list = []
    for y in x:
        for z in y:
            flag = 0
            if len(z[0])>1:
                flag = 1
        masuk_list = []
        if flag==1:
            panjang = len(y)
            hasil = permutasi_jenis_frasa_kata(y, panjang)
            semua_list.append(hasil)
        else:
            masuk_list.append(y)
            semua_list.append(masuk_list)
    hasil_permu_kata = permutasi_kata(semua_list, data)
    hasil_semua_total = []
    for a in hasil_permu_kata:
        Subjekn, Predikatn, Keterangann, Konjungsin, Objekn = fungsi_bedain_jenis_kal (a, data)
        tampungan = fungsi_hasil_awal(Subjekn, Predikatn, Keterangann, Konjungsin, Objekn, contoh, cocok)
        tampungan = list(set(tampungan))
        if len(tampungan) > 0:
            hasil_semua_total += tampungan
    hasil_final_total += hasil_semua_total

print('Kalimat ngacak:')
print(contoh)
print('')
print('Hasil:')
set_hasil_final_total = list(set(hasil_final_total))
for iter_akhir in set_hasil_final_total:
    print(iter_akhir)

