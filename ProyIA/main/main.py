from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from wordcloud import WordCloud
from bs4 import BeautifulSoup
import os 
import requests
import PyPDF2
import nltk
import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET
import re
nltk.download('stopwords')
nltk.download('punkt')

#Configuración del servidor de Grobid
grobid_url = "http://grobid:8070/api/processFulltextDocument"
#Directorio que contiene los PDFs a enviar
pdf_dir = "../Resources"
#Lista de palabras vacías en ingles
stop_words = set(stopwords.words("english"))
#Diccionario de frecuencia de palabras en los resumenes
word_freq = {}
#Diccionario de figuras
figure_freq = {}
#Diccionario de links
links = {}

for filename in os.listdir(pdf_dir):
    if filename.endswith(".pdf"):
        pdf_path = os.path.join(pdf_dir, filename)
        with open(pdf_path,"rb") as pdf_file:
            response = requests.post(grobid_url, files={"input": pdf_file}, data= {"output": "text", "consolidateCitations": "true"})
            summary = response.text
            root = ET.fromstring(summary)
#NUMERO DE IMÁGENES--------------------------------------------------------------------------------
            figure_freq[filename] = 0
            for elem in root.iter():
                if 'figure' in elem.tag:
                    figure_freq[filename] += 1
#---------------------------------------------------------------------------------------------------
#NUBE DE KEYWORDS-----------------------------------------------------------------------------------
            soup = BeautifulSoup(summary)
            xml_test = soup.get_text()
            tokens = word_tokenize(xml_test.lower())
            tokens = [token for token in tokens if token.isalpha() and token not in stop_words]
            for token in tokens:
                if token in word_freq:
                    word_freq[token] += 1
                else:
                    word_freq[token] = 1
#---------------------------------------------------------------------------------------------------

if len(os.listdir("../Resources/figures")) > 1:
    os.remove("../Resources/figures/wordcloud.png")
    os.remove("../Resources/figures/num_images.png")

wordcloud = WordCloud(width=800, height=800, background_color="white").generate_from_frequencies(word_freq)
plt.figure(figsize=(8, 8))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.savefig('../Resources/figures/wordcloud.png')

plt.clf()

plt.figure(figsize=(12, 12))
x = list(figure_freq.keys())
y = list(figure_freq.values())
plt.bar(x, y)
plt.xticks(rotation=90)
plt.ylabel("Numero de figuras")
plt.savefig('../Resources/figures/num_images.png')