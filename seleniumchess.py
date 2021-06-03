from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#enter your selenium path here
PATH='C:\chromedriver.exe'
driver = webdriver.Chrome(PATH)



driver.get("http://chess.com/login")

#do NOT change these 2 lines
username = driver.find_element_by_id("username")
password = driver.find_element_by_id("password")


#enter your username and password here
username.send_keys("USERNAME")
password.send_keys("PASSWORD")

driver.find_element_by_name("login").click()


page=1
while True:
    print(1)
    driver.get("https://www.chess.com/games/archive?gameOwner=my_game&gameTypes%5B0%5D=chess960&gameTypes%5B1%5D=daily&gameType=live&page="+str(page))
    try:
        selector = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "archive-games-check-all"))
        )
        selector.click()


        downloader = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "archive-games-download-button"))
        )
        downloader.click()
    except:
        driver.quit()
        exit()
    page+=1
    print(page)





