from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import requests
from pprint import pprint
from time import sleep
import re

#페이지 별로 데이터 추출 함수 생성
def extract_data_from_page(driver):
    #Beautifulsoup을 사용해서 데이터 추출

    page_source = driver.page_source
    soup = BeautifulSoup(page_source, "html.parser")

    #가격 데이터 추출

    price_tag = soup.select(selector=".HFtIW")
    price_list = []

    for text in price_tag:
        price_text = text.text
        price_list.append(price_text)
        

    #방의 형태 데이터 추출

    residential_type_tag = soup.select(selector=".hcIoY")
    residential_type_list = []

    for text in residential_type_tag:
        residential_type_text = text.text
        residential_type_list.append(residential_type_text)


    #방의 특징 데이터 추출

    description_tag = soup.select(selector=".hvrORi")
    description_list = []

    for i in range(0, len(description_tag) - 1, 2):
        first_description = description_tag[i].text
        second_description = description_tag[i + 1].text
    
        description_list.append((first_description, second_description))

    return price_list, residential_type_list, description_list


#강남역 주변의 원룸, 오피스텔 url

da_bang_url = "https://www.dabangapp.com/search/map?filters=%7B%22multi_room_type%22%3A%5B0%2C1%2C2%5D%2C%22selling_type%22%3A%5B0%2C1%2C2%5D%2C%22deposit_range%22%3A%5B0%2C999999%5D%2C%22price_range%22%3A%5B0%2C999999%5D%2C%22trade_range%22%3A%5B0%2C999999%5D%2C%22maintenance_cost_range%22%3A%5B0%2C999999%5D%2C%22room_size%22%3A%5B0%2C999999%5D%2C%22supply_space_range%22%3A%5B0%2C999999%5D%2C%22room_floor_multi%22%3A%5B1%2C2%2C3%2C4%2C5%2C6%2C7%2C-1%2C0%5D%2C%22division%22%3Afalse%2C%22duplex%22%3Afalse%2C%22room_type%22%3A%5B1%2C2%5D%2C%22use_approval_date_range%22%3A%5B0%2C999999%5D%2C%22parking_average_range%22%3A%5B0%2C999999%5D%2C%22household_num_range%22%3A%5B0%2C999999%5D%2C%22parking%22%3Afalse%2C%22short_lease%22%3Afalse%2C%22full_option%22%3Afalse%2C%22elevator%22%3Afalse%2C%22balcony%22%3Afalse%2C%22safety%22%3Afalse%2C%22pano%22%3Afalse%2C%22is_contract%22%3Afalse%2C%22deal_type%22%3A%5B0%2C1%5D%7D&position=%7B%22location%22%3A%5B%5B127.0087128%2C37.478779%5D%2C%5B127.0463924%2C37.517083%5D%5D%2C%22center%22%3A%5B127.02755260367%2C37.4979334880069%5D%2C%22zoom%22%3A15%7D&search=%7B%22id%22%3A%22subway_20%22%2C%22type%22%3A%22subway%22%2C%22name%22%3A%22%EA%B0%95%EB%82%A8%EC%97%AD%22%7D&tab=all"

#driver 초기화

chrome_option = Options()
chrome_option.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_option)

#데이터 저장할 리스트 초기화

all_price_list = []
all_residential_type_list = []
all_description_list = []

#driver를 사용해서 페이지 열기

driver.get(url=da_bang_url)

#각페이지에서 데이터 추출 및 저장
for _ in range(8):
    price_list, residential_type_list, description_list = extract_data_from_page(driver)
    all_price_list.extend(price_list)
    all_residential_type_list.extend(residential_type_list)
    all_description_list.extend(description_list)
    next_page = driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[1]/div/div/div[1]/div[2]/div/div/div/div/button[8]')
    current_page = int(driver.find_element(By.CLASS_NAME, "cbZgbl").text)
    page_buttons = driver.find_elements(By.CLASS_NAME, "styled__PageBtn-d24fjp-2")
    max_page = max([int(text.text) for text in page_buttons])
    if max_page > current_page:
        next_page.click()
        sleep(2)

driver.quit()


sleep(2)

#Google Form을 열어서 각 데이터 전송

form_url = "https://docs.google.com/forms/d/e/1FAIpQLSd_8dvy9pxax0R1XdIZq04VUIDkZfpdkrWJomd7X4YuCyUXbw/viewform?usp=sf_link"
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_option)
driver.get(url=form_url)

for i in range(len(all_price_list)):
    wait = WebDriverWait(driver, 15)    
    type_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    description_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    price_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    
    #input에 데이터 입력
    
    type_input.send_keys(all_residential_type_list[i])
    description_input.send_keys(all_description_list[i])
    price_input.send_keys(all_price_list[i])

    #데이터 제출
    
    submit_button.click()
    
    #다음 응답 입력

    sleep(2)
    next_submit = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    next_submit.click()








