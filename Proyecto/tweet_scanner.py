import tweepy	#importando las librerias necesarias
import os
import time
import pandas as pd
import csv
from textblob import TextBlob
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
#Elimina los archivos para evitar problemas con informacion atrasada
a = "Separado.txt"
if os.path.isfile(a):
    os.remove(a)
b = "Archivo.txt"
if os.path.isfile(b):
    os.remove(b)
c = "Tweets.txt"
if os.path.isfile(c):
    os.remove(c)
#Crea desde 0 los archivos para garantizar que estan en blanco
open('Tweets.txt', 'w+').close()
open('Archivo.txt', 'w+').close()
open('Separado.txt', 'w+').close()

start_time = time.time()#Se toma el tiempo para observar cuanto tarda el tiempo de ejecucion
listaC = []#Se crea una lista donde guardar los datos de los tweets 
consumer_key = 'okhTYnzNURavmFohKkTomG7cK'#informacion del 'bot' necesaria para que corra el programa
consumer_secret = 'wOn2vK5PLI9zNQjWuQ09KlrN5lXy3amAeqZcjT4JAgWJG2bFLy'

access_token = '403824956-G709hWOrAdn2CQQYQNnCMHCg2S2SZGck7cIJQyMn'
access_token_secret = 'xlg2394YmBlxpVIEbwq8cyZKnKqsBBK1wMEiZazVUtLj5'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
#Creacion de la clase STDOutListener
class StdOutListener(StreamListener):
    def __init__(self, api=None):
        super(StdOutListener, self).__init__()
        self.num_tweets = 0

    def on_data(self, data):
        self.num_tweets += 1
        if self.num_tweets < 20: #Un numero pequeño de tweets para probar el programa
        	try:
        		with open('Archivo.txt', 'w') as f:
        			f.write(data + '\n')
        	except BaseException as e:
        		print("No se pudo guardar ese tweet al Archivo")
        	return True
        else:
            return False

    def on_error(self, status):
        print (status)


l = StdOutListener()
try:
	file = open("Archivo.txt","r")#Se intenta leer el archivo para obtener la informacion
	listaC = file.read()
except BaseException as e:
	print("No se ha podido acceder al archivo")
stream = Stream(auth, l)
stream.filter(locations = [-99.3573,19.1322,-98.9433,19.5927] ) #Cuadro de localizacion de México 


ASeparar = listaC #Se separa la informacion util de los tweets de la innecesaria
x = 0
for i in ASeparar:
	ASeparar3 = ASeparar
	Alfa = ASeparar3.find("\",\"text\":")
	Omega = ASeparar3.find("\"source\":")
	intermedio = ASeparar[Alfa:Omega]
	if intermedio.find("\"display_text_range\":") > 0:
		comenzar = ASeparar.find(",\"text\"")
		x = x + 1
		ASeparar2 = ASeparar[comenzar:]
		ASeparar = ASeparar2
		final = ASeparar2.find(",\"display_text_range\"")
		texto = ASeparar2[:final]
		comenzar = ASeparar.find("\"screen_name\"")
		ASeparar2 = ASeparar[comenzar:]
		ASeparar = ASeparar2
		final = ASeparar2.find(",\"location\"")
		usuario = ASeparar2[:final]
		tweet = usuario + "|" + texto
		tweet = tweet.replace("\"screen_name\":", "Usuario: ")
		tweet = tweet.replace("\"text\":", "Tweet: ")
		try:
			with open('Separado.txt', 'a') as f:
				f.write(str(x) + ' ) ' + tweet + '\n')
		except BaseException as e:
			print("No se ha podido acceder al archivo")
	else:
		if intermedio.find("\"indices\":") > 0:
			comenzar = ASeparar.find("\"text\"")
			x = x + 1
			ASeparar2 = ASeparar[comenzar:]
			ASeparar = ASeparar2
			final = ASeparar2.find(",\"display_text_range\"")
			texto = ASeparar2[:final]
			comenzar = ASeparar.find("\"screen_name\"")
			ASeparar2 = ASeparar[comenzar:]
			ASeparar = ASeparar2
			final = ASeparar2.find(",\"location\"")
			usuario = ASeparar2[:final]
			tweet = usuario + "|" + texto
			tweet = tweet.replace("\"screen_name\":", "Usuario: ")
			tweet = tweet.replace("\"text\":", "Tweet: ")
			try:
				with open('Separado.txt', 'a') as f:
					f.write(data + '\n')
			except BaseException as e:
				print("No se ha podido acceder al archivo")
		else:
			ASeparar = ASeparar[Omega:]

#Se crean dos listas que son necesarias para el proceso de garantizar que no haya tweets repetidos
listA = []
listB = []
textoABuscar = 'banco prestamo dinero'
lista = textoABuscar.split()




api = tweepy.API(auth)
for X in lista:
	for Z in range(0,1):
			try:
				public_tweets = api.search(X)
				for tweet in public_tweets:
					if ('RT @' not in tweet.text):
						listA.append(tweet.text)
			except BaseException as e:
				print("Error on_data: %s" % str(e))
				continue
for key in listA:
	if key not in listB:
		listB.append(key)
	
print("--- %s seconds ---" % (time.time() - start_time))

for key in listB:
	print(key + '\n')
	try:
				with open('Tweets.txt', 'a') as f:
					f.write(key + '\n')
	except BaseException as e:
		print("No se ha podido acceder al archivo")
	