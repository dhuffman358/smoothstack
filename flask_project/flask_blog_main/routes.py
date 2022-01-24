import secrets
import os
from PIL import Image 
from flask import render_template, url_for, flash, redirect, abort, request
from flask_blog_main import app, password_checker, db, password_checker
from flask_blog_main.forms import RegisterForm, LoginForm, UpdateAccountForm, PostForm
from flask_blog_main.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required

@app.route('/')
@app.route('/home')
def home():
    posts = Post.query.all()
    return render_template('home.html', posts = posts)

@app.route("/about")
def about():
    return render_template('about.html', title = 'About')

@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    rform = RegisterForm()
    if rform.validate_on_submit():
        hashword = password_checker.generate_password_hash(rform.password.data).decode('utf-8')
        user = User(username=rform.username.data, email=rform.email.data, password=hashword)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created, please login to continue.', category='success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form = rform)

@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    lform = LoginForm()
    if lform.validate_on_submit():
        user = User.query.filter_by(email=lform.email.data).first()
        if user and password_checker.check_password_hash(user.password, lform.password.data):
            login_user(user, remember=True)
            next_page = request.args.get('next')
            if current_user.admin == 'admin':
                return redirect(next_page) if next_page else redirect(url_for('user_list'))
            else:
                return redirect(next_page) if next_page else redirect(url_for('home'))
        flash('Login Unsuccessful. Check email or password.', 'danger')
    return render_template('login.html', title='Login', form = lform)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

def save_picture(form_picture):
    random_number = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_number +f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pictures', picture_fn)
    i = Image.open(form_picture)
    i.thumbnail((125, 125))
    i.save(picture_path)
    return picture_fn




@app.route('/account', methods=["GET", "POST"])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated.', 'success')
        return redirect(url_for('account'))
    elif request.method =='GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pictures/' + current_user.image_file)
    return render_template('account.html', title='My Account', image_file=image_file, form=form)



@app.route('/post/new', methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Post created successfully.', 'success')
        return redirect(url_for('home'))
    return render_template('create_post.html', title='New Post', form=form, legend='New Post')

@app.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)


@app.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated.', 'success')
        return redirect(url_for('post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title='Update Post', form=form, legend='Update Post')

@app.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    db.session.delete(post)
    db.session.commit()
    flash('Post deleted successfully.', 'success')
    return redirect(url_for('home'))

@app.route('/user_list', methods =['GET'])
@login_required
def user_list():
    if current_user.admin != 'admin':
        abort(403)
    ulist=User.query.all()
    print(ulist[0].username)
    return render_template('user_list.html', title='User List', ulist = ulist)
    
