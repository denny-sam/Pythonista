from splinter import Browser
from selenium import webdriver
from openpyxl import Workbook
import time
import requests
import shutil
import os
import sys

if len(sys.argv) == 1 :
    print("Enter atleast one username as argument")
    os.sys(exit())

for i in range(1, len(sys.argv)):
    user = sys.argv[i]
    wb = Workbook()
    ws = wb.active
    ws.title = "sheet"

    driver = webdriver.Chrome()
    user_url = "https://www.instagram.com/"+user
    driver.get(user_url)
    try: 
        j = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div/div/h2')
        if j:
            print("The account you are trying to access is private.")
            os.sys(exit())
    except:
        print('')

    print("Scrolling the feeds of "+user)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    elem = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div/a')
    elem.click()
    time.sleep(3)    

    try:
        while driver.find_element_by_class_name('_anzsd'):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
            driver.execute_script("window.scrollTo(0,0);")
            time.sleep(0.5)

    except:
        print('Finished scrolling')

    os.system("mkdir -p "+user+"/posts")
    print("Saving posts of "+user)

    imgs = driver.find_elements_by_class_name('_2di5p')
    
    for x in range(len(imgs)):
        caption = imgs[x].get_attribute("alt")
        url = imgs[x].get_attribute("src")

        ws.cell(row=x+1, column=1).value = caption

        response = requests.get(url, stream=True)
        
        try:
            with open(user+"/posts/post_"+str(len(imgs)-x)+".jpg", "wb") as out_file:
                shutil.copyfileobj(response.raw, out_file)
            del response
        except:
            print("unable to save file")

    wb.save(user+"/"+user+"_captions.xlsx")

    driver.close()

