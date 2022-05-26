
import pandas as pd
import sqlite3
from textblob import TextBlob
import boto3


FilePath = 'C:\\Users\\fatih\\PycharmProjects\\Twitter\\Veri\\twitter.xlsx'
df = pd.read_excel(FilePath, sheet_name="Edges", index_col=None, usecols=[0])

conn = sqlite3.connect('C:\\Users\\fatih\\PycharmProjects\\Twitter\\Veri\\tweeter.db')
df.to_sql("İsimler", conn, if_exists='append', index=False)

cursor = conn.cursor()

cursor.execute("SELECT * FROM İsimler")

veri =cursor.fetchall()

df = pd.read_excel(FilePath, sheet_name="Edges", index_col=None, usecols=[4])
df.to_sql("Tweetler", conn, if_exists='append', index=False)
cursor.execute("SELECT * FROM Tweetler")
twet = cursor.fetchall()
x = len(twet)




def duygu_bul(cumle_turkce,ceviri,dil_isleyici):
    ceviri_sonuc=ceviri.translate_text(Text=cumle_turkce,SourceLanguageCode="tr", TargetLanguageCode="en")
    cevrilmis_cumle = ceviri_sonuc['TranslatedText']
    duygu_sonucu = dil_isleyici.dectect.sentiment(
        Text = cevrilmis_cumle,
        LanguageCode ='en'
    )
    return duygu_sonucu




def duygu_sonucu_gorsellestir(duygu_sonucu):
    pozitif_duygu_skoru = duygu_sonucu['SentimentScore']['Positive']
    negatif_duygu_skoru = duygu_sonucu['SentimentScore']['Negative']
    notr_duygu_skoru    = duygu_sonucu['SentimentScore']['Neutral']

    duygu =""

    if duygu_sonucu['Sentiment']=="POSITIVE":
        duygu="iyi :)"
    elif duygu_sonucu['Sentiment']=="NEGATIVE":
        duygu="kotu :("

    print("\n")
    print("Muhtemelen {} birsey soyledin".format(duygu))
    print('Pozitif Skor : {}'.format(pozitif_duygu_skoru))
    print('Negatif Skor : {}'.format(negatif_duygu_skoru))



ceviri = boto3.client(service_name='translate')
dil_isleyici = boto3.client(service_name='comprehend')

cumle_turkce =twet[1]
duygu_sonucu =duygu_bul(cumle_turkce, ceviri ,dil_isleyici)
duygu_sonucu_gorsellestir(duygu_sonucu)



//////////////////////////////////
k=0
a={}

for i in range(x):
 if i>0:
  for j in range(x):
   if j>0:
    if lokaysoyon1[i]==lokaysoyon1[j]:



     k+=1
 a[i]=k
 k=0







y=len(a)

for p in range(y):
 if p>0 :
  print(a[p])


















