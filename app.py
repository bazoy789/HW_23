from flask import Flask

from views import bp_pars


def create_app():
    app = Flask(__name__)
    app.register_blueprint(bp_pars)
    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
