# Проект поделись горными перевалами.
### Описание:
Разработан в [SkillFactory](https://skillfactory.ru/python-developer) для Федерации Спортивного Туризма и Развития (ФСТР) с целью поделиться пейзажами, туристическими направлениями и сложностью преодоления маршрута. 
База совершенствуется самими туристами.
Реализованы методы: API POST/submitData для добавления туристом информации о новом перевале; 
GET /submitData/<id> — получение записи о определённом перевале по его id;
PATCH /submitData/<id> — редактирование существующей записи, если она еще не поступила в работу модератору;
GET /submitData/?user__email=<email> — список данных обо всех объектах, которые пользователь с почтой <email> отправил на сервер.

###  Параметры реализации:
1.При подготовке проекта использована база данных PostgreSQL, установка производится командой: 
```
pip install psycopg2
```
Порт, логин, пароль и путь к базе данных берется из переменных окружения с использованием библиотеки dotenv: 
```
pip install python-dotenv
```
2.Код приложения был покрыт тестами, установлена библиотека coverage.
Рабочий проект на базе данных PostgreSQL(конвертация с помощью ./manage.py dumpdata > dump.json,
./manage.py loaddata dump.json)

### Как работать с API (endpoints):
1. По адресу /api/submitData/pereval/ или api/schema/swagger-ui/#/api/api_submitData_pereval_create можно создать информацию о новом перевале с помощью POST.
2. По адресу /api/submitData/pereval/id или api/schema/swagger-ui/#/api/api_submitData_pereval_retrieve можно получить одну запись о перевале по ее id, в том числе статус модерации c помощью GET;
3. По адресу /api/submitData/pereval/id или /api/schema/swagger-ui/#/api/api_submitData_pereval_partial_update можно редактировать существующую запись, если она еще не поступила в работу модератору с помощь PATCH;
4. Сменить статус модерации можно только через админ-панель по адресу: /admin. Возможность работы в ней обеспечивается созданием модератора по команде:
```
python manage.py createsuperuser
```
5. По адресу /api/submitData/user__email=<str:email> или /api/schema/swagger-ui/#/api/api_submitData_user__email%3D_list  можно с помощью GET получить список данных обо всех объектах, которые пользователь с почтой <email> отправил на сервер.
Пример JSON-запроса для создания, редактирования сведений о перевале.

