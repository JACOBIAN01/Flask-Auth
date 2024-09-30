from flask import Flask, render_template, redirect, url_for, flash, request
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from models import User, db
from forms import LoginForm, RegisterForm



app = Flask(__name__)
app.config['SECRET_KEY']="538fa9f367bc05745f1899ccfcce1c4c"
app.config['SQLALCHEMY_DATABASE_URI'] = 'jdbc:sqlite:identifier.sqlite'
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view='login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
@login_required
def home():
    return render_template('home.html', name=current_user.username)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('home'))
        flash('Invalid credentials', 'danger')
    return render_template('login.html', form=form)


@app.route('/register',methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(email=form.email.data,username=form.username.data)
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash("Registration Successful ! Please Log in!",'success')
        return redirect(url_for('login'))
    return render_template('register.html',form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)


