import os.path

from main import app
from flask import request

BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
DATA_DIR = os.path.join(BASE_DIR, 'apache_log.txt')


@app.route('/perform_query', methods=['POST'])
def perform_query():
    # cmd1 = request.args.get('cmd1')
    # cmd2 = request.args.get('cmd2')
    # value1 = request.args.get('value1')
    # value2 = request.args.get('value2')
    file_name = request.args.get('file_name')

    DATA_DIR = os.path.join(BASE_DIR, file_name)

    if not os.path.isfile(DATA_DIR):
        return '', 400
    else:
        return 'файл найден', 200


    # получить параметры query и file_name из request.args, при ошибке вернуть ошибку 400
    # проверить, что файла file_name существует в папке DATA_DIR, при ошибке вернуть ошибку 400
    # с помощью функционального программирования (функций filter, map), итераторов/генераторов сконструировать запрос
    # вернуть пользователю сформированный результат
    return app.response_class('', content_type="text/plain")