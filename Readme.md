### Registation with the help of JWT
###  1. Устанавливаем библиотеку djangorestframework-simplejwt и производим все настройки согласно документации

https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html

###  2. Для примера сделаем так, чтобы просматривать странцу с машинами могли только те пользователи, которые авторизовались с помощью JWT
![img.png](images%20for%20readme%2Fimg.png)
###  3. Для получения токена авторизованному пользователю, необходимо перейти на определенную страницу и ввести login and password

![img_1.png](images%20for%20readme%2Fimg_1.png)
![img_2.png](images%20for%20readme%2Fimg_2.png)

###  4. Получим 2 токена : access and refresh

###     4.1 access token, используется при запросах к серверу (например, при логине). У него есть два свойства: он многоразовый и короткоживущий. 

###     4.2 Второй, refresh token, используется для обновления пары access и refresh токенов. 
![img_3.png](images%20for%20readme%2Fimg_3.png)


###  5. Через программу Postman попытаемся достучаться до сайта с машинами без авторизации. Но получим ошибку(Учетные данные не были предоставлены)
![img_4.png](images%20for%20readme%2Fimg_4.png)

###  6. Для этого мы выберем авторизацию через Bearer Token и передадим наш полученный access token
![img_5.png](images%20for%20readme%2Fimg_5.png)
###  Получаем такой результат

![img_6.png](images%20for%20readme%2Fimg_6.png)

###  7. Бывает, что время использования access токена истекает, для этого нам надо сделать refresh токена
###  Мы копируем refresh токен и переходим по url для получения нового access токена
![img_7.png](images%20for%20readme%2Fimg_7.png)
![img_8.png](images%20for%20readme%2Fimg_8.png)

### refresh token --------> new access token and new refresh token
![img_9.png](images%20for%20readme%2Fimg_9.png)





### Выгрузка данных из БД в exel
### Реализованно с помощью библиотеки import-export and django admin

![img_10.png](images%20for%20readme%2Fimg_10.png)
### Файл с данными ----> [Car-2023-04-25.xls](Car-2023-04-25.xls)