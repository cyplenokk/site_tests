from flask import Flask, render_template, request
from werkzeug.utils import redirect

from data import db_session
from data.users import User

from data import db_session
from flask import Flask, render_template, redirect
from data.users import User
from data.results_dog import Results_Dog
from data.results_drink import Results_Drink
from data.results import Results
from data.reqq import Requests

from forms.user import RegisterForm, LoginForm, RequestsForm
from flask_login import LoginManager, logout_user, login_required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'test_project'
login_manager = LoginManager()
login_manager.init_app(app)

if_auto = False
user_name = ''
user_email = ''
searching = ''
result = ''

user_id = 0

titles = ["тест 'какая ты собака?'", "тест 'какой ты напиток?'", "тест 'какая/ой ты кошка/кот?'",
          "тест 'какая ты шиншилла?'"]

dog = {
    'бульдог': ['Сангвинник', 'Ассам', 'Кино', 'Силы', 'Желтый'],
    'пудель': ['Флегматик', 'Улун', 'Рисование', 'Богатство', 'Синий'],
    'гончая': ['Холерик', 'Фруктовый', 'Спорт', 'Бессмертие', 'Красный'],
    'бобтейл': ['Меланхолик', 'Нет', 'Книги', 'Любовь', 'Зеленый']
}

dog_inv = {
    '1': ['Сангвинник', 'Флегматик', 'Холерик', 'Меланхолик'],
    '2': ['Улун', 'Ассам', 'Фруктовый', 'Нет'],
    '3': ['Кино', 'Рисование', 'Спорт', 'Книги'],
    '4': ['Силы', 'Богатство', 'Любовь', 'Бессмертие'],
    '5': ['Желтый', 'Синий', 'Красный', 'Зеленый']
}

dog_results = {
    'бульдог': 0,
    'пудель': 0,
    'гончая': 0,
    'бобтейл': 0
}

drink = {
    'кофе': ['Волнение', 'Дождь', 'Осень', 'Детектив', 'Заранее'],
    'сок': ['Жизнерадостный', 'Солнце', 'Лето', 'Роман', 'Ничего'],
    'молочный коктейль': ['Мечтательный', 'Снег', 'Зима', 'Фэнтези', 'Когда как'],
    'чай': ['Задумчивый', 'Облачно', 'Весна', 'Фантастика', 'Прокрастинирую']
}

drink_inv = {
    '1': ['Волнение', 'Жизнерадостный', 'Мечтательный', 'Задумчивый'],
    '2': ['Дождь', 'Солнце', 'Снег', 'Облачно'],
    '3': ['Осень', 'Лето', 'Зима', 'Весна'],
    '4': ['Детектив', 'Роман', 'Фэнтези', 'Фантастика'],
    '5': ['Заранее', 'Ничего', 'Умею', 'Прокрастинирую']
}

drink_results = {
    'кофе': 0,
    'сок': 0,
    'молочный коктейль': 0,
    'чай': 0
}

last_drink = ''
dog_ins = [0, 0, 0, 0, 0]
dog_spisok = []

last_temp = ''
last_temp_num = ''

last_tea = ''
last_tea_num = ''

last_hobbie = ''
last_hobbie_num = ''

last_power = ''
last_power_num = ''

last_man = ''
last_man_num = ''

last_drink = ''
drink_ins = [0, 0, 0, 0, 0]
drink_spisok = []

last_char = ''
last_char_num = ''

last_wea = ''
last_wea_num = ''

last_time = ''
last_time_num = ''

last_genre = ''
last_genre_num = ''

last_color = ''
last_color_num = ''


@app.route("/")
def index():
    global if_auto, user_name, searching

    if not if_auto:
        return render_template("log_index.html", if_auto=if_auto, user=user_name)
    else:
        return render_template("log_index.html", if_auto=if_auto, user=user_name)


