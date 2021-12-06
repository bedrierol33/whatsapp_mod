import time
from selenium import webdriver
import threading
import app
global browser
global tarayici
browser = webdriver.Chrome()
tarayici = browser.get('https://bedrierol33.tr.gg/')
app.f1()
