from flask import Flask, jsonify, request
# Importo de la librería flask el constructor Flask

from src.db.load_data import load_data
# Importo la función load_data para mostrar la información que contiene el archivo csv

from src.db.save_data import save_data
# Importo la función save data para almacenar lo que ingresa mediante el método HTTP POST

import statistics

app = Flask(__name__)
# Con el constructor creo una instancia de un objeto especial y la guardo en la variable app

data = load_data()

# [POST]
@app.route('/api/prometheus/statistics', methods=['POST'])
def create_stat():
    req_json = request.json
    try:
        save_data(req_json)

    except KeyError as key_err:
        missing_param = (key_err.__str__())
        return jsonify(
            error_code=400,
            error_description="Bad request",
            error_body=missing_param
        ), 400

    return jsonify({'blood_data': req_json})


# [GET]
@app.route('/api/prometheus/statistics', methods=['GET'])
def get_all_stats():
    return jsonify({'case': [case.serialize() for case in data], 'status': 'ok'})


# [GET]
@app.route('/api/prometheus/statistics/reports', methods=['GET'])
def get_reports():
    date_param = request.args.get('report_date', '')

    date_blood_sugar_level = []
    date_emotion_level = []

    if date_param == '':
        return jsonify(error_code=400, error_description='Missing mandatory param'), 400

    else:
        for report in data:
            if report.date == date_param:
                date_blood_sugar_level.append(int(report.blood_sugar_level))
                date_emotion_level.append(int(report.emotion_level))
            else:
                continue

        return jsonify({'avg_blod_sugar_level': round(statistics.mean(date_blood_sugar_level), 2),
                        'avg_emotion_level': round(statistics.mean(date_emotion_level), 2)
                        })


if __name__ == '__main__':
    app.run(debug=True, port=5000)