@app.route("/search", methods=['GET', 'POST'])
def search():
    global if_auto, user_name, titles, searching

    searching = request.args['title'].lower().split()

    ready = []

    for title in titles:
        for i in searching:
            count = 0
            if i in title:
                count += 1
        if count == len(i.split()):
            ready.append(title)

    if not if_auto:
        return render_template("search_index.html", titles=titles, request=ready, if_auto=if_auto, user=user_name)

    else:
        return render_template("search_index.html", if_auto=if_auto, user=user_name, titles=titles, request=searching)


@app.route("/auto", methods=['GET', 'POST'])
def auto():
    return render_template('auto.html', title='Авторизация')


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route("/dog_test_1", methods=['POST', 'GET'])
def dog_1():
    global dog_spisok, dog, dog_results, result, last_temp, dog_ins, last_temp, last_temp_num
    if request.method == 'POST':

        result = request.form.get('temperament')

        for key in dog:
            if dog[key][0] == result:
                dog_ins[0] += 1
                if dog_ins[0] > 1:
                    dog_spisok.remove(last_temp)
                    dog_results[last_temp_num] -= 1
                dog_results[key] += 1
                last_temp_num = key
                dog_spisok.append(result)
                last_temp = result
        return redirect("/dog_test_2")
    else:

        return render_template("dog_test_1.html", head='Какая вы собака?', if_auto=if_auto, user=user_name,
                               result=result,
                               title='Какой у вас темперамент?', first='Холерик',
                               second='Флегматик', third='Сангвинник', fourth='Меланхолик', source='/dog_test_1',
                               id_1='Holeric', id_2='Flegmatic', id_3='Sangvinnic', id_4='Melanholic',
                               value_1='Холерик',
                               value_2='Флегматик', value_3='Сангвинник', value_4='Меланхолик', name='temperament',
                               spisok=dog_spisok, message='Дальше', progress='0%', count=dog_ins, picture='static/img/dog_1.jpg')


@app.route("/dog_test_2", methods=['POST', 'GET'])
def dog_2():
    global dog_spisok, dog, dog_results, result, dog_ins, last_tea, last_tea_num

    if request.method == 'POST':

        result = request.form.get('tea')

        for key in dog:
            if dog[key][1] == result:
                dog_ins[1] += 1
                if dog_ins[1] > 1:
                    dog_spisok.remove(last_tea)
                    dog_results[last_tea_num] -= 1
                dog_results[key] += 1
                last_tea_num = key
                dog_spisok.append(result)
                last_tea = result
        return redirect("/dog_test_3")
    else:

        return render_template("dog_test_1.html", head='Какая вы собака?', if_auto=if_auto, user=user_name,
                               result=result,
                               title='Ваш любимый чай?', first='Я не пью чай',
                               second='Черный чай Ассам', third='Зеленый чай Молочный Улун',
                               fourth='Черный фруктовый чай', source='/dog_test_2',
                               id_1='Not', id_2='Assam', id_3='Ulun', id_4='Fruit',
                               value_1='Нет',
                               value_2='Ассам', value_3='Улун', value_4='Фруктовый', name='tea', spisok=dog_spisok,
                               message='Дальше', progress='20%', count=dog_ins, picture='static/img/dog_2.jpg')


@app.route("/dog_test_3", methods=['POST', 'GET'])
def dog_3():
    global dog_spisok, dog, dog_results, result, dog_ins, last_hobbie, last_hobbie_num

    if request.method == 'POST':

        result = request.form.get('hobbie')

        for key in dog:
            if dog[key][2] == result:
                dog_ins[2] += 1
                if dog_ins[2] > 1:
                    dog_spisok.remove(last_hobbie)
                    dog_results[last_hobbie_num] -= 1
                dog_results[key] += 1
                last_hobbie_num = key
                dog_spisok.append(result)
                last_hobbie = result
        return redirect("/dog_test_4")
    else:

        return render_template("dog_test_1.html", head='Какая вы собака?', if_auto=if_auto, user=user_name,
                               result=result,
                               title='Чем вы предпочли бы заняться?', first='Просмотром фильма или сериала',
                               second='Рисованием', third='Чтением книги', fourth='Спортом', source='/dog_test_3',
                               id_1='Film', id_2='Draw', id_3='Book', id_4='Sport',
                               value_1='Кино',
                               value_2='Рисование', value_3='Книги', value_4='Спорт', name='hobbie', spisok=dog_spisok,
                               message='Дальше', progress='40%', count=dog_ins, picture='static/img/dog_3.jpeg')


