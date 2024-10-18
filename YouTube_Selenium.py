
# pip install Selenium 
import selenium
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
from selenium.webdriver.chrome.options import Options


# List of Chappell Roan -Artist- urls to scrape comments from:
url1 = 'https://www.youtube.com/watch?v=vL92xyS0IEM'
url2 = 'https://www.youtube.com/watch?v=uMshgHF9Gso'
url3 = 'https://www.youtube.com/watch?v=w4WiXKGCJhg'
url4 = 'https://www.youtube.com/watch?v=Ifq4_6FJdZA'
url5 = 'https://www.youtube.com/watch?v=-74g4LM1hCU'

# List of The Row -Fashion- urls to scrape comments from:
TR_url1 = 'https://www.youtube.com/watch?v=SaVSo9L55g8'
TR_url2 = 'https://www.youtube.com/watch?v=WelntXT22X8'
TR_url3 = 'https://www.youtube.com/watch?v=qds1Bx06sDs'
TR_url4 = 'https://www.youtube.com/watch?v=VeOzDX0Gz8w'
TR_url5 = 'https://www.youtube.com/watch?v=BgpWTk5RDq4'
TR_url6 = 'https://www.youtube.com/watch?v=K-9F26lB4ac'
TR_url7 = 'https://www.youtube.com/watch?v=RlSbm8dJcac'

# List of OpenAI -tech- urls to scrape comments from:
OAI_url1 = 'https://www.youtube.com/watch?v=acPbO2yCeDE'
OAI_url2 = 'https://www.youtube.com/watch?v=SbrfjBV8EzM'
OAI_url3 = 'https://www.youtube.com/watch?v=2mbM1wHwQhk'
OAI_url4 = 'https://www.youtube.com/watch?v=p3LKeKo4MMM' 
OAI_url5 = 'https://www.youtube.com/watch?v=vYjHMkVEIR4'
OAI_url6 = 'https://www.youtube.com/watch?v=CpwlKDCdfq4'

 

# Run the scrape for the first CR url:
data1 = []

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

path = webdriver.Chrome(options=options)
service = Service(executable_path=path)


path.get(url1)
path.maximize_window()

with path as driver:
    wait = WebDriverWait(driver, 120)
    driver.get(url1)
    driver.maximize_window()
    
    for item in range(6): # how many scrolls down the page
        wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.END)
        time.sleep(10)
    for comment in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#comment #content-text"))):
        data1.append(comment.text)


print(data1)

tf1 = data1
with open('/Users/kdr/Documents/AmazonInfo/text_files/CR_YT_1.txt', 'w') as f:
    f.writelines(tf1)



# Run the scrape for the second CR url:
data2 = []

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

path = webdriver.Chrome(options=options)
service = Service(executable_path=path)


path.get(url2)
path.maximize_window()

with path as driver:
    wait = WebDriverWait(driver, 120)
    driver.get(url2)
    driver.maximize_window()
    
    for item in range(6):
        wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.END)
        time.sleep(5)
    for comment in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#comment #content-text"))):
        data2.append(comment.text)


print(data2)

tf2 = data2
with open('/Users/kdr/Documents/AmazonInfo/text_files/CR_YT_2.txt', 'w') as f:
    f.writelines(tf2)


# Run the scrape for the third CR url:
data3 = []

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

path = webdriver.Chrome(options=options)
service = Service(executable_path=path)


path.get(url3)
path.maximize_window()

with path as driver:
    wait = WebDriverWait(driver, 120)
    driver.get(url3)
    driver.maximize_window()
    
    for item in range(6):
        wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.END)
        time.sleep(5)
    for comment in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#comment #content-text"))):
        data3.append(comment.text)


print(data3)

tf3 = data3
with open('/Users/kdr/Documents/AmazonInfo/text_files/CR_YT_3.txt', 'w') as f:
    f.writelines(tf3)


# Run the scrape for the fourth CR url:
data4 = []

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

path = webdriver.Chrome(options=options)
service = Service(executable_path=path)


path.get(url4)
path.maximize_window()

with path as driver:
    wait = WebDriverWait(driver, 120)
    driver.get(url4)
    driver.maximize_window()
    
    for item in range(6):
        wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.END)
        time.sleep(5)
    for comment in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#comment #content-text"))):
        data4.append(comment.text)


print(data4)

tf4 = data4
with open('/Users/kdr/Documents/AmazonInfo/text_files/CR_YT_4.txt', 'w') as f:
    f.writelines(tf4)
    
    
    
# Run the scrape for the fifth CR url:
data5 = []

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

path = webdriver.Chrome(options=options)
service = Service(executable_path=path)


path.get(url5)
path.maximize_window()

with path as driver:
    wait = WebDriverWait(driver, 120)
    driver.get(url5)
    driver.maximize_window()
    
    for item in range(6):
        wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.END)
        time.sleep(5)
    for comment in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#comment #content-text"))):
        data5.append(comment.text)


