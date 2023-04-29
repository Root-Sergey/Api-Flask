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

    return jsonify(result)

