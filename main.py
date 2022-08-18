# coding=utf-8

def retweet():
    print("retweet")

def usuarios():
    print("usuarios")

def dias():
    print("dias")

def hashtags():
    print("hashtags")


def main():
    print("Bienvenido")
    print("Qué funcion deseas utilizar:")
    print("1. Los top 10 tweets más retweeted.")
    print("2. Los top 10 usuarios en función de la cantidad de tweets que emitieron.")
    print("3. Los top 10 días donde hay más tweets.")
    print("4. Los top 10 hashtags más usados.")

    resp = input("ingresa una opción:")
    print("Opción: " + str(resp))
    if (resp == 1):
        retweet()
    elif (resp == 2):
        usuarios()
    elif (resp == 3):
        dias()
    elif(resp == 4):
        hashtags()


main()




import pandas as pd
from pandas.io.json import json_normalize
import warnings
warnings.filterwarnings("ignore")
raw_tweets = pd.read_json(r'../input/farmers-protest-tweets-dataset-raw-json/farmers-protest-tweets-2021-2-4.json', lines=True)
raw_tweets = raw_tweets[raw_tweets['lang']=='en']
print("Shape: ", raw_tweets.shape)
raw_tweets.head(5)