from flask import Flask
from flask import render_template
from random import choice


app = Flask(__name__)


# главное окно сайта
@app.route('/')
@app.route('/main')
def main():
    return """<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Главная</title>
    <style>
      a {
       line-height: 2
       }

      .thumb img  {
       border: 2px solid #55c5e9; /* Рамка вокруг фотографии */
       padding: 0px; 
       margin-right: 15px; /* Отступ справа */
       margin-bottom: 15px; /* Отступ снизу */
       }

      figcaption { 
       text-align: center;
       max-width: 350px;
       }

      .layer2 {
       padding-left: 50%;
      }

      .layer2 {
       padding-left: 50%;
      }

      .layer3 {
       padding-left: 80%;
      }
      #left { position: absolute; left: 0; top: 15%; width: 20%; }
      #right { position: absolute; right: 0; top: 15%; width: 80%; }

    </style>
  </head>

  <body>
    <big><big><center><h1><b>DinoLAND</b></h1></center></big></big>
    <hr></hr> 

    <div id="left"> 
      <center><h2>Основные разделы:</h2></center>
      <ul id="navbar">
        <li><a href="main">Главная</a></li>
        <li><a href="random_fact">Рандомный факт</a></li>
        <li><a href="random_dinosaur">Случайный динозавр</a></li>
        <li><a href="tests">Тесты</a></li>
        <li><a href="new_dinosaur">Добавь своего динозавра</a></li>
        <li><a href="registration">Вход/Регистрация</a></li>
      </ul>
    </div>

    <div id="right"> 
      <center><h1><b>Главная</b></h1></center>
      <center><h2>Самые популярные динозавры:</h2></center>
      <div class="thumb">
        <img src="static/img/Тиранозавр.png" alt="упси дупси" width="350" height="250" title="Тираннозавр">
        <img src="static/img/Велоцираптор.png" alt="упси дупси" width="350" height="250" title="Велоцираптор">
        <img src="static/img/Трицератопс.png" alt="упси дупси" width="350" height="250" title="Трицератопс">
        <img src="static/img/Спинозавр.png" alt="упси дупси" width="350" height="250" title="Спинозавр">
        <img src="static/img/Стегозавр.png" alt="упси дупси" width="350" height="250" title="Стегозавр">
        <img src="static/img/Апатозавр.png" alt="упси дупси" width="350" height="250" title="Апатозавр">
        <img src="static/img/Диплодок.png" alt="упси дупси" width="350" height="250" title="Диплодок">
        <img src="static/img/Аллозавр.png" alt="упси дупси" width="350" height="250" title="Аллозавр">
        <img src="static/img/Брахиозавр.png" alt="упси дупси" width="350" height="250" title="Брахиозавр">
        <img src="static/img/Анкилозавр.png" alt="упси дупси" width="350" height="250" title="Анкилозавр">
        <img src="static/img/Игуанодон.png" alt="упси дупси" width="350" height="250" title="Игуанодон">
        <img src="static/img/Гигантозавр.png" alt="упси дупси" width="350" height="250" title="Гиганотозавр">
        <img src="static/img/Паразауролоф.png" alt="упси дупси" width="350" height="250" title="Паразауролоф">
        <img src="static/img/Дилофозавр.png" alt="упси дупси" width="350" height="250" title="Дилофозавр">
        <img src="static/img/Пахицефалозавр.png" alt="упси дупси" width="350" height="250" title="Пахицефалозавр">
        <img src="static/img/Дейноних.png" alt="упси дупси" width="350" height="250" title="Дейноних">
        <img src="static/img/Карнотавр.png" alt="упси дупси" width="350" height="250" title="Карнотавр">
        <img src="static/img/Компсогнат.png" alt="упси дупси" width="350" height="250" title="Компсогнат">
        
      </div>
    </div>

  </body>
</html>"""


# окно с фактами
@app.route('/random_fact')
def random_fact():
    names = ["аллозавр", "брахиозавр", "велоцираптор", "паразауролоф",
             "спинозавр", "тиранозавр", "игуанодон"]
    # выбирается динозавр
    dino = choice(names) + ".html"
    return render_template(dino)


# окно с информацией
@app.route('/random_dinosaur')
def random_dinosaur():
    names = ["анкилозавр", "апатозавр", "велоцираптор", "гигантозавр",
             "карнотавр", "пахицефалозавр", "тиранозавр"]
    # выбирается динозавр
    dino = choice(names) + "_инфа.html"
    return render_template(dino)


