from flask import Flask, request, jsonify

app = Flask(__name__)
if __name__ == "__main__":
    app.run()

@app.route('/python_req_1', methods=['GET'])
def python_req_1():
    name = request.args.get('name')
    age = request.args.get('age')

    salary = request.form.get('salary')
    car = request.form.get('car')

    result = {
        'user_name': name,
        'user_age': age,
        'user_salary':salary,
        'user_car': car
    }

    return jsonify(result), 404


@app.route('/python_req_2', methods=['GET', 'POST'])
def python_req_2():
    model = request.args.get('model')
    title = request.args.get('title')

    price = int(request.form.get('price')) + 5000
    open_air = request.form.get('open_air')

    result = {
        'model': model,
        'title': title,
        'price': price,
        'open_air': open_air
    }

    return jsonify(result)



