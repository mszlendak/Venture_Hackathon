from flask import Flask, jsonify

from .service import (get_forecasts_from_api, get_forecast_file_path,
                      save_forecast)


APP = Flask(__name__)


@APP.route('/update-forecast/<int:woe_id>', methods=['POST'])
def update_forecast(woe_id):

    try:
        data = get_forecasts_from_api(woe_id)

        if not data:
            return jsonify({"message": "No data"}), 404
    except:
        return jsonify({"message": "An error occured"}), 502

    file_path = get_forecast_file_path(woe_id)
    save_forecast(data, file_path[0], file_path[1] )

    return jsonify({"updated": "ok"}), 201
