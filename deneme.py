# ***************** Instagram Bot Wıth Selenium *****************

import time
from User_infor import username, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


driver = webdriver.Chrome()

driver.get('https://www.instagram.com/')
driver.maximize_window()

def login_and_settings(driver, username, password):
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH,'/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input')))
    user_name_bar = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input')
    user_name_bar.send_keys(username)

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH,'/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input')))
    password_bar = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input')
    password_bar.send_keys(password + Keys.ENTER)

    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div')))
    bilgi_kaydet = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div')

    if 'Şimdi Değil' in bilgi_kaydet.text:
        bilgi_kaydet.click()

    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')))
    bildirim_ac = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
    bildirim_ac.click()

    user_page = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div[1]/div[2]/div/div[1]/div/div/div/div/div/div[2]/div/div/span[1]/span/div/a')
    user_page.click()


login_and_settings(driver, username, password)

WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a/span/span')))
number_of_followers = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a/span/span')
number_of_followers = int(number_of_followers.text)
print(f'takipçi sayın: {number_of_followers}')

click_flowers = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a')
click_flowers.click()


WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/div/div/div/div[2]/div/div/span[1]/span/div/div[1]/div/a/span/div')))
follower_list = []

def scrollDown():
    jsKomut = '''
    sayfa = document.querySelector("._aano");
    sayfa.scrollTo(0,sayfa.scrollHeight);
    var sayfaSonu = sayfa.scrollHeight;
    return sayfaSonu;
    '''
    sayfaSonu = driver.execute_script(jsKomut)

    while True:
        son = sayfaSonu
        time.sleep(0.5)
        sayfaSonu = driver.execute_script(jsKomut)

        if son == sayfaSonu:
            break

def get_followers(driver):
    scrollDown()
    for x in range(1, number_of_followers + 1):
        WebDriverWait(driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,f'/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[{x}]/div/div/div/div[2]/div/div/span[1]/span/div/div[1]/div/a/span/div')))
        follower = driver.find_element(By.XPATH,f'/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[{x}]/div/div/div/div[2]/div/div/span[1]/span/div/div[1]/div/a/span/div')
        follower_list.append(follower.text)

    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH,'/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/button')))
    close_button = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/button')
    close_button.click()

get_followers(driver)

WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[3]/a/span/span')))
number_of_follow = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[3]/a/span/span')
number_of_follow = int(number_of_follow.text)
print(f'takip sayın: {number_of_follow}')

follow_list = []

def get_follow(driver):
    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[3]/a')))
    click_follow = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[3]/a')
    click_follow.click()
    time.sleep(1)

    scrollDown()

    for x in range(1, number_of_follow + 1):
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH,f'/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[{x}]/div/div/div/div[2]/div/div/span[1]/span/div/div/div/a/span/div')))
        follower = driver.find_element(By.XPATH,f'/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[{x}]/div/div/div/div[2]/div/div/span[1]/span/div/div/div/a/span/div')
        follow_list.append(follower.text)

get_follow(driver)

fark_list = []
for i in follow_list:
    if i not in follower_list:
        fark_list.append(i)

for user in fark_list:
    print(user)





