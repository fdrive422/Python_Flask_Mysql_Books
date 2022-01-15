from flask_app import app

from flask_app.controllers import books
from flask_app.controllers import authors

if __name__=='__main__':
    app.run(debug=True)