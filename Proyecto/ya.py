import tweepy
import time
import pandas as pd
import json
import csv
from textblob import TextBlob
file = open("Archivo.txt","r")
ASeparar = file.read()
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
			print("NEl joven, el lunes sin falta carnal")
		print(str(x) + ' ) ' + tweet + '\n')
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
				print(str(x) + ' ) ' + tweet + '\n')
			print(str(x) + ' ) ' + tweet + '\n')
		else:
			ASeparar = ASeparar[Omega:]