# -*- coding:utf-8 -*-
# __author__ = 'li.zh'
from api_sport import sport_info
from flask import jsonify
from flask import Blueprint

sport = Blueprint("sport", __name__)


@sport.route("/sport", methods=['GET', 'POST'])
def show():
    result = sport_info.search()
    return jsonify(result)