# окно с тестом
@app.route('/tests')
def tests():
    return """<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Главная</title>
    <style>
      a {
       line-height: 2
       }

      #left { position: absolute; left: 0; top: 15%; width: 20%; }
      #right { position: absolute; right: 0; top: 15%; width: 80%; }

    </style>
  </head>

  <body>
    <big><big><center><h1><b>DinoLAND</b></h1></center></big></big>
    <hr></hr> 

    <div id="left"> 
      <center><h2>Основные разделы:</h2></center>
      <ul id="navbar">
        <li><a href="main">Главная</a></li>
        <li><a href="random_fact">Рандомный факт</a></li>
        <li><a href="random_dinosaur">Случайный динозавр</a></li>
        <li><a href="tests">Тесты</a></li>
        <li><a href="new_dinosaur">Добавь своего динозавра</a></li>
        <li><a href="registration">Вход/Регистрация</a></li>
      </ul>
    </div>

    <div id="right"> 
      <center><h1><b>Тест</b></h1></center>
      <p>Выполните задания теста:</p>
<p>Введите название самого известного динозавра <input type="text" id="z_1"></p>
<p>Введите название самого опасного динозавра <input type="text" id="z_2"></p>
<p>Введите название самого высокого динозавра <input type="text" id="z_3"></p>
<p>Введите название самого маленького динозавра <input type="text" id="z_4"></p>
<button onclick="proverit();">Проверить</button>
<div id="rezultat"></div>
<script>
function proverit(){
pr_otv_zadachi_1 = "Тираннозавр";
pr_otv_zadachi_2 = "Гиганотозавр";
pr_otv_zadachi_3 = "Завропосейдон";
pr_otv_zadachi_4 = "Микроцератопс";
otv_uch_1 = document.getElementById('z_1').value;
otv_uch_2 = document.getElementById('z_2').value;
otv_uch_3 = document.getElementById('z_3').value;
otv_uch_4 = document.getElementById('z_4').value;
ball = 0;
if(otv_uch_1 == pr_otv_zadachi_1){
ball +=1;
}
if(otv_uch_2 == pr_otv_zadachi_2){
ball +=1;
}
if(otv_uch_3 == pr_otv_zadachi_3){
ball +=1;
}
if(otv_uch_4 == pr_otv_zadachi_4){
ball +=1;
}
vsego_zadach = 4;
procent_vip = ball/vsego_zadach * 100;
document.getElementById('rezultat').innerHTML = "Ответы верные на "+procent_vip+"%.";
}
</script>
      
    </div>

  </body>
</html>"""


# окно для нового динозавра
@app.route('/new_dinosaur')
def new_dinosaur():
    return """<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Новый динозавр</title>
    <style>
      a {
       line-height: 2
       }

      #left { position: absolute; left: 0; top: 15%; width: 20%; }
      #right { position: absolute; right: 0; top: 15%; width: 80%; }

    </style>
  </head>

  <body>
    <big><big><center><h1><b>DinoLAND</b></h1></center></big></big>
    <hr></hr>

    <div id="left">
      <center><h2>Основные разделы:</h2></center>
      <ul id="navbar">
        <li><a href="main">Главная</a></li>
        <li><a href="random_fact">Рандомный факт</a></li>
        <li><a href="random_dinosaur">Случайный динозавр</a></li>
        <li><a href="tests">Тесты</a></li>
        <li><a href="new_dinosaur">Добавь своего динозавра</a></li>
        <li><a href="registration">Вход/Регистрация</a></li>
      </ul>
    </div>

    <div id="right">
      <center><h1><b>Новый динозавр</b></h1></center>

      <center><h2>В настоящее время данный раздел находится в разработке. Приносим свои извинения!</h2></center>

      <center><img src="static/img/RUN.gif" alt="упси дупси" width="700" height="350"><center>

    </div>

  </body>
</html>"""


# окно регистрации
@app.route('/registration')
def registration():
    return """<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Главная</title>
  <style>
      a {
       line-height: 2
       }

      #left { position: absolute; left: 0; top: 15%; width: 20%; }
      #right { position: absolute; right: 0; top: 15%; width: 80%; }

body {
    font-family: Arial, Helvetica, sans-serif;
    background-color: white;} {
    font-family: Arial, Helvetica, sans-serif;
    background-color: black;}

* {
    box-sizing: border-box;}

.container {
    padding: 16px;
    background-color: white;}

input[type=text], input[type=password] {
    width: 100%;
    padding: 15px;
    margin: 5px 0 22px 0;
    display: inline-block;
    border: none;
    background: #f1f1f1;}

input[type=text]:focus, input[type=password]:focus {
    background-color: #ddd;
    outline: none;}

hr {
    border: 1px solid #f1f1f1;
    margin-bottom: 25px;}

.registerbtn {
    background-color: #4CAF50;
    color: white;
    padding: 16px 20px;
    margin: 8px 0;
    border: none;
    cursor: pointer;
    width: 100%;
    opacity: 0.9;}

.registerbtn:hover {
    opacity: 1;}

a {color: dodgerblue;}

.signin {
    background-color: #f1f1f1;
    text-align: center;}
</style>
</head>
<body>
<big><big><center><h1><b>DinoLAND</b></h1></center></big></big>
    <hr></hr>

    <div id="left">
      <center><h2>Основные разделы:</h2></center>
      <ul id="navbar">
        <li><a href="main">Главная</a></li>
        <li><a href="random_fact">Рандомный факт</a></li>
        <li><a href="random_dinosaur">Случайный динозавр</a></li>
        <li><a href="tests">Тесты</a></li>
        <li><a href="new_dinosaur">Добавь своего динозавра</a></li>
        <li><a href="registration">Вход/Регистрация</a></li>
      </ul>
    </div>

    <div id="right">
<form action="/action.py" method="GET">
  <div class="container">
    <h1>Регистрация</h1>
    <p>Заполните эти поля чтобы создать аккаунт.</p>
    <hr>

    <label for="email"><b>Email</b></label>
    <input type="text" placeholder="Введите Email" name="email" required>

    <label for="psw"><b>Password</b></label>
    <input type="password" placeholder="Введите пароль" name="psw" required>

    <label for="psw-repeat"><b>Repeat Password</b></label>
    <input type="password" placeholder="Повторите пароль" name="psw-repeat" required>
    <hr>
    <p>Создавая аккаунт вы соглашаетесь с нашими <a href="polite">Условиями и Конфиденциальностью</a>.</p>

    <button type="submit" class="registerbtn">Зарегистрироваться</button>
  </div>

  <div class="container signin">
    <p>Уже есть аккаунт? <a href="enter">Вход</a>.</p>
  </div>
</form>
    </div>
</body>
</html>

"""


