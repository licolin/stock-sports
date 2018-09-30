# -*- coding:utf-8 -*-
# __author__ = 'li.zh'


from flask import Flask


def create_app():
    app = Flask(__name__)
    regester_blueprint(app)
    return app


def regester_blueprint(app):
    from app.sports import sport
    from app.stocks import stock
    app.register_blueprint(sport)
    app.register_blueprint(stock)