print(data5)

tf5 = data5
with open('/Users/kdr/Documents/AmazonInfo/text_files/CR_YT_5.txt', 'w') as f:
    f.writelines(tf5)
    
    
    
    
    

# Run the scrape for the first The Row url:
TR_data1 = []

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

path = webdriver.Chrome(options=options)
service = Service(executable_path=path)


path.get(TR_url1)
path.maximize_window()

with path as driver:
    wait = WebDriverWait(driver, 120)
    driver.get(TR_url1)
    driver.maximize_window()
    
    for item in range(6): # how many scrolls down the page
        wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.END)
        time.sleep(10)
    for comment in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#comment #content-text"))):
        TR_data1.append(comment.text)


print(TR_data1)

TR_tf1 = TR_data1
with open('/Users/kdr/Documents/AmazonInfo/text_files/TR_YT_1.txt', 'w') as f:
    f.writelines(TR_tf1)
    
    
    
# Run the scrape for the second The Row url:
TR_data2 = []

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

path = webdriver.Chrome(options=options)
service = Service(executable_path=path)


path.get(TR_url2)
path.maximize_window()

with path as driver:
    wait = WebDriverWait(driver, 120)
    driver.get(TR_url2)
    driver.maximize_window()
    
    for item in range(6): # how many scrolls down the page
        wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.END)
        time.sleep(10)
    for comment in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#comment #content-text"))):
        TR_data2.append(comment.text)


print(TR_data2)

TR_tf2 = TR_data2
with open('/Users/kdr/Documents/AmazonInfo/text_files/TR_YT_2.txt', 'w') as f:
    f.writelines(TR_tf2)
    
    
# Run the scrape for the third The Row url:
TR_data3 = []

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

path = webdriver.Chrome(options=options)
service = Service(executable_path=path)


path.get(TR_url3)
path.maximize_window()

with path as driver:
    wait = WebDriverWait(driver, 120)
    driver.get(TR_url3)
    driver.maximize_window()
    
    for item in range(6): # how many scrolls down the page
        wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.END)
        time.sleep(10)
    for comment in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#comment #content-text"))):
        TR_data3.append(comment.text)


print(TR_data3)

TR_tf3 = TR_data3
with open('/Users/kdr/Documents/AmazonInfo/text_files/TR_YT_3.txt', 'w') as f:
    f.writelines(TR_tf3)
    
    
# Run the scrape for the fourth The Row url:
TR_data4 = []

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

path = webdriver.Chrome(options=options)
service = Service(executable_path=path)


path.get(TR_url4)
path.maximize_window()

with path as driver:
    wait = WebDriverWait(driver, 120)
    driver.get(TR_url4)
    driver.maximize_window()
    
    for item in range(6): # how many scrolls down the page
        wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.END)
        time.sleep(10)
    for comment in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#comment #content-text"))):
        TR_data4.append(comment.text)


print(TR_data4)

TR_tf4 = TR_data4
with open('/Users/kdr/Documents/AmazonInfo/text_files/TR_YT_4.txt', 'w') as f:
    f.writelines(TR_tf4)
    
    
    
# Run the scrape for the fifth The Row url:
TR_data5 = []

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

path = webdriver.Chrome(options=options)
service = Service(executable_path=path)


path.get(TR_url5)
path.maximize_window()

with path as driver:
    wait = WebDriverWait(driver, 120)
    driver.get(TR_url5)
    driver.maximize_window()
    
    for item in range(6): # how many scrolls down the page
        wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.END)
        time.sleep(10)
    for comment in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#comment #content-text"))):
        TR_data5.append(comment.text)


print(TR_data5)

TR_tf5 = TR_data5
with open('/Users/kdr/Documents/AmazonInfo/text_files/TR_YT_5.txt', 'w') as f:
    f.writelines(TR_tf5)
    
    
# Run the scrape for the sixth The Row url: 
TR_data6 = []

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

path = webdriver.Chrome(options=options)
service = Service(executable_path=path)


path.get(TR_url6)
path.maximize_window()

with path as driver:
    wait = WebDriverWait(driver, 120)
    driver.get(TR_url6)
    driver.maximize_window()
    
    for item in range(6): # how many scrolls down the page
        wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.END)
        time.sleep(10)
    for comment in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#comment #content-text"))):
        TR_data6.append(comment.text)


print(TR_data6)

TR_tf6 = TR_data6
with open('/Users/kdr/Documents/AmazonInfo/text_files/TR_YT_6.txt', 'w') as f:
    f.writelines(TR_tf6)
    
    
# Run the scrape for the seventh The Row url:
TR_data7 = []

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

path = webdriver.Chrome(options=options)
service = Service(executable_path=path)


path.get(TR_url7)
path.maximize_window()

