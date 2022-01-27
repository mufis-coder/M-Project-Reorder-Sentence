#!/usr/bin/env python
# coding: utf-8

# In[1]:


from itertools import permutations
from itertools import combinations

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
        
def cari_frasa(lista, minim, data):
    panjang = len(lista)
    i = panjang
    iterlist = [i for i in range(1,panjang+1)]
    ob1 = Solution()
    kombi_old = ob1.combinationSum(iterlist,panjang)
    #masih bisa dikombinasi
#     kombi = [xx for xx in kombi if len(xx)==minim]
    for xx in kombi_old:
        if len(xx) == minim:
            kombi = xx
            break
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
    kombi.sort(reverse=True)
    cek = hasil_frasa_list[0]
    hasil = []
    hasil.append(hasil_frasa_ori[0])
    for i, xx in enumerate(kombi):
        for yy, zz in zip(hasil_frasa_list, hasil_frasa_ori):
            if (len(yy) == xx) and (i != 0) and (cek_frasa(cek, yy)==False):
                hasil.append(zz)
                break
    minim_most = min([len(x) for x in hasil_frasa_list])
    kata_dikit = []
    for x in hasil_frasa_list:
        if len(x) == minim_most:
            for y in x:
                kata_dikit.append(y)
    
    unik_kata = set(kata_dikit)
    dict_most = {x:0 for x in unik_kata}
    for x in kata_dikit:
        dict_most[x] += 1
        
    while (minim>len(hasil)):
        maximum_awal = 0
        for x, y in dict_most.items():
            if y>0:
                maximum_awal = y
        for x, y in dict_most.items():
            if y == maximum_awal:
                dict_most[x] -= 1
                hasil.append(x)
                break
    return (hasil)

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
        hasil_subjek = temps
    if len(tempp) > minim:    
        hasil_predikat = cari_frasa(tempp, minim, data)
    elif len(tempp) <= minim:
        hasil_predikat = tempp
    if len(tempo) > minim:
        hasil_obejk = cari_frasa(tempo, minim, data)
    elif len(tempo) <= minim:
        hasil_objek = tempo
    if len(tempket) > minim:
        hasil_keterangan = cari_frasa(tempket, minim, data)
    elif len(tempket) <= minim:
        hasil_keterangan = tempket
    if len(tempkonj) > minim:
        hasil_konjungsi = cari_frasa(tempkonj, minim, data)
    elif len(tempkonj) <= minim:
        hasil_konjungsi = tempkonj
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
#         print('xx', x)
    return count, jenis

def susun_kalimat(kombinasi_kata, struktur_kalimat):
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


data = {'kamu':'S', 'aku':'S', 'ernia':'S', 'adik':'S', 'rifa':'S',
        'suka':'P', 'minum':'P', 'makan':'P', 'sangat':'P', 'sedang':'P', 'ingin':'P', 'pergi':'P', 'tidur':'P',
        'ingin pergi':'P', 'suka makan':'P', 'sedang makan':'P', 'suka minum':'P', 'sedang minum':'P', 'sangat suka':'P',
        'suka tidur':'P',
        'sangat suka makan':'P', 'sangat suka minum':'P', 'sedang suka makan':'P', 'sangat suka tidur':'P',
        'donat':'O', 'susu':'O', 'coklat':'O',
        'di':'Ket', 'rumah':'Ket', 'sekolah':'Ket', 'ke':'Ket', 'pasar':'Ket',
        'di rumah':'Ket', 'di sekolah':'Ket', 'ke pasar':'Ket',
        'ketika':'Konj', 'sedangkan':'Konj', 'karena':'Konj'}
cocok = {'sedang makan':'Makan', 'donat':'Makan', 'suka makan':'Makan', 'coklat':'Makan',
        'minum':'Minum', 'susu':'Minum', 'sangat suka minum':'Minum'}
j_kata = {'S':0, 'P':0, 'Ket':0, 'Konj':0, 'O':0}

#masalah
# contoh = 'suka kamu aku'
# contoh = 'sangat aku suka di tidur rumah aku tidur karena suka'

#jadi
# contoh = 'di sekolah susu adik minum ernia sedang makan donat ketika di rumah'
# contoh = 'ingin pergi aku ke pasar'
# contoh = 'sangat suka minum susu aku rifa sedangkan coklat suka makan'
# contoh = 'aku donat suka makan di sangat rumah'
contoh = 'sangat aku suka di tidur rumah' #aku sangat suka tidur di rumah



# contoh = 'makan makan suka makan'
# contoh = 'sedang makan suka minum'
kalimat2 = ['S', 'P', 'O', 'K', 'Konj', 'S', 'P', 'O', 'K']

count, jenis = pemisah_kalimat(data, contoh, j_kata)
# print(count)
print('jenis old', jenis)

minimum = minimum_jenis_kata(count)
print('minimum', minimum)

hasil_subjek, hasil_predikat, hasil_objek, hasil_keterangan, hasil_konjungsi = susun_jenis_kata(count, jenis, minimum, data)
print('hasil_subjek, hasil_predikat, hasil_objek, hasil_keterangan, hasil_konjungsi',
      hasil_subjek, hasil_predikat, hasil_objek, hasil_keterangan, hasil_konjungsi)

jenis = {}
Subjek, jenis = hitung_jumlah_kata (hasil_subjek, 'S', jenis)
Predikat, jenis = hitung_jumlah_kata (hasil_predikat, 'P', jenis)
Objek, jenis = hitung_jumlah_kata (hasil_objek, 'O', jenis)
Keterangan, jenis = hitung_jumlah_kata (hasil_keterangan, 'Ket', jenis)
Konjungsi, jenis = hitung_jumlah_kata (hasil_konjungsi, 'Konj', jenis)
print('predikat', Predikat)
print('subjek', Subjek)
print('jenis', jenis)


(Subjek_per, Predikat_per, Keterangan_per, 
Konjungsi_per, Objek_per) = permutasi_jenis_kata(Subjek, Predikat, Keterangan, Konjungsi, Objek)
print(Subjek_per)
print(Predikat_per)

Gabungan_per = [[x, y, j, z, a] for x in Subjek_per for y in Predikat_per 
                for j in Objek_per for z in Keterangan_per for a in Konjungsi_per]
print(Gabungan_per)

total = list_kombinasi_kata(Gabungan_per)
print('total', total)

print('Kalimat ngacak:')
print(contoh)
print('')
print('Hasil:')
hasil_kalimat = susun_kalimat(total, kalimat2)
for x in hasil_kalimat:
    print(x)

