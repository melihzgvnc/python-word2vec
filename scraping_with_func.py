import requests
from bs4 import BeautifulSoup
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import re
import csv

def ready_for_csv(news_url):
    
    news_without_soup = requests.get(news_url)
    soup_news = BeautifulSoup(news_without_soup.content, "html.parser")
    news_p = soup_news.find_all("p")    
    
    news_all_text = ""
    for i in range(1,len(news_p)):
        news_all_text += (news_p[i].get_text())  
    
    #delete stopwords
    news_without_stopwords = ""
    stop_words = stopwords.words('turkish')
    for word in word_tokenize(news_all_text):
        if word not in stop_words:            
            news_without_stopwords += (" "+word)
    
    #data cleaning      
    tokenized_news = sent_tokenize(news_without_stopwords)
    cleaned_news = []
    for sent in range(len(tokenized_news)):
        temp = re.sub("\W+"," ",tokenized_news[sent])    
        temp = re.sub("[0-9]+"," ",temp)
        temp = re.sub("\s\w\s", " ", temp)
        temp = re.sub("^\s", "", temp)
        temp = re.sub("\s$", "", temp)
        temp = re.sub("\s+"," ",temp)
        tokenized_news[sent] = temp
        
        cleaned_news.append(tokenized_news[sent].lower())    
        
    #create a list that includes 'url', 'segment_no', 'cümle_metni', 'kelime_sayısı' as elements     
    list_for_csv = []
    for sent in cleaned_news:
        temp_list = [news_url]
        segment_no = cleaned_news.index(sent)
        word_count = len(word_tokenize(sent))
        temp_list.append(segment_no)
        temp_list.append(sent)
        temp_list.append(word_count)
        list_for_csv.append(temp_list) 

    return list_for_csv


def write_CSV(list_for_csv):
    
    with open('news_corpus.csv', 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['url', 'segment_no', 'cumle_icerigi', 'sozcuk_sayisi']
        #add column_names
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        
        writer = csv.writer(f)
        writer.writerows(list_for_csv)
      

#---------------------------------------------------------

    
csv_list = []

url1 = "https://www.indyturkish.com/node/171756/haber/koronavirüs-salgını-kitap-sektörünü-nasıl-etkiledi-evde-kalanlar-kitap-okuyor-mu"
csv_list += ready_for_csv(url1)

url2 = "https://www.indyturkish.com/node/171836/kültür/devrim-marc-chagall’ın-gözünde-bir-felaket-olduğu-vakit"
csv_list += ready_for_csv(url2)

url3 = "https://www.indyturkish.com/node/171841/bilim/bilim-insanlarından-çığır-açan-dinozor-keşfi-spinosaurusların-yüzdüğü-kanıtlandı"
csv_list += ready_for_csv(url3)

url4 = "https://www.indyturkish.com/node/171366/bilim/hubble-uzay-teleskopu-atlas-kuyrukluyıldızının-parçalandığı-anı-görüntüledi"
csv_list += ready_for_csv(url4)

url5 = "https://www.indyturkish.com/node/169511/bilim/britanyalı-nörobilimcilerin-yeni-keşfi-insan-beynindeki-dil-yetisinin-kökeni-en-az"
csv_list += ready_for_csv(url5)

url6 = "https://www.indyturkish.com/node/171731/yaşam/dev-tur-gemileri-onlara-hapis-oldu-100-bini-aşkın-tayfa-denizde-hâlâ-mahsur"
csv_list += ready_for_csv(url6)

url7 = "https://www.indyturkish.com/node/172266/dünya/zaman-tükeniyor-abd-hapishanelerindeki-kovid-19-pozitif-vakaların-sayısı-alarm"
csv_list += ready_for_csv(url7)

url8 = "https://www.indyturkish.com/node/171656/ekonomi̇/doların-699’da-kalıp-7-liraya-çıkmaması-için-“kur-savunması”-yapılıp"
csv_list += ready_for_csv(url8)

url9 = "https://www.indyturkish.com/node/172166/spor/ergin-atamandan-shane-larkin-açıklaması-nba-opsiyonu-var-iyi-bir-takım-bulursa"
csv_list += ready_for_csv(url9)

url10 = "https://www.indyturkish.com/node/172111/haber/karantina-sürecinin-ardından-yurtlarda-duygu-yüklü-mektuplar-kaldı"
csv_list += ready_for_csv(url10)

url11 = "https://www.indyturkish.com/node/171026/siyaset/akşener-merkez-bankasının-yedek-akçeleri-gitmiş-geçilmeyen-yollara-inilmeyen"
csv_list += ready_for_csv(url11)

url12 = "https://www.indyturkish.com/node/172036/haber/uzaktan-eğitimin-merak-edilen-yönleri-televizyonu-bilgisayarı-olmayan-çocukların"
csv_list += ready_for_csv(url12)

url13 = "https://www.indyturkish.com/node/171666/sağlik/türkiyede-salgınla-en-önde-mücadele-eden-doktorlar-anlattı-dışarıya-karşı"
csv_list += ready_for_csv(url13)
 
write_CSV(csv_list)
