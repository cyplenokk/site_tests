from flask import Flask, render_template, request
from werkzeug.utils import redirect

from data import db_session
from data.users import User

from data import db_session
from flask import Flask, render_template, redirect
from data.users import User
from data.results_dog import Results_Dog
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

titles = ["тест 'какая ты собака?'", "тест 'какой ты напиток?'", "тест 'какая ты кошка/кот?'",
          "тест 'какая ты шиншилла?'"]

dog = {
    'бульдог': ['Сангвинник', 'Ассам', 'кино', 'силы', 'желтый'],
    'пудель': ['Флегматик', 'Улун', 'рисование', 'богатство', 'синий'],
    'гончая': ['Холерик', 'Фруктовый', 'спорт', 'бессмертие', 'красный'],
    'бобтейл': ['Меланхолик', 'Нет', 'книги', 'любовь', 'зеленый']
}

dog_results = {
    'бульдог': 0,
    'пудель': 0,
    'гончая': 0,
    'бобтейл': 0
}

dog_spisok = []


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

    searching = request.args['title'].lower()

    if not if_auto:
        return render_template("search_index.html", titles=titles, request=searching, if_auto=if_auto, user=user_name)

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
    global dog_spisok, dog, dog_results, result

    if request.method == 'POST':

        result = request.form.get('temperament')

        for key in dog:
            if key[0] == result:
                dog_results[key] += 1
                dog_spisok.append(result)
        return redirect("/")
    else:

        return render_template("dog_test_1.html", if_auto=if_auto, user=user_name, result=result)




@app.route('/register', methods=['GET', 'POST'])
def register():
    global if_auto, user_name, user_email

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
        return redirect("/")
    return render_template('register.html', title='Регистрация', form=form, if_auto=if_auto, user=user_name)


@app.route('/login', methods=['GET', 'POST'])
def login():
    global if_auto, user_name, user_email

    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            if_auto = True
            user_name = user.name
            user_email = user.email
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
