from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from wtforms.validators import Email

app = Flask(__name__)

app.config['SECRET_KEY'] = '4daf72f578adc41da0f41f9ef6d23cc2'

posts = [
    {
        'author': 'Matt Orme',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'Now'
    },

    {
        'author': 'Jane Dpe',
        'title': 'Blog Post 523',
        'content': 'hello post content',
        'date_posted': 'also now'
    },
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == 'admin' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check your username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
    