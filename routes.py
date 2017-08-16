from flask import Flask, render_template, request, session, redirect, url_for
from models import db
from forms import SignupForm
from models import User

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:sed123@localhost/learning-flask'
db.init_app(app)


app.secret_key = "development-key"

@app.route('/')
def index():
    return render_template("index.html")
@app.route('/about')
def about():
    return render_template("about.html")
@app.route('/signup', methods=['POST', 'GET'])
def signup():
    form = SignupForm()
    if request.method == "POST":
        if form.validate() == False:
            return render_template("signup.html", form=form)
        else:
            newuser = User(form.first_name.data, form.last_name.data, form.email.data, form.password.data)
            db.session.add(newuser)
            db.session.commit()
            return "Thank you for signing up and becoming a valuable member"
    elif request.method == "GET":
        return render_template("signup.html", form=form)

if __name__ == '__main__':
    app.run(debug=True)
