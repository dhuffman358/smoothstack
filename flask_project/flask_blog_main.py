from sre_constants import SUCCESS
from flask import Flask, render_template, url_for, flash, redirect
from forms import RegisterForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '6587989bbaaeeff0923eeebb0192234'

posts = [
    {   'author': 'Daniel Huffman',
        'title': "First Post Content",
        'date_posted' : 'Jan 21 2021',
        'content': 'This is the first ever post ever done on any project like this ever.'
    },
        
    {
        'author': 'Joe Mama',
        'title': "Best Post Ever",
        'date_posted' : 'Jan 21 2021',
        'content' : 'This post is inarguably the best post ever.'
    }
]   



@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts = posts)

@app.route("/about")
def learn():
    return render_template('about.html', title = 'About')

@app.route("/register", methods=["GET", "POST"])
def register():
    rform = RegisterForm()
    if rform.validate_on_submit():
        flash(f'Account created for {rform.username.data}!', category='success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form = rform)

@app.route("/login")
def login():
    lform = LoginForm()
    return render_template('login.html', title='Login', form = lform)




if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port =3000)