@app.route("/dog_test_4", methods=['POST', 'GET'])
def dog_4():
    global dog_spisok, dog, dog_results, result, dog_ins, last_power, last_power_num

    if request.method == 'POST':

        result = request.form.get('wish')

        for key in dog:
            if dog[key][3] == result:
                dog_ins[3] += 1
                if dog_ins[3] > 1:
                    dog_spisok.remove(last_power)
                    dog_results[last_power_num] -= 1
                dog_results[key] += 1
                last_power_num = key
                dog_spisok.append(result)
                last_power = result

        return redirect("/dog_test_5")
    else:

        return render_template("dog_test_1.html", head='Какая вы собака?', if_auto=if_auto, user=user_name,
                               result=result,
                               title='Что бы вы выбрали?', first='Богатство',
                               second='Любовь', third='Сверхъестественные силы', fourth='Бессмертие',
                               source='/dog_test_4',
                               id_1='Money', id_2='Love', id_3='Powers', id_4='Deathless',
                               value_1='Богатство',
                               value_2='Любовь', value_3='Силы', value_4='Бессмертие', name='wish', spisok=dog_spisok,
                               message='Дальше', progress='60%', count=dog_ins, picture='static/img/dog_4.webp')


@app.route("/dog_test_5", methods=['POST', 'GET'])
def dog_5():
    global dog_spisok, dog, dog_results, result, dog_ins, last_color, last_color_num

    if request.method == 'POST':

        result = request.form.get('color')

        for key in dog:
            if dog[key][4] == result:
                dog_ins[4] += 1
                if dog_ins[4] > 1:
                    dog_spisok.remove(last_color)
                    dog_results[last_color_num] -= 1
                dog_results[key] += 1
                last_color_num = key
                dog_spisok.append(result)
                last_color = result

        return redirect("/dog_results")
    else:

        return render_template("dog_test_1.html", head='Какая вы собака?', if_auto=if_auto, user=user_name,
                               result=result,
                               title='Ваш любимый цвет?', first='Синий',
                               second='Желтый', third='Зеленый', fourth='Красный', source='/dog_test_5',
                               id_1='Blue', id_2='Yellow', id_3='Green', id_4='Red',
                               value_1='Синий',
                               value_2='Желтый', value_3='Зеленый', value_4='Красный', name='color', spisok=dog_spisok,
                               message='Завершить', progress='80%', count=dog_ins, picture='static/img/dog_5.jfif')


@app.route("/dog_results", )
def result_dog():
    global dog_spisok, dog, dog_results, result, user_id, dog_inv

    maximum = 0
    for key in dog_results:
        if dog_results[key] > maximum:
            maximum = dog_results[key]
            result = key

    new_spisok = []
    for key in dog_inv:
        for item in dog_spisok:
            if item in dog_inv[key] and item not in new_spisok:
                new_spisok.append(item)

    db_sess = db_session.create_session()
    res = Results_Dog(
        dog_1=sorted(dog_spisok)[0],
        dog_2=sorted(dog_spisok)[1],
        dog_3=sorted(dog_spisok)[2],
        dog_4=sorted(dog_spisok)[3],
        dog_5=sorted(dog_spisok)[4],
        user_id=user_id
    )
    db_sess.add(res)
    db_sess.commit()

    db_sess = db_session.create_session()
    ress = Results(
        dog=result,
        user_id=user_id
    )
    db_sess.add(ress)
    db_sess.commit()

    return render_template("result_dog.html", head='Какая вы собака?', title=result, spis=dog_spisok)


