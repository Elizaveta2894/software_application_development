import random
import requests

BASE_URL = 'http://127.0.0.1:5000'


def send_get_request():
    param = random.randint(1, 10)
    response = requests.get(f'{BASE_URL}/number/', params={'param': param})
    if response.status_code == 200:
        data = response.json()
        print(f'GET запрос: param={param}')
        print(f'Ответ: result={data["result"]}, operation={data["operation"]}')
        return data['result'], data['operation']
    else:
        print(f'GET ошибка: {response.status_code}')
        return None, None

def send_post_request():
    json_param = random.randint(1, 10)
    headers = {'Content-Type': 'application/json'}
    payload = {'jsonParam': json_param}
    response = requests.post(f'{BASE_URL}/number/', json=payload, headers=headers)
    if response.status_code == 200:
        data = response.json()
        print(f'POST запрос: jsonParam={json_param}')
        print(f'Ответ: result={data["result"]}, operation={data["operation"]}')
        return data['result'], data['operation']
    else:
        print(f'POST ошибка: {response.status_code}')
        return None, None

def send_delete_request():
    response = requests.delete(f'{BASE_URL}/number/')
    if response.status_code == 200:
        data = response.json()
        print(f'DELETE запрос: operation={data["operation"]}')
        print(f'Ответ: result={data["result"]}')
        return data['result'], data['operation']
    else:
        print(f'DELETE ошибка: {response.status_code}')
        return None, None


def calculate_result(values):
    if not values:
        return 0
    result = values[0][0]
    print(f'\nНачальное значение: {result}')
    for i in range(1, len(values)):
        num, op = values[i]
        print(f'Выполняем операцию {i}: {result} {op} {num} = ', end='')

        if op == 'сложение':
            result = result + num
        elif op == 'вычитание':
            result = result - num
        elif op == 'умножение':
            result = result * num
        elif op == 'деление':
            result = result / num if num != 0 else result

        print(f'{result}')
    return int(result)


def main():
    results = []
    print('\n GET запрос')
    res1, op1 = send_get_request()
    if res1 is not None:
        results.append((res1, op1))

    print('\n POST запрос')
    res2, op2 = send_post_request()
    if res2 is not None:
        results.append((res2, op2))

    print('\n DELETE запрос')
    res3, op3 = send_delete_request()
    if res3 is not None:
        results.append((res3, op3))

    print('\n Результаты запросов')
    for i, (res, op) in enumerate(results, 1):
        print(f'{i}. result={res}, operation={op}')

    final_result = calculate_result(results)
    print(f'\n Итоговый результат ')
    print(f'Результат вычислений (int): {final_result}')
if __name__ == '__main__':
    main()