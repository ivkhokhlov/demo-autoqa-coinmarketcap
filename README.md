# Демонстрационный проект для портала https://coinmarketcap.com/
![image](/assets/coinmarketcap-separat.png)
Включает в себя 
1. API тесты
2. UI тесты
3. MOBILE тесты
## Описание
Демо-проект для страницы настроек профиля пользователя.
![image](https://github.com/ivkhokhlov/store_gaijin_demo/assets/58159018/a8f6b440-0997-4417-b731-723c90e20cf8)

## Стек технологий
<code><img width="5%" title="Python" src="assets/python.png"></code>
<code><img width="5%" title="Pytest" src="assets/pytest.png"></code>
<code><img width="5%" title="Selene" src="assets/selene.png"></code>
<code><img width="5%" title="Selenium" src="assets/selenium.png"></code>
<code><img width="5%" title="Selenoid" src="assets/selenoid.png"></code>
<code><img width="5%" title="Jenkins" src="assets/jenkins.png"></code>
<code><img width="5%" title="Telegram" src="assets/tg.png"></code>

## Запуск тестов
### Запуск тестов локально
1. Клонировать репозиторий
```
git clone git@github.com:ivkhokhlov/store_gaijin_demo.git
```
2. Перейти в папку
```
cd store_gaijin_demo
```
3. Инициализировать виртуальное окружение
```
python -m venv venv
```
4. Активировать виртуальное окружение
```
source ./venv/bin/activate
```
5. Установить зависимости
```
pip install -r requirements.txt
```
6. Положить .env файл в папку с проектом
```
GAIJIN_LOGIN = 'xokev83191@ipnuc.com'
GAIJIN_PASSWORD = 123456
SELENE_LOGIN = 'user1'
SELENE_PASSWORD = 1234
```
7. Запустить тесты
```
python -m pytest
```
### Удаленный запуск проекта в Jenkins
Проект доступен по [ссылке](https://jenkins.autotests.cloud/job/C07-master_klinka-store_gaijin_demo/), сборка и просмотр отчетов доступна для неавторизованных пользователей.
1. Открыть проект в Jenkins
2. Нажать "Собрать с параметрами"
<details><summary>screenshot</summary><img src=https://github.com/ivkhokhlov/store_gaijin_demo/assets/58159018/856de153-56cf-4511-975e-473a0479eede></details>

3. Заполнить параметры, нажать "Собрать"
<details><summary>screenshot</summary><img src=https://github.com/ivkhokhlov/store_gaijin_demo/assets/58159018/8f318a87-a210-4293-af4c-f0b92d9e086d></details>

4. После успешной сборки, Allure-отчет с результатами будет доступен в истории сборок
<details><summary>screenshot</summary><img src=https://github.com/ivkhokhlov/store_gaijin_demo/assets/58159018/8a3e48cf-a4fd-4a82-bc6c-c41b0213d6e3></details>

## Отчеты

### Allure-отчет
Доступен по [ссылке](https://jenkins.autotests.cloud/job/C07-master_klinka-store_gaijin_demo/16/allure/)
![image](https://github.com/ivkhokhlov/store_gaijin_demo/assets/58159018/82f540bf-cd90-49cc-b218-292c346a77a3)
![image](https://github.com/ivkhokhlov/store_gaijin_demo/assets/58159018/6638c88b-71ee-40cd-a478-c92e8305eda3)
![image](https://github.com/ivkhokhlov/store_gaijin_demo/assets/58159018/926d7d2e-c4ba-4304-a71a-03fa5d8c5878)


### Пример оповещений в Telegram
![image](https://github.com/ivkhokhlov/store_gaijin_demo/assets/58159018/167cd8d9-a7c0-45ef-9118-abe0579dc69e)
### Видео запуска теста
Браузеры запускаются удаленно на Selenide
![selene](https://github.com/ivkhokhlov/store_gaijin_demo/assets/58159018/cac8b732-daf2-44d6-b572-41cbd0edef7e)
