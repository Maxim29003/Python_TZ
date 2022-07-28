# Парсер
В файле parser.py написан код, которой парсит всех майнеров с сайта https://moonarch.app/miners.
Данные майнера:

1. Имя майнера
2. Ссылку на сайт
3. Ссылку на telegram
4. Token
5. Open contract balance chart
6. Open contract code
7. Fees
8. Time
9. Daily %:
10. TVL
11. Evol TVL

В поцессе выполнения программы данные о майнерах сохраняются в файл data.txt, а html код страницы в файл source-page.html
Для работы парсера необходима браузер Google Chrome и драйвер для этого браузера.
Пути для всех файлов хранятся в глобальных переменных в коде.

DRIVER_DIRECTORY = '/home/maxim/PycharmProjects/Practik_1/chromedriver_linux64/chromedriver'
PATH_FILE_HTML = '/home/maxim/PycharmProjects/TZpython/source-page.html'
PATH_FILE_TXT = "/home/maxim/PycharmProjects/TZpython/data.txt"

Парсер заберает данные с сайта каждую минуту.
Это можно изменить в коде на строке 148 
"schedule.every(1).minutes.do(update)" в место 1 введите своё время в минутах 

#Бот
В файле bot.py написан код Telegram Bot 
Название: MoonarchBot
Ссылка: http://t.me/Cryoto_Price_Bot

При вводе команды "Top" бот пришлёт топ 10 майнеров сайта
1. Имя майнера
2. Ссылку на сайт
3. Ссылку на telegram
4. Token

Порядок запуска:
1.Запустить файл parser.py и дождаться сообщения "Данные обновились"
2.Запустить фай bot.py