@app.route("/drink_test_1", methods=['POST', 'GET'])
def drink_1():
    global drink_spisok, drink, drink_results, result, last_char, drink_ins, last_char_num
    if request.method == 'POST':

        result = request.form.get('character')

        for key in drink:
            if drink[key][0] == result:
                drink_ins[0] += 1
                if drink_ins[0] > 1:
                    drink_spisok.remove(last_char)
                    drink_results[last_char_num] -= 1
                drink_results[key] += 1
                last_char_num = key
                drink_spisok.append(result)
                last_char = result
        return redirect("/drink_test_2")
    else:

        return render_template("dog_test_1.html", head='Какой вы напиток?', if_auto=if_auto, user=user_name,
                               result=result,
                               title='Как бы вы охарактеризовали себя?', first='Я жизнерадостный человек',
                               second='Я задумчивый человек', third='Я мечтательный человек',
                               fourth='Я много волнуюсь о различных вещах', source='/drink_test_1',
                               id_1='Happy', id_2='Think', id_3='Dream', id_4='Care',
                               value_1='Жизнерадостный',
                               value_2='Задумчивый', value_3='Мечтательный', value_4='Волнение', name='character',
                               spisok=drink_spisok, message='Дальше', progress='0%', count=drink_ins, picture='static/img/drink_1.jpg')


@app.route("/drink_test_2", methods=['POST', 'GET'])
def drink_2():
    global drink_spisok, drink, drink_results, result, drink_ins, last_wea, last_wea_num

    if request.method == 'POST':

        result = request.form.get('weather')

        for key in drink:
            if drink[key][1] == result:
                drink_ins[1] += 1
                if drink_ins[1] > 1:
                    drink_spisok.remove(last_wea)
                    drink_results[last_wea_num] -= 1
                drink_results[key] += 1
                last_wea_num = key
                drink_spisok.append(result)
                last_wea = result
        return redirect("/drink_test_3")
    else:

        return render_template("dog_test_1.html", head='Какой вы напиток?', if_auto=if_auto, user=user_name,
                               result=result,
                               title='Ваша любимая погода?', first='Дождливая',
                               second='Солнечная', third='Облачная',
                               fourth='Снежная', source='/drink_test_2',
                               id_1='Rainy', id_2='Sunny', id_3='Cloudy', id_4='Snow',
                               value_1='Дождь',
                               value_2='Солнце', value_3='Облачно', value_4='Снег', name='weather', spisok=drink_spisok,
                               message='Дальше', progress='20%', count=drink_ins, picture='static/img/drink_2.jpg')


@app.route("/drink_test_3", methods=['POST', 'GET'])
def drink_3():
    global drink_spisok, drink, drink_results, result, drink_ins, last_time, last_time_num

    if request.method == 'POST':

        result = request.form.get('time')

        for key in drink:
            if drink[key][2] == result:
                drink_ins[2] += 1
                if drink_ins[2] > 1:
                    drink_spisok.remove(last_time)
                    drink_results[last_time_num] -= 1
                drink_results[key] += 1
                last_time_num = key
                drink_spisok.append(result)
                last_time = result
        return redirect("/drink_test_4")
    else:

        return render_template("dog_test_1.html", head='Какой вы напиток?', if_auto=if_auto, user=user_name,
                               result=result,
                               title='Ваше любимое время года?', first='Зима',
                               second='Лето', third='Осень', fourth='Весна', source='/drink_test_3',
                               id_1='Winter', id_2='Summer', id_3='Autumn', id_4='Spring',
                               value_1='Зима',
                               value_2='Лето', value_3='Осень', value_4='Весна', name='time', spisok=drink_spisok,
                               message='Дальше', progress='40%', count=drink_ins, picture='static/img/drink_3.jpg')


@app.route("/drink_test_4", methods=['POST', 'GET'])
def drink_4():
    global drink_spisok, drink, drink_results, result, drink_ins, last_genre, last_genre_num

    if request.method == 'POST':

        result = request.form.get('genre')

        for key in drink:
            if drink[key][3] == result:
                drink_ins[3] += 1
                if drink_ins[3] > 1:
                    drink_spisok.remove(last_genre)
                    drink_results[last_genre_num] -= 1
                drink_results[key] += 1
                last_genre_num = key
                drink_spisok.append(result)
                last_genre = result

        return redirect("/drink_test_5")
    else:

        return render_template("dog_test_1.html", head='Какой вы напиток?', if_auto=if_auto, user=user_name,
                               result=result,
                               title='Какой жанр книг вы бы предпочли?', first='Детектив',
                               second='Фантастика', third='Роман', fourth='Фэнтези',
                               source='/drink_test_4',
                               id_1='Детектив', id_2='Fantastic', id_3='Roman', id_4='Fantasy',
                               value_1='Богатство',
                               value_2='Фантастика', value_3='Роман', value_4='Фэнтези', name='genre',
                               spisok=drink_spisok,
                               message='Дальше', progress='60%', count=drink_ins, picture='static/img/drink_4.jpg')


