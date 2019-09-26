from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import xlrd
import math

chromedriver_dir = '/usr/local/bin/chromedriver'
driver = webdriver.Chrome(chromedriver_dir)

driver.get('http://www.iros.go.kr/')
driver.implicitly_wait(4)

driver.find_element_by_xpath('//*[@id="cenS"]/div/ul/li[1]/div/ul/li[2]/a').send_keys(Keys.ENTER)

Alert(driver).accept()
driver.implicitly_wait(4)

input_frame = driver.find_element_by_name('inputFrame')
driver.switch_to.frame(input_frame)

# 부동산구분 (1.집합건물 / 2.토지 / 3.건물)
estate = driver.find_element_by_id('selkindcls')
estate.send_keys('집합건물')

# 시/도
region = driver.find_element_by_id('e001admin_regn1')
region.send_keys('대구광역시')

# 주소
region = driver.find_element_by_id('txt_simple_address')
region.send_keys('상록로 21')
driver.implicitly_wait(4)

# 검색버튼
button = driver.find_element_by_id('btnSrchSojae')
button.send_keys(Keys.ENTER)
driver.implicitly_wait(10)

frame = driver.find_element_by_name('seltype_ifrm')
driver.switch_to.frame(frame)

# 검색결과 수
sum = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="simpleResult"]/div[3]/div[1]/span')))
page = math.ceil(sum/10)
last_page_result = sum%10

wb = xlrd.open_workbook('apt_docs.xlsx')



go = True
for i in range(1, 10):
	for j in range(1, page):
		if j == page && i == last_page_result :
			go = False
			break
		x =driver.find_element_by_xpath('//*[@id="simpleResult"]/div[2]/table/tbody/tr['+str(i)+']/td['+str(j)+']')
		wb.write(i,j,x)
	if !go :
		break

wb.save('apt_docs.xlsx')