import pandas as pd
import sqlite3
import re
from geopy.geocoders import ArcGIS
import folium


#Exel Twitlerini projeye tanıtma pandas ile veritabanına kayıt etme

FilePath = 'C:\\Users\\fatih\\PycharmProjects\\Twitter\\Veri\\twitter.xlsx'
df = pd.read_excel(FilePath, sheet_name="Edges", index_col=None, usecols=[0])
conn = sqlite3.connect('C:\\Users\\fatih\\PycharmProjects\\Twitter\\Veri\\tweeter.db')

df.to_sql("İsimler", conn, if_exists='append', index=False)
cursor = conn.cursor()
cursor.execute("SELECT * FROM İsimler")
veri = cursor.fetchall()

df = pd.read_excel(FilePath, sheet_name="Edges", index_col=None, usecols=[4])
df.to_sql("Tweetler", conn, if_exists='append', index=False)
cursor.execute("SELECT * FROM Tweetler")
twet = cursor.fetchall()
x = len(twet)

df = pd.read_excel(FilePath, sheet_name="Edges", index_col=None, usecols=[10])
df.to_sql("Lokasyon1", conn, if_exists='append', index=False)
cursor.execute("SELECT * FROM Lokasyon1")
lokaysoyon1 = cursor.fetchall()

df = pd.read_excel(FilePath, sheet_name="Edges", index_col=None, usecols=[11])
df.to_sql("Lokasyon2", conn, if_exists='append', index=False)
cursor.execute("SELECT * FROM Lokasyon2")
lokaysoyon2 = cursor.fetchall()

#twitlerdeki gereksiz ifadeleri temizleme

for i in range(x):
    if i>0:
     metin = " ".join(map(str, twet[i]))
     ara="@"
     ara1="RT"
     ara2="#"
     ara3="/"
     ara4="https"
     ara5=":"
     ara6="//"
     ara7="'.'"
     ara8="_"
     ara9="="


     ydeger=""

     sonuc   = re.sub(ara,ydeger,   metin)
     sonuc1  = re.sub(ara1,ydeger,  sonuc)
     sonuc2  = re.sub(ara2,ydeger,  sonuc1)
     sonuc3 = re.sub(ara3,ydeger,  sonuc2)
     sonuc4  = re.sub(ara4,ydeger,  sonuc3)
     sonuc5  = re.sub(ara5, ydeger, sonuc4)
     sonuc6 = re.sub(ara7, ydeger, sonuc5)
     sonuc7= re.sub(ara7, ydeger, sonuc6)
     sonuc8 = re.sub(ara8, ydeger, sonuc7)
     twet[i] = re.sub(ara9, ydeger, sonuc8)
     metin = ""


#atılan twitte kaç adet kelime oldugunu hesaplama

bosluk_sayac=0
kelime_sayisi=0




for i in range(x):
  if i>0:
   metin = " ".join(map(str, veri[i]))
   for i in twet[i]:
    if i == " ":
     bosluk_sayac +=1
   kelime_sayisi=bosluk_sayac+1
   print(metin, "'in kullandığı kelime sayisi =", kelime_sayisi)


   bosluk_sayac = 0
   kelime_sayisi = 0
   metin=""

print("\n")


#Her harften kaçar adet kullanıldıgını hesaplama



for i in range(x):
 if i > 0:
  wordcount = {}
  metin = " ".join(map(str, twet[i]))
  kelime = metin.split()
  print(veri[i])
  for word in metin.split():
   if word not in wordcount:
    wordcount[word] = 1
   else:
    wordcount[word] += 1
  for key in wordcount.keys():

   print("%s %s " % (key, wordcount[key]))
  wordcount = {}
  metin = {}
  print("\n")

print("\n")
for i in range(x) :
 if i>0 :
  print(veri[i],"in twiti = ",twet[i])


print("\n")

center=(15.176912, 76.662933)
map_colony=folium.Map(location=center,zoom_start=8)

for i in range(x) :
 if i >0:
  metin = " ".join(map(str, lokaysoyon1[i]))
  nom = ArcGIS()
  s = nom.geocode(metin)
  a=s.latitude
  b=s.longitude
  print(a,b)
  location=[a,b]
  folium.Marker(location,popup=lokaysoyon1[i],tooltip="Click for more ").add_to(map_colony)


map_colony.save("harita.html")

print("\n")


allWords={}
for i in range(x):
 if i>0:
  metin = " ".join(map(str, lokaysoyon1[i]))
  splitWord = metin.split()
  for word in splitWord:
    if word not in allWords:
        allWords[word] = 1
    else:
        allWords[word] += 1
 metin=""
for key in allWords.keys():
   print ("Şehirler: %s =>%s " %(key , allWords[key]))












