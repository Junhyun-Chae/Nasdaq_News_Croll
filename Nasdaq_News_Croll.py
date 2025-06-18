import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import pyautogui
import openpyxl
import os

kabu = []
kabu_name = []
kabu_code = []
keyword_kabu_code = 'NONE'

code_name = openpyxl.load_workbook('./code_name.xlsx')
code_sheet = code_name["Nasdaq"]

for item in code_sheet.rows:
    code_val = item[1].value
    kabu_name.append(code_val)
    code_val = item[2].value
    kabu_code.append(code_val)

# User input for search method
bunnrui = pyautogui.prompt(
    "If you know the exact stock name or code, enter it directly.\n"
    "Otherwise, enter '1'.\n"
    "If '1' is entered, the program will match stock names and codes using the Excel file."
)

while True:
    if bunnrui == '1':
        keyword = pyautogui.prompt("Enter a keyword to search for:")

        print('==== Matching keyword with stock codes ====')
        keyword = keyword.upper()
        for i in range(0, 14280):
            if keyword in str(kabu_code[i]):
                print(kabu_name[i], kabu_code[i])

        print('\n==== Matching keyword with stock names ====')
        keyword = keyword.title()
        for i in range(0, 14280):
            if keyword in kabu_name[i]:
                print(kabu_name[i], kabu_code[i])

        keyword = pyautogui.prompt("Enter the keyword to search again:")
        lastpage = pyautogui.prompt("Enter the last page number you want to search:")
        keyword_change = keyword.upper()

        for i in range(0, 14280):
            if keyword_change in str(kabu_code[i]):
                keyword_kabu_name = kabu_name[i]
                keyword_kabu_code = kabu_code[i]

        keyword_change = keyword.title()
        for i in range(0, 14280):
            if keyword_change in kabu_name[i]:
                keyword_kabu_name = kabu_name[i]
                keyword_kabu_code = kabu_code[i]

        pageNum = 1
        for i in range(1, int(lastpage) * 10, 10):
            print('\n========== Naver News Search by Stock Name ==========')
            print(f"========== Page {pageNum} ==========")

            response = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={keyword_kabu_name}&start={i}")
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
            links = soup.select(".news_tit")

            for link in links:
                title = link.text
                url = link.attrs['href']
                print(title, url, '\n')

            pageNum += 1

        if keyword_kabu_code != 'NONE':
            pageNum = 1
            for i in range(1, int(lastpage) * 10, 10):
                print('\n========== Naver News Search by Stock Code ==========')
                print(f"========== Page {pageNum} ==========")

                response = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={keyword_kabu_code}&start={i}")
                html = response.text
                soup = BeautifulSoup(html, 'html.parser')
                links = soup.select(".news_tit")

                for link in links:
                    title = link.text
                    url = link.attrs['href']
                    print(title, url, '\n')

                pageNum += 1

        # Google News Search
        baseUrl = 'https://news.google.com/search?q='
        plusUrl = keyword_kabu_name
        url = baseUrl + plusUrl

        driver = webdriver.Chrome()
        driver.get(url)

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        newsUrl = 'https://news.google.com'
        r = soup.select('.xrnccd')

        print('\n========== Google News Search by Stock Name ==========')
        for i in r:
            print(i.text)
            name = i.a.attrs['href']
            print(newsUrl + name, '\n')

        plusUrl = keyword_kabu_code
        print('\n========== Google News Search by Stock Code ==========')
        for i in r:
            print(i.text)
            name = i.a.attrs['href']
            print(newsUrl + name, '\n')

        driver.close()

    else:
        keyword = bunnrui
        lastpage = pyautogui.prompt("Enter the last page number you want to search:")
        keyword_change = keyword.upper()

        for i in range(0, 14280):
            if keyword_change in str(kabu_code[i]):
                keyword_kabu_name = kabu_name[i]
                keyword_kabu_code = kabu_code[i]

        keyword_change = keyword.title()
        for i in range(0, 14280):
            if keyword_change in kabu_name[i]:
                keyword_kabu_name = kabu_name[i]
                keyword_kabu_code = kabu_code[i]

        pageNum = 1
        for i in range(1, int(lastpage) * 10, 10):
            print('\n========== Naver News Search by Stock Name ==========')
            print(f"========== Page {pageNum} ==========")

            response = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={keyword_kabu_name}&start={i}")
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
            links = soup.select(".news_tit")

            for link in links:
                title = link.text
                url = link.attrs['href']
                print(title, url, '\n')

            pageNum += 1

        if keyword_kabu_code != 'NONE':
            pageNum = 1
            for i in range(1, int(lastpage) * 10, 10):
                print('\n========== Naver News Search by Stock Code ==========')
                print(f"========== Page {pageNum} ==========")

                response = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={keyword_kabu_code}&start={i}")
                html = response.text
                soup = BeautifulSoup(html, 'html.parser')
                links = soup.select(".news_tit")

                for link in links:
                    title = link.text
                    url = link.attrs['href']
                    print(title, url, '\n')

                pageNum += 1

        baseUrl = 'https://news.google.com/search?q='
        plusUrl = keyword_kabu_name
        url = baseUrl + plusUrl

        driver = webdriver.Chrome()
        driver.get(url)

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        newsUrl = 'https://news.google.com'
        r = soup.select('.xrnccd')

        print('\n========== Google News Search by Stock Name ==========')
        for i in r:
            print(i.text)
            name = i.a.attrs['href']
            print(newsUrl + name, '\n')

        plusUrl = keyword_kabu_code
        print('\n========== Google News Search by Stock Code ==========')
        for i in r:
            print(i.text)
            name = i.a.attrs['href']
            print(newsUrl + name, '\n')

        driver.close()

    # Restart loop
    bunnrui = pyautogui.prompt(
        "If you know the exact stock name or code, enter it directly.\n"
        "Otherwise, enter '1'.\n"
        "If '1' is entered, the program will match stock names and codes using the Excel file."
    )
    os.system('cls')
