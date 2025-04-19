import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

os.devnull ="D:\APP\Python\Python312\chromedriver.log"

print("-------------", os.devnull)

# 指定 ChromeDriver 的路径
chromedriver_path = r'D:\APP\Python\Python312\chromedriver.exe'
service = Service(executable_path=chromedriver_path)

service.log_path = r'D:\APP\Python\Python312\chromedriver.log'  # 设置日志文件路径

driver = webdriver.Chrome(service=service)
driver.get('https://www.baidu.com/')

# 获取页面标题
print(driver.title)
driver.quit()

time.sleep(20)