@app.route("/drink_test_5", methods=['POST', 'GET'])
def drink_5():
    global drink_spisok, drink, drink_results, result, drink_ins, last_man, last_man_num

    if request.method == 'POST':

        result = request.form.get('manage')

        for key in drink:
            if drink[key][4] == result:
                drink_ins[4] += 1
                if drink_ins[4] > 1:
                    drink_spisok.remove(last_man)
                    drink_results[last_man_num] -= 1
                drink_results[key] += 1
                last_man_num = key
                drink_spisok.append(result)
                last_man = result

        return redirect("/drink_results")
    else:

        return render_template("dog_test_1.html", head='Какой вы напиток?', if_auto=if_auto, user=user_name,
                               result=result,
                               title='Насколько вы организованны?', first='Я умею распределять свое время',
                               second='Я часто прокрастинирую и откладываю на потом', third='Я делаю все заранее',
                               fourth='Я часто ленюсь и ничего не делаю', source='/drink_test_5',
                               id_1='Blue', id_2='Yellow', id_3='Green', id_4='Red',
                               value_1='Умею',
                               value_2='Прокрастинирую', value_3='Заранее', value_4='Ничего', name='manage',
                               spisok=drink_spisok,
                               message='Завершить', progress='80%', count=drink_ins, picture='static/img/drink_5.webp')


@app.route("/drink_results", )
def result_drink():
    global drink_spisok, drink, drink_results, result, user_id, drink_inv

    maximum = 0
    for key in drink_results:
        if drink_results[key] > maximum:
            maximum = drink_results[key]
            result = key

    new_spisok = []
    for key in drink_inv:
        for item in drink_spisok:
            if item in drink_inv[key] and item not in new_spisok:
                new_spisok.append(item)

    db_sess = db_session.create_session()
    res = Results_Drink(
        drink_1=sorted(drink_spisok)[0],
        drink_2=sorted(drink_spisok)[1],
        drink_3=sorted(drink_spisok)[2],
        drink_4=sorted(drink_spisok)[3],
        drink_5=sorted(drink_spisok)[4],
        user_id=user_id
    )
    db_sess.add(res)
    db_sess.commit()

    db_sess = db_session.create_session()
    ress = Results(
        drink=result,
        user_id=user_id
    )
    db_sess.add(ress)
    db_sess.commit()

    return render_template("result_dog.html", head='Какой вы напиток?', title=result, spis=drink_spisok)


@app.route('/register', methods=['GET', 'POST'])
def register():
    global if_auto, user_name, user_email, user_id

    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            email=form.email.data,
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        if_auto = True
        user_name = user.name
        user_email = user.email
        user_id = user.id
        return redirect("/")
    return render_template('register.html', title='Регистрация', form=form, if_auto=if_auto, user=user_name)


@app.route('/login', methods=['GET', 'POST'])
def login():
    global if_auto, user_name, user_email, user_id

    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            if_auto = True
            user_name = user.name
            user_email = user.email
            user_id = user.id
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль. Возможно, требуется регистрация",
                               form=form)

    return render_template('login.html', title='Авторизация', form=form, if_auto=if_auto, user=user_name)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/personal')
def person():
    form = RequestsForm()
    return render_template("personal.html", user=user_name, if_auto=if_auto, email=user_email, form=form)


def main():
    db_session.global_init("db/tests.db")

    app.run(port=8080)


if __name__ == '__main__':
    db_session.global_init("db/tests.db")

    app.run(port=8080)
