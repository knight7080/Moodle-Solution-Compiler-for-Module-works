from Test1 import module_fetch
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
import time

j_mod = ["TT JAVA MODULE-I","TT JAVA MODULE-II","TT JAVA MODULE-III","TT JAVA MODULE-IV","TT JAVA MODULE-V","TT JAVA MODULE-VI","TT JAVA MODULE-VII","TT JAVA MODULE-VIII","TT JAVA MODULE-IX","TT JAVA MODULE-X","TT JAVA MODULE-XI","TT JAVA MODULE-XII"]
c_mod = ["TT Module - I","TT Module - II","TT Module - III","TT Module - IV","TT Module - V","TT Module - VI","TT Module - VII","TT Module - VIII","TT Module - IX","TT Module - X","TT Module - XI","TT Module - XII"]
cpp_mod = ["TT DS CPP MODULE-I","TT DS CPP MODULE-II","TT DS CPP MODULE-III","TT DS CPP MODULE-IV","TT DS CPP MODULE-V","TT DS CPP MODULE-VI","TT DS CPP MODULE-VII","TT DS CPP MODULE-VIII","TT DS CPP MODULE-IX","TT DS CPP MODULE-X","TT DS CPP MODULE-XI","TT DS CPP MODULE-XII"]
daa_mod = ["TT DS PYTHON MODULE-19", "TT DS PYTHON MODULE-20","TT DS PYTHON MODULE-21 ","TT DS PYTHON MODULE-22","TT DS PYTHON MODULE-23","TT DS PYTHON MODULE-24"]

lang = input()

if lang == "Java":
    curr = j_mod
elif lang == "C":
    curr = c_mod
elif lang == "Cpp":
    curr = cpp_mod
elif lang == "Daa":
    curr = daa_mod
else:
    print("Doesnt exist")

chrome_options = Options()
# chrome_options.add_argument('--headless')
# // run this for executing in the backend without a visible window

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

driver.get("http://training.saveetha.in/login/index.php")

rno = "21000045"
pas = "t65363"
u_btn = driver.find_element(By.NAME, "username")
u_btn.send_keys(rno)
p_btn = driver.find_element(By.NAME, "password")
p_btn.send_keys(pas)
time.sleep(4)
driver.find_element(By.ID, "loginbtn").click()
time.sleep(10)

for i in range(0,len(curr)):
    module_fetch(curr[i], lang, lang+str(i), driver)

time.sleep(2)
driver.close()
driver.quit()