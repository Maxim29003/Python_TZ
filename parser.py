import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import schedule


URL = "https://moonarch.app/miners"
DRIVER_DIRECTORY = '/home/maxim/PycharmProjects/Practik_1/chromedriver_linux64/chromedriver'
SCROLL_PAUSE_TIME = 4
PAUSE_TIME = 4
PATH_FILE_HTML = '/home/maxim/PycharmProjects/TZpython/source-page.html'
PATH_FILE_TXT = "/home/maxim/PycharmProjects/TZpython/data.txt"


def get_source_html(url):
    driver = webdriver.Chrome(
        executable_path=DRIVER_DIRECTORY
    )

    driver.maximize_window()

    try:
        driver.get(url=url)
        time.sleep(PAUSE_TIME)

        button_click = driver.find_elements(By.TAG_NAME, "button").pop()
        button_click.click()

        time.sleep(PAUSE_TIME)

        last_height = driver.execute_script("return document.body.scrollHeight")

        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(SCROLL_PAUSE_TIME)

            with open(PATH_FILE_HTML, "w") as file:
                file.write(driver.page_source)

            new_height = driver.execute_script("return document.body.scrollHeight")

            if new_height == last_height:
                break

            last_height = new_height

    except Exception as _ex:
        print(_ex)
    finally:
        driver.close()
        driver.quit()


def get_data():
    str_html = ""
    with open(PATH_FILE_HTML) as file:
        str_html = file.readline()

    soup = BeautifulSoup(str_html, "lxml")
    rows = soup.find_all("tr")
    with open(PATH_FILE_TXT, "w") as file:
        for tr in rows:
            td = tr.find_all("td")
            print(td)
            if len(td) != 0:
                str_data = ""
                try:
                    str_data += "Link to telegram: {0},".format(td[0].find("a").get("href"))
                except Exception:
                    str_data += "Link to telegram: None,"

                try:
                    str_data += "Link to the website: {0},".format(td[1].find("a").get("href"))
                except Exception:
                    str_data += "Link to the website: None,"

                try:
                    str_data += "Miner's name: {0},".format(td[1].find("a").text)
                except Exception:
                    str_data += "Miner's name: None,"

                try:
                    str_data += "Token: {0},".format(td[3].find("a").find("img").get("class")[1])
                except Exception:
                    str_data += "Token: None,"

                try:
                    list_href = []
                    for a in td[4].find_all("a"):
                        list_href.append(a.get("href"))
                    str_data += "Open contract balance chart: {0},".format(list_href[0])
                    str_data += "Open contract code: {0},".format(list_href[0])
                except Exception:
                    str_data += "Open contract balance chart: None,"
                    str_data += "Open contract code: None,"

                try:
                    list_fees = []
                    for span in td[5].find_all("span"):
                        list_fees.append(span.text)
                    if len(list_fees) >= 2:
                        str_data += "Fees: {0}{1},".format(list_fees[0], list_fees[1])
                    if len(list_fees) == 1:
                        str_data += "Fees: {0},".format(list_fees[0])
                except Exception:
                    str_data += "Fees: None,"

                try:
                    str_data += "Time: {0},".format(td[6].find("span").text)
                except Exception:
                    str_data += "Time: None,"

                try:
                    str_data += "Daily %: {0},".format(td[7].find("span").text)
                except Exception:
                    str_data += "Daily %: None,"

                try:
                    str_data += "TVL: {0},".format(td[8].find("span").text)
                except Exception:
                    str_data += "TVL: None,"

                try:
                    str_data += "Evol TVL: {0}\n".format(td[9].find("span").text)
                except Exception:
                    str_data += "Evol TVL: None\n"
                file.write(str_data)


def output():
    with open(PATH_FILE_TXT) as file:
        for line in file.readlines():
            for word in line.split(","):
                print(word)
        print("\n")


def update():
    get_source_html(URL)
    get_data()
    output()
    print("Данные обновились")


def main():
    schedule.every(1).minutes.do(update)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()