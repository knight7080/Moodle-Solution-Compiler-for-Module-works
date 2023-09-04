from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from fpdf import FPDF

import pdfkit


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://training.saveetha.in/login/index.php")

rno = "21003975"
pas = "h85153"
u_btn = driver.find_element(By.NAME,"username")
u_btn.send_keys(rno)
p_btn = driver.find_element(By.NAME,"password")
p_btn.send_keys(pas)
time.sleep(4)
driver.find_element(By.ID,"loginbtn").click()
time.sleep(10)

driver.find_element(By.XPATH,"//span[contains(.,'TT JAVA MODULE-VII')]").click()

mods = driver.find_elements(By.XPATH,"//li[@class='activity quiz modtype_quiz ']")

m = mods[0].find_elements(By.CLASS_NAME,"instancename")

cont = len(m)
m[0].click()

try:
    atmpt = driver.find_element(By.XPATH, "//tr[@class = 'bestrow lastrow']")

    atmpt.find_element(By.TAG_NAME, "a").click()

except:
    atmpt = driver.find_element(By.XPATH, "//tr[@class = 'lastrow']")

    atmpt.find_element(By.TAG_NAME, "a").click()


page = driver.page_source.encode('utf-8')

file = open('result.html','wb')

file.write(page)

file.close()

config = pdfkit.configuration(wkhtmltopdf="C:\Program Files\wkhtmltopdf\\bin\wkhtmltopdf.exe")

pdfkit.from_file('result.html', 'output.pdf', configuration = config)

driver.back()

time.sleep(2)

driver.back()

time.sleep(2)
driver.close()
driver.quit()