from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return """
Tamal Kundu \n
Shukla Kundu \n
Payal Kundu \n
Thakur Das Kundu \n
Rinki Kundu \n
"""


@app.route('/tamal')
def tamal_function():
    return "Tamal works in tcs, and mainly works in server engineer. "

@app.route('/bye')
def bye():
    a = ["Tamal Kundu",
         "shukla Kundu",
         "Thakur das Kundu"]
    b = ["Python", "Fun"]
    return a+b

@app.route('/json_format')
def json_data():
    retjson = {
        'name': 'Tamal',
        'age': 32,
        'phones': [
            {
                'phoneName': 'redmi',
                'sim com': 'airtle',
                'num': 8972014763
            },
            {
                'phoneName': 'redmi',
                'sim com': 'jio',
                'num': 9635068723
            }
        ]
    }
    return retjson
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)