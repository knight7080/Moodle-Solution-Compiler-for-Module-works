from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

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
time.sleep(6)

t = driver.find_element(By.XPATH,"//div[@class='card-deck dashboard-card-deck ']")
l = t.find_elements(By.XPATH,"./child::*")

q = l[1]
m = q.find_element(By.XPATH,"//a[@class='aalink coursename mr-2']")
pp = m.find_elements(By.XPATH,"./child::*")

print(pp[2].get_attribute("innerHTML"))

time.sleep(2)
driver.close()
driver.quit()