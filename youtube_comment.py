# Youtube username, comment crawler (Auto scroll)
# developed by LHG
# Python 3.7
# You need to install this module => selenium, BeautifulSoup, Pandas
# check your chrome version! (included chrome webdriver version : 84)
# download chrome webdriver => http://chromedriver.chromium.org/downloads
from selenium import webdriver as wd
from bs4 import BeautifulSoup

from webdriver_manager.chrome import ChromeDriverManager
import sys, os, time, re
import pandas as pd

# current time + file name
# Year=y, Month=m, Day=d, Hour=H, Minute=M, Second=S / If you need H,M,S just add %H%M%S
t_str = time.strftime("%y%m%d_%H%M%S")

# chrome headless mode
chrome_options = wd.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("lang=ko_KR")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# chrome webdriver path
# you need to make .spec file and input your webdriver path -> pathex
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)

driver = wd.Chrome(resource_path('./chromedriver.exe'), options=chrome_options)

# Enter the YouTube url
user_input=input('Enter Youtube ID:')
# example:7fBJu2WDI3c/8SYI9mtjBSc
url = 'https://www.youtube.com/watch?v='+user_input

driver.get(url)

# Scroll function
last_page_height = driver.execute_script("return document.documentElement.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    time.sleep(3.0)
    new_page_height = driver.execute_script("return document.documentElement.scrollHeight")
    if new_page_height == last_page_height:
        break
    last_page_height = new_page_height

html_source = driver.page_source
driver.close()
soup = BeautifulSoup(html_source, 'lxml')

youtube_username = soup.select('div#header-author > a > span')
youtube_comments = soup.select('yt-formatted-string#content-text')

list_youtube_username = []
list_youtube_comments = []
text=""

for i in range(len(youtube_username)):
    str_tmp = str(youtube_username[i].text)
    str_tmp = str_tmp.replace('\n', '')
    str_tmp = str_tmp.replace('\t', '')
    str_tmp = str_tmp.replace(' ','')
    list_youtube_username.append(str_tmp)

    str_tmp = str(youtube_comments[i].text)
    str_tmp = str_tmp.replace('\n', '')
    str_tmp = str_tmp.replace('\t', '')
    str_tmp = str_tmp.replace(' ', '')
    list_youtube_comments.append(str_tmp)

# --- dataframe (data refinement) / pandas module ---
# here is a description site -> https://pandas.pydata.org/docs/user_guide/index.html
pd_data = {"Username":list_youtube_username, "Comment":list_youtube_comments}
youtube_df = pd.DataFrame(pd_data)
print(youtube_df)
print('----- Done Well -----')
youtube_df.to_excel(t_str+"_"+'youtube_crawling.xlsx')
