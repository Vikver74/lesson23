from flask import Flask, request
import os.path
from utils import get_filter, get_map, get_unique, get_sort, get_limit


app = Flask(__name__)


BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')


@app.route('/perform_query', methods=['POST'])
def perform_query():
    cmd1 = request.form.get('cmd1')
    cmd2 = request.form.get('cmd2')
    value1 = request.form.get('value1')
    print(f'value1:   {value1}')
    value2 = request.form.get('value2')

    value = [value1, value2]
    cmd = [cmd1, cmd2]

    file_name = request.form.get('file_name')

    if file_name:
        data_path = os.path.join(BASE_DIR, file_name)
    else:
        return f'файл {file_name} не найден', 400

    if not os.path.isfile(data_path):
        return f'файл {file_name} не найден', 400

    # if len(cmd) > 0:
    #     for item in cmd:

    choice_func = {
        'filter': [get_filter, data_path, value1],
        'map': [get_map, data_path, int(value2)],
        'unique': [get_unique, data_path, value1],
        'sort': [get_sort, data_path, value1],
        'limit': [get_limit,data_path, int(value2)]
    }
    # choice_func[cmd1][0](choice_func[cmd1][1], choice_func[cmd1][2])
    # func = choice_func[cmd1]
    # func[0](func[1], func[2])

    if cmd1:
        func = choice_func[cmd1]
        func[0](func[1], func[2])


    # if cmd1 == 'filter':
    #     get_filter(data_path, value1)
    #
    # if cmd1 == 'map':
    #     get_map(data_path, int(value1))
    #
    # if cmd1 == 'unique':
    #     get_unique(data_path)
    #
    # if cmd1 == 'sort':
    #     get_sort(data_path, value1)
    #
    # if cmd1 == 'limit':
    #     get_limit(data_path, int(value1))

    # return '', 200


    # получить параметры query и file_name из request.args, при ошибке вернуть ошибку 400
    # проверить, что файла file_name существует в папке DATA_DIR, при ошибке вернуть ошибку 400
    # с помощью функционального программирования (функций filter, map), итераторов/генераторов сконструировать запрос
    # вернуть пользователю сформированный результат
    return app.response_class('', content_type="text/plain")


if __name__ == '__main__':
    app.run()


