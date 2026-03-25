import random
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/number/', methods=['GET'])
def get_number():

    param = request.args.get('param', type=int)
    if param is None:
        return jsonify({'error': 'Параметр param обязателен'}), 400

    random_number = random.randint(1, 100)
    result = random_number * param
    operation = 'умножение'

    return jsonify({
        'result': result,
        'operation': operation,
        'random_number': random_number,
        'param': param
    })


@app.route('/number/', methods=['POST'])
def post_number():
    data = request.get_json()
    if data is None:
        return jsonify({'error': 'Требуется JSON в теле запроса'}), 400

    json_param = data.get('jsonParam')
    if json_param is None:
        return jsonify({'error': 'Поле jsonParam обязательно'}), 400

    random_number = random.randint(1, 100)
    result = random_number * json_param
    operation = 'умножение'

    return jsonify({
        'result': result,
        'operation': operation,
        'random_number': random_number,
        'jsonParam': json_param
    })


@app.route('/number/', methods=['DELETE'])
def delete_number():
    random_number = random.randint(1, 100)
    operations = ['сложение', 'вычитание', 'умножение', 'деление']
    operation = random.choice(operations)

    return jsonify({
        'result': random_number,
        'operation': operation,
        'random_number': random_number
    })
if __name__ == '__main__':
    app.run(debug=True, port=5000)