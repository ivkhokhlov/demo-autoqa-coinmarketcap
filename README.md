# Демонстрационный проект API + UI + MOBILE на примере портала [coinmarketcap.com](https://coinmarketcap.com/)
![image](https://github.com/ivkhokhlov/demo-autoqa-coinmarketcap/assets/58159018/e3d953ee-931f-4131-a9ed-068984b35030)


## Описание
Демо-проект для демонстрации возможностей тестирования в связке API + UI + MOBILE в рамках одного продукта
![image](https://github.com/ivkhokhlov/demo-autoqa-coinmarketcap/assets/58159018/5d7682a4-e82c-4f58-bd1b-c539f3e009cd)


## Стек технологий
<p  align="center">
<code><img width="7%" title="Python" src="assets/python.png"></code>
<code><img width="7%" title="Pytest" src="assets/pytest.png"></code>
<code><img width="7%" title="Selene" src="assets/selene.png"></code>
<code><img width="7%" title="Selenium" src="assets/selenium.png"></code>
<code><img width="7%" title="Selenoid" src="assets/selenoid.png"></code>
<code><img width="7%" title="Jenkins" src="assets/jenkins.png"></code>
<code><img width="7%" title="Telegram" src="assets/tg.png"></code>
<code><img width="7%" title="Jenkins" src="assets/jira.png"></code>
<code><img width="7%" title="Telegram" src="assets/requests.png"></code>
<code><img width="7%" title="Telegram" src="assets/browserstack.png"></code>
<code><img width="7%" title="Telegram" src="assets/appium.png"></code>
</p>

## Запуск тестов
### Запуск тестов локально
1. Клонировать репозиторий
```
git clone git@github.com:ivkhokhlov/demo-autoqa-coinmarketcap
.git
```
2. Перейти в папку
```
cd demo-autoqa-coinmarketcap
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

# Отчеты и TMS
## Allure-отчет
Доступен по [[ссылке](https://jenkins.autotests.cloud/job/C07-master_klinka-store_gaijin_demo/16/allure/)](https://jenkins.autotests.cloud/job/07-master_klinka-diploma/20/allure)
Отчет полностью прописан по шагам и готов для интеграции в TestOps
![image](https://github.com/ivkhokhlov/demo-autoqa-coinmarketcap/assets/58159018/b6f22bc0-5958-4559-bd6e-36c1d3336c61)
![image](https://github.com/ivkhokhlov/demo-autoqa-coinmarketcap/assets/58159018/0178c9d5-0ccc-42a2-b28c-c921c27ad4f3)

## Allure TestOps
Выгрузка отчетов настроена в AllureTestOPS + обратная интеграция в Jenkins для еденичнго запуска
https://allure.autotests.cloud/launch/32398/tree/523384?treeId=7460
![image](https://github.com/ivkhokhlov/demo-autoqa-coinmarketcap/assets/58159018/338a1d28-0a63-4b15-a523-41bd050972ec)

## Видео запуска тестов
### UI
![2ade84bbd1f69befc2911a23a01b06d8](https://github.com/ivkhokhlov/demo-autoqa-coinmarketcap/assets/58159018/240e67c9-c053-4032-ab20-1757fdc70547)
### MOBILE
![73330c21c59b131204250343f485ce9fa8868a6d](https://github.com/ivkhokhlov/demo-autoqa-coinmarketcap/assets/58159018/237224df-2a14-4a64-b8cd-178e65d13d0d)
## Пример оповещений в Telegram
![image](https://github.com/ivkhokhlov/demo-autoqa-coinmarketcap/assets/58159018/b089374e-c75a-426f-82c1-dc5b2033697a)