# окно входа
@app.route('/enter')
def enter():
    return """<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Главная</title>
  <style>
      a {
       line-height: 2
       }

      #left { position: absolute; left: 0; top: 15%; width: 20%; }
      #right { position: absolute; right: 0; top: 15%; width: 80%; }

body {
    font-family: Arial, Helvetica, sans-serif;
    background-color: white;}

* {
    box-sizing: border-box;}

.container {
    padding: 16px;
    background-color: white;}

input[type=text], input[type=password] {
    width: 100%;
    padding: 15px;
    margin: 5px 0 22px 0;
    display: inline-block;
    border: none;
    background: #f1f1f1;}

input[type=text]:focus, input[type=password]:focus {
    background-color: #ddd;
    outline: none;}

hr {
    border: 1px solid #f1f1f1;
    margin-bottom: 25px;}

.registerbtn {
    background-color: #4CAF50;
    color: white;
    padding: 16px 20px;
    margin: 8px 0;
    border: none;
    cursor: pointer;
    width: 100%;
    opacity: 0.9;}

.registerbtn:hover {
    opacity: 1;}

a {color: dodgerblue;}

.signin {
    background-color: #f1f1f1;
    text-align: center;}
</style>
</head>
<body>
<big><big><center><h1><b>DinoLAND</b></h1></center></big></big>
    <hr></hr>

    <div id="left">
      <center><h2>Основные разделы:</h2></center>
      <ul id="navbar">
        <li><a href="main">Главная</a></li>
        <li><a href="random_fact">Рандомный факт</a></li>
        <li><a href="random_dinosaur">Случайный динозавр</a></li>
        <li><a href="tests">Тесты</a></li>
        <li><a href="new_dinosaur">Добавь своего динозавра</a></li>
        <li><a href="registration">Вход/Регистрация</a></li>
      </ul>
    </div>

    <div id="right">

<form action="/action_page.php">
  <div class="container">
    <h1>Вход</h1>
    <p>Заполните эти поля чтобы войти в аккаунт.</p>
    <hr>

    <label for="email"><b>Email</b></label>
    <input type="text" placeholder="Введите Email" name="email" required>

    <label for="psw"><b>Password</b></label>
    <input type="password" placeholder="Введите пароль" name="psw" required>

    <hr>

    <button type="submit" class="registerbtn">Войти</button>
  </div>

  <div class="container signin">
    <p>Еще нет аккаунта? <a href="registration">Регистрация</a>.</p>
  </div>
</form>
    </div>>

</body>
</html>

"""


# окно политики конфедициальности
@app.route('/polite')
def polite():
    return """<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Главная</title>
    <style>
      a {
       line-height: 2
       }

      #left { position: absolute; left: 0; top: 15%; width: 20%; }
      #right { position: absolute; right: 0; top: 15%; width: 80%; }

    </style>
  </head>

  <body>
    <big><big><center><h1><b>DinoLAND</b></h1></center></big></big>
    <hr></hr> 

    <div id="left"> 
      <center><h2>Основные разделы:</h2></center>
      <ul id="navbar">
        <li><a href="main">Главная</a></li>
        <li><a href="random_fact">Рандомный факт</a></li>
        <li><a href="random_dinosaur">Случайный динозавр</a></li>
        <li><a href="tests">Тесты</a></li>
        <li><a href="new_dinosaur">Добавь своего динозавра</a></li>
        <li><a href="registration">Вход/Регистрация</a></li>
      </ul>
    </div>

    <div id="right"> 
      <center><h1><b>Политика конфиденциальности</b></h1></center>
      <center><img src="static/img/sad.gif" alt="упси дупси" width="700" height="350"><center>
        <h3>Ваши данные будут под контролем :Р</h3>>

    </div>>

  </body>
</html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
