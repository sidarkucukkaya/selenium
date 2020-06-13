from selenium import webdriver
import time
import random

browser = webdriver.Firefox(executable_path="C:\\Users\\kucuk\\Downloads\\geckodriver-v0.26.0-win64\\geckodriver.exe")  # geckodriver.exe'nin yolunu vermemiz lazım
url = "https://eksisozluk.com/python-programlama-dili--6303607?p="

"""url = "https://eksisozluk.com/python-programlama-dili--6303607" # Gitmek istediğimiz url
browser.get(url)    # Bunu yaptığımız zaman bizim web sayfamız sanal browser'ımıza açılacak
time.sleep(5)   #FireFox 5 saniye bekledikten sonra kapanacak
elements = browser.find_elements_by_css_selector(".content")   # bu metod ile class content olanları alacağız.
for element in elements:
    print("-----------------------------------------")
    print(element.text)"""

# Rastgele sayfalardan rastgele entry çekmek
pageCount = 1
entry = []
entryCount = 1
while pageCount <= 10:  # Bu döngüyle 10 farklı sayfaya gidiyoruz
    randomPage = random.randint(1,132)  # 1 ile 132. sayfalar arasında
    newUrl = url + str(randomPage)  # url'mizin sonuna sayfa numarasını ekledik
    browser.get(newUrl) # Yeni url'mizi çalıştırdık
    elements = browser.find_elements_by_css_selector(".content")    # class'ı content olanları çektik
    for element in elements:
        entry.append(element.text)
    time.sleep(1)   # Her sayfada 1 saniye bekleme işlemi
    pageCount += 1

"""for ent in entry:   # entry'leri yazdırma
    print("*********************************************")
    print(ent)"""

# Alınan entry'leri dosyaya yazmak
with open("entry.txt","w",encoding="UTF-8") as file:
    for ent in entry:
        file.write(str(entryCount) + ".\n" + ent + "\n")
        entryCount += 1

browser.close()


