from flask import Flask, escape, render_template, request, url_for
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api()


values = {
    1 : {"info": "Test", "number": 1},
    2 : {"info": "Test2", "number": 2},
}

class Main(Resource):
    def get(self, id_value:int) -> dict:
        if id_value == 0:
            return values
        
        return values[id_value]
        



api.add_resource(Main, '/main/<int:id_value>')
api.init_app(app=app)
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
    

# @app.get('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         return "DO LOGIN"
    
#     return "SHOW LOGIN FORM"


# @app.get('/login')
# def login():
#     return "get  login"


# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('show_id', id = 123))
    