with path as driver:
    wait = WebDriverWait(driver, 120)
    driver.get(TR_url7)
    driver.maximize_window()
    
    for item in range(6): # how many scrolls down the page
        wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.END)
        time.sleep(10)
    for comment in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#comment #content-text"))):
        TR_data7.append(comment.text)


print(TR_data7)

TR_tf7 = TR_data7
with open('/Users/kdr/Documents/AmazonInfo/text_files/TR_YT_7.txt', 'w') as f:
    f.writelines(TR_tf7)
    
    



# Run the scrape for the first OpenAI url:
OAI_data1 = []

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

path = webdriver.Chrome(options=options)
service = Service(executable_path=path)


path.get(OAI_url1)
path.maximize_window()

with path as driver:
    wait = WebDriverWait(driver, 120)
    driver.get(OAI_url1)
    driver.maximize_window()
    
    for item in range(6): # how many scrolls down the page
        wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.END)
        time.sleep(10)
    for comment in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#comment #content-text"))):
        OAI_data1.append(comment.text)


print(OAI_data1)

OAI_tf1 = OAI_data1
with open('/Users/kdr/Documents/AmazonInfo/text_files/OAI_YT_1.txt', 'w') as f:
    f.writelines(OAI_tf1)    
    
    
    
# Run the scrape for the second OpenAI url:
OAI_data2 = []

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

path = webdriver.Chrome(options=options)
service = Service(executable_path=path)


path.get(OAI_url2)
path.maximize_window()

with path as driver:
    wait = WebDriverWait(driver, 120)
    driver.get(OAI_url2)
    driver.maximize_window()
    
    for item in range(6): # how many scrolls down the page
        wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.END)
        time.sleep(10)
    for comment in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#comment #content-text"))):
        OAI_data2.append(comment.text)


print(OAI_data2)

OAI_tf2 = OAI_data2
with open('/Users/kdr/Documents/AmazonInfo/text_files/OAI_YT_2.txt', 'w') as f:
    f.writelines(OAI_tf2)    
      
    
    
# Run the scrape for the third OpenAI url:
OAI_data3 = []

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

path = webdriver.Chrome(options=options)
service = Service(executable_path=path)


path.get(OAI_url3)
path.maximize_window()

with path as driver:
    wait = WebDriverWait(driver, 120)
    driver.get(OAI_url3)
    driver.maximize_window()
    
    for item in range(6): # how many scrolls down the page
        wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.END)
        time.sleep(10)
    for comment in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#comment #content-text"))):
        OAI_data3.append(comment.text)


print(OAI_data3)

OAI_tf3 = OAI_data3
with open('/Users/kdr/Documents/AmazonInfo/text_files/OAI_YT_3.txt', 'w') as f:
    f.writelines(OAI_tf3)   
    

# Run the scrape for the fourth OpenAI url:
OAI_data4 = []

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

path = webdriver.Chrome(options=options)
service = Service(executable_path=path)


path.get(OAI_url4)
path.maximize_window()

with path as driver:
    wait = WebDriverWait(driver, 120)
    driver.get(OAI_url4)
    driver.maximize_window()
    
    for item in range(6): # how many scrolls down the page
        wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.END)
        time.sleep(10)
    for comment in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#comment #content-text"))):
        OAI_data4.append(comment.text)


print(OAI_data4)

OAI_tf4 = OAI_data4
with open('/Users/kdr/Documents/AmazonInfo/text_files/OAI_YT_4.txt', 'w') as f:
    f.writelines(OAI_tf4)   
    
    
# Run the scrape for the fifth OpenAI url:
OAI_data5 = []

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

path = webdriver.Chrome(options=options)
service = Service(executable_path=path)


path.get(OAI_url5)
path.maximize_window()

with path as driver:
    wait = WebDriverWait(driver, 120)
    driver.get(OAI_url5)
    driver.maximize_window()
    
    for item in range(6): # how many scrolls down the page
        wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.END)
        time.sleep(10)
    for comment in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#comment #content-text"))):
        OAI_data5.append(comment.text)


print(OAI_data5)

OAI_tf5 = OAI_data5
with open('/Users/kdr/Documents/AmazonInfo/text_files/OAI_YT_5.txt', 'w') as f:
    f.writelines(OAI_tf5)   
     

# Run the scrape for the sixth OpenAI url:
OAI_data6 = []

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

path = webdriver.Chrome(options=options)
service = Service(executable_path=path)


path.get(OAI_url6)
path.maximize_window()

with path as driver:
    wait = WebDriverWait(driver, 120)
    driver.get(OAI_url6)
    driver.maximize_window()
    
    for item in range(6): # how many scrolls down the page
        wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.END)
        time.sleep(10)
    for comment in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#comment #content-text"))):
        OAI_data6.append(comment.text)


print(OAI_data6)

OAI_tf6 = OAI_data6
with open('/Users/kdr/Documents/AmazonInfo/text_files/OAI_YT_6.txt', 'w') as f:
    f.writelines(OAI_tf6)   
    