<h1 align='center'>API Социальной сети</h1>

Проект представляет собой небольшую социальную сеть сделанную с использованием технологии Django Rest Framework. В проекте реализован весь CRUD, авторизация(использовалась библиотека djoser), дополнительные @action под тематику проекта 

### Тестирование
* Тестирование поиска пользователя.
* Тестирование поиска поста по оглавлению.
* Тестирование поиска поста по тематике.
* Тестирование лайков.
* Тестирование дислайков. 



### API Endpoint

#### Authentication

* **/auth/users/** (Регистрация пользователя)
* **/auth/token/login/** (Авторизация пользователя)
* **/api/users/logout/** (Выход пользователя)


#### Users

* **/social_net/user/** (Вывод всех пользователей, 'GET')
* **/social_net/user/** (Добавление пользователя, 'POST')
* **/social_net/user/pk/** (Чтение пользователя, 'GET')
* **/social_net/user/pk/** (Редактирование пользователя, 'PUT')
* **/social_net/user/pk/** (Удаление пользователя, 'DELETE')
* **/social_net/user/search_user/?user** (Поиск пользователя, 'GET')
  

#### Product

* **/social_net/post/** (Вывод всех постов, 'GET')
* **/social_net/post/** (Добавление поста, 'POST')
* **/social_net/post/pk/** (Чтение поста, 'GET')
* **/social_net/post/pk/** (Редактирование поста, 'PUT')
* **/social_net/post/pk/** (Удаление поста, 'DELETE')
* **/social_net/post/search_post/?post** (Поиск поста, 'GET')
* **/social_net/post/search_by_theme/?id** (Фильтрация постов по теме, 'GET')
* **/social_net/post/like/?id** (Лай, 'GET')
* **/social_net/post/dislike/?id** (Дислайк, 'GET')


#### Post

* **/magazine_api/category/** (Вывод всех категорий товаров, 'GET')
* **/magazine_api/category/** (Добавление категории, 'POST')
* **/magazine_api/category/pk/** (Чтение категории, 'GET')
* **/magazine_api/category/pk/** (Редактирование категории, 'PUT')
* **/magazine_api/category/pk/** (Удаление категории, 'DELETE')


#### Comment

* **/social_net/comment/** (Вывод всех пользователей, 'GET')
* **/social_net/comment/** (Добавление пользователя, 'POST')
* **/social_net/comment/pk/** (Чтение пользователя, 'GET')
* **/social_net/comment/pk/** (Редактирование пользователя, 'PUT')
* **/social_net/comment/pk/** (Удаление пользователя, 'DELETE')


### Install 

    pip install -r req.txt

### Usage

    python manage.py test

### License

  Этот проект лицензирован под MIT License.


    

