from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = 'https://www.getmyboat.com/bridge/threads/2196354'
url2 = 'https://accounts.google.com/signin/v2/identifier?flowName=GlifWebSignIn&flowEntry=ServiceLogin'
browser = webdriver.Chrome()

browser.get(url)


_name = browser.find_element_by_xpath('//*[@id="email"]')
_name.send_keys('carlos.paz@getmyboat.com')

_pass = browser.find_element_by_xpath('//*[@id="password"]')
_pass.send_keys('Maxine2020')

_pass.send_keys(Keys.RETURN)   #se loguea en el primero


#LOGIN DE GMAIL
_gmail_name = browser.find_element_by_xpath('//*[@id="identifierId"]').send_keys('carlos.paz@getmyboat.com')
#_gmail_name.send_keys()
"""
_gmail_pass = browser.find_element_by_xpath('')
_gmail_pass.send_keys('Maxine2020')
"""
_gmail_name.send_keys(Keys.RETURN)  