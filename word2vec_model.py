import gensim
import pandas as pd
from nltk.tokenize import word_tokenize

df = pd.read_csv("news_corpus.csv",usecols=['cumle_icerigi'])

all_words = []
for sent in df["cumle_icerigi"]:
    all_words.append(word_tokenize(sent))    

model = gensim.models.Word2Vec(all_words, size=100)


similarity_dolar = model.most_similar("dolar", topn=5)
print("Dolar kelimesi için benzerlik ölçümü: \n",similarity_dolar,"\n")

similarity_insan = model.most_similar("insan", topn=5)
print("İnsan kelimesi için benzerlik ölçümü: \n",similarity_insan,"\n")

similarity_kovid = model.most_similar("kovid", topn=5)
print("Kovid kelimesi için benzerlik ölçümü: \n",similarity_kovid,"\n")

similarity_uzay = model.most_similar("uzay", topn=5)
print("Uzay kelimesi için benzerlik ölçümü: \n",similarity_uzay,"\n")

similarity_beyin = model.most_similar("beyin", topn=5)
print("Beyin kelimesi için benzerlik ölçümü: \n",similarity_beyin,"\n")
