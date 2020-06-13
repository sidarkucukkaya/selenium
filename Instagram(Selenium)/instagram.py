from selenium import webdriver
import time

browser = webdriver.Firefox(executable_path="C:\\Users\\kucuk\\Downloads\\geckodriver-v0.26.0-win64\\geckodriver.exe")  # geckodriver.exe'nin yolunu vermemiz lazım
url = "https://www.instagram.com/"
browser.get(url)

time.sleep(1)

username = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input')
password = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input')

username = browser.find_element_by_name("username")
password = browser.find_element_by_name("password")

username.send_keys("myusername")
password.send_keys("mypassword")

girisYap = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]')
girisYap.click()

time.sleep(5)

bilgileriKaydet = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/section/div/button')
bilgileriKaydet.click()

time.sleep(5)

bildirimleriAc = browser.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
bildirimleriAc.click()

time.sleep(5)

myProfile = browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/a/img')
myProfile.click()

time.sleep(5)

myFollowers = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
myFollowers.click()

jsCommand = """
followers = document.querySelector("body > div.RnEpo.Yx5HN");
followers.scrollTo(0,followers.scrollHeight);
var lenOfPage = followers.scrollHeight;
return lenOfPage;
"""

lenOfPage = browser.execute_script(jsCommand)
match = False
while match == False:
    lastCount = lenOfPage
    time.sleep(5)
    lenOfPage = browser.execute_script(jsCommand)
    if lastCount == lenOfPage:
        match = True

time.sleep(5)

followersList = []
followersName = browser.find_elements_by_css_selector(".FPmhX.notranslate._0imsa ")
for follower in followersName:
    followersList.append(follower.text)

with open("followers.txt","w",encoding="UTF-8") as file:
    for follower in followersList:
        file.write(follower + "\n")

time.sleep(5)

browser.close()

