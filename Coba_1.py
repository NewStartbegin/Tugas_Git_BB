Data_panen = {
    'Lokasi_1':{
        'nama_lokasi':'kebun A',
        'hasil_panen':{
            'padi': 1200,
            'jagung':800,
            'kedelai':500
        }
    },
    'Lokasi_2':{
        'nama_lokasi':'kebun B',
        'hasil_panen':{
            'padi': 1500,
            'jagung':900,
            'kedelai':450
        }
    },
    'Lokasi_3':{
        'nama_lokasi':'kebun C',
        'hasil_panen':{
            'padi': 1100,
            'jagung':750,
            'kedelai':600
        }
    },
    'Lokasi_4':{
        'nama_lokasi':'kebun D',
        'hasil_panen':{
            'padi': 1300,
            'jagung':850,
            'kedelai':550
        }
    },
    'Lokasi_5':{
        'nama_lokasi':'kebun E',
        'hasil_panen':{
            'padi': 1400,
            'jagung':950,
            'kedelai':480
        }
    }
}
print("No 1")

for tempat,data in Data_panen.items():
    print(f"{tempat}\nNama Tempat :{data['nama_lokasi']}\nHasil Panen :")
    for tanaman,berat in data['hasil_panen'].items():
        print(f"    {tanaman} = {berat}Kg")

print("No 2")

print(f"Jumlah Jagung Yang Ada Di lokasi 2 = {Data_panen['Lokasi_2']['hasil_panen']['jagung']}Kg")

print("No 3")

print(f"Tempat Ke 3 Berada Di {Data_panen['Lokasi_3']['nama_lokasi']}")

print("No 4")

padi1 = Data_panen['Lokasi_1']['hasil_panen']['padi']
padi2 = Data_panen['Lokasi_2']['hasil_panen']['padi']
padi3 = Data_panen['Lokasi_3']['hasil_panen']['padi']
padi4 = Data_panen['Lokasi_4']['hasil_panen']['padi']
padi5 = Data_panen['Lokasi_5']['hasil_panen']['padi']
kedelai1 = Data_panen['Lokasi_1']['hasil_panen']['kedelai']
kedelai2 = Data_panen['Lokasi_2']['hasil_panen']['kedelai']
kedelai3 = Data_panen['Lokasi_3']['hasil_panen']['kedelai']
kedelai4 = Data_panen['Lokasi_4']['hasil_panen']['kedelai']
kedelai5 = Data_panen['Lokasi_5']['hasil_panen']['kedelai']

print(f"Data Padi Dan Kedelai Di setiap Tempat\n{Data_panen['Lokasi_1']['nama_lokasi']} {padi1}Kg\n{Data_panen['Lokasi_1']['nama_lokasi']} {kedelai1}Kg\n{Data_panen['Lokasi_2']['nama_lokasi']} {padi2}Kg\n{Data_panen['Lokasi_2']['nama_lokasi']} {kedelai2}Kg\n{Data_panen['Lokasi_3']['nama_lokasi']} {padi3}Kg\n{Data_panen['Lokasi_3']['nama_lokasi']} {kedelai3}Kg\n{Data_panen['Lokasi_4']['nama_lokasi']} {padi4}Kg\n{Data_panen['Lokasi_4']['nama_lokasi']} {kedelai4}Kg\n{Data_panen['Lokasi_5']['nama_lokasi']} {padi5}Kg\n{Data_panen['Lokasi_5']['nama_lokasi']} {kedelai5}Kg")

print("No 5")

jmlh_padi = []
jmlh_kedelai = []

for a in Data_panen.values():
    jmlh_padi.append(a['hasil_panen']['padi'])
    jmlh_kedelai.append(a['hasil_panen']['kedelai'])

total1 = sum(jmlh_padi)
total2 = sum(jmlh_kedelai)
print(f"Jumlah Seluruh Padi dari semua Lokasi = {total1}\nJumlah Seluruh Kedelai dari semua lokasi = {total2}")

print('No 6')
for tempat,data in Data_panen.items(): 
    nama_tempat = data['nama_lokasi']
    hasil_padi = data['hasil_panen']['padi']
    hasil_jagung = data['hasil_panen']['jagung']

    if hasil_padi > 1300 or hasil_jagung > 800:
        print(f"Lokasi {nama_tempat} Membutuhkan Perhatian Khusus")
    else:
        print(f"Lokasi {nama_tempat} Dalam Kondisi Normal Dan Aman ")