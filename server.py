from flask import Flask
from flask import escape
from flask import url_for
from flask import render_template
from flask import request
app = Flask(__name__)

# @app.route("/")
# def index():
#     return "<h1>Index</h1>"

# @app.route('/<value>')
# def show_value(value):
#     return f"<h1>{escape(value)}</h1>"


# @app.route('/post/<int:id>')
# def show_id(int:id):
#     return f"{escape(id)}"


# @app.route('/<name>/<surname>')
# def show_surname(name,surname):
#     return f"Name: {escape(name)}    Surname: {escape(surname)}"


# @app.route('/path/<path:subpath>')
# def show_subpath(subpath):
#     # show the subpath after /path/
#     return f'Subpath {escape(subpath)}'

@app.route('/id')
@app.route('/id/<name>')
def id(name=None):
    return render_template('id.html', name = name)
    

@app.get('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "DO LOGIN"
    
    return "SHOW LOGIN FORM"


@app.get('/login')
def login():
    return "get  login"


# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('show_id', id = 123))
    

