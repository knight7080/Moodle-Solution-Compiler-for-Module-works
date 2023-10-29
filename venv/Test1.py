from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import time
import merger
from fpdf import FPDF
from selenium.webdriver.chrome.options import Options
import pdfkit

chrome_options = Options()
chrome_options.add_argument('--headless')

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

driver.get("http://training.saveetha.in/login/index.php")

rno = "21003975"
pas = "h85153"
mod_name = "TT JAVA MODULE-VI"
u_btn = driver.find_element(By.NAME,"username")
u_btn.send_keys(rno)
p_btn = driver.find_element(By.NAME,"password")
p_btn.send_keys(pas)
time.sleep(4)
driver.find_element(By.ID,"loginbtn").click()
time.sleep(10)

driver.get("http://training.saveetha.in/?redirect=0")

driver.find_element(By.XPATH,"//a[text()='" + mod_name + "']").click()

quant = driver.find_elements(By.XPATH, "//li[@class='activity quiz modtype_quiz ']")

l = len(quant)

for j in range(l):
        mods = driver.find_elements(By.XPATH, "//li[@class='activity quiz modtype_quiz ']")

        try:
            m = mods[j].find_elements(By.CLASS_NAME, "instancename")
            m[0].click()
            try:
                atmpt = driver.find_element(By.XPATH, "//tr[@class = 'bestrow lastrow']")

                atmpt.find_element(By.TAG_NAME, "a").click()

            except:
                atmpt = driver.find_element(By.XPATH, "//tr[@class = 'lastrow']")

                atmpt.find_element(By.TAG_NAME, "a").click()

            page = driver.page_source.encode('utf-8')

            # res = "result" + str(j) + ".html"

            file = open('result.html', 'wb')

            file.write(page)

            file.close()

            op_file = r'C:\Users\kaushik\PycharmProjects\moodle_doc\venv\output' + str(j) + '.pdf'

            pdfkit.from_file(r'C:\Users\kaushik\PycharmProjects\moodle_doc\venv\result.html', op_file,
                             options={"enable-local-file-access": ""}, verbose=True)
        except:
            driver.back()
            continue
        time.sleep(4)

        driver.back()

        time.sleep(4)

        driver.back()

merger.merge_pdfs(l,mod_name)

time.sleep(2)
driver.close()
driver.quit()