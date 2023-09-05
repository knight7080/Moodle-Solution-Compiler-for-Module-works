from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import time
import merger
from fpdf import FPDF

import pdfkit


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://training.saveetha.in/login/index.php")

rno = "21000045"
pas = "t65363"
mod_name = "TT JAVA MODULE-VI"
u_btn = driver.find_element(By.NAME,"username")
u_btn.send_keys(rno)
p_btn = driver.find_element(By.NAME,"password")
p_btn.send_keys(pas)
time.sleep(4)
driver.find_element(By.ID,"loginbtn").click()
time.sleep(10)

driver.find_element(By.XPATH,"//span[contains(.,'TT JAVA MODULE-VII')]").click()

quant = driver.find_elements(By.XPATH, "//li[@class='activity quiz modtype_quiz ']")

l = len(quant)

for j in range(l):
        mods = driver.find_elements(By.XPATH, "//li[@class='activity quiz modtype_quiz ']")
        m = mods[j].find_elements(By.CLASS_NAME, "instancename")
        m[0].click()

        try:
            atmpt = driver.find_element(By.XPATH, "//tr[@class = 'bestrow lastrow']")

            atmpt.find_element(By.TAG_NAME, "a").click()

        except:
            atmpt = driver.find_element(By.XPATH, "//tr[@class = 'lastrow']")

            atmpt.find_element(By.TAG_NAME, "a").click()

        page = driver.page_source.encode('utf-8')

        file = open('result.html', 'wb')

        file.write(page)

        file.close()

        config = pdfkit.configuration(wkhtmltopdf="C:\Program Files\wkhtmltopdf\\bin\wkhtmltopdf.exe")

        op_file = 'output' + str(j)  + '.pdf'

        pdfkit.from_file('result.html', op_file , configuration=config)

        time.sleep(2)

        driver.back()

        time.sleep(2)

        driver.back()

merger.merge_pdfs(l,mod_name)

time.sleep(2)
driver.close()
driver.quit()