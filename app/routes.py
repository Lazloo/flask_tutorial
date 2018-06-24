from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

# the @app.route decorator creates an association between the URL given as an argument and the function. In this
# example there are two decorators, which associate the URLs / and /index to this function.
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    # The render_template() function invokes the Jinja2 template engine that comes bundled with the Flask framework.
    # Jinja2 substitutes {{ ... }} blocks with the corresponding values, given by the arguments provided in the
    # render_template() call.
    return render_template('index.html', title='Home', user=user, posts=posts)


# This tells Flask that this view function accepts GET and POST requests, overriding the default, which is to accept
# only GET requests. The "Method Not Allowed" error that the browser showed you before, appears because the browser
# tried to send a POST request and the application was not configured to accept it.
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    # When the browser sends the GET request to receive the web page with the form, this method is going to return False
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        # This function instructs the client web browser to automatically navigate to a different page, given as an
        # argument. This view function uses it to redirect the user to the index page of the application.
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
