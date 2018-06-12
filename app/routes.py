from app import app

# the @app.route decorator creates an association between the URL given as an argument and the function. In this
# example there are two decorators, which associate the URLs / and /index to this function.
@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"