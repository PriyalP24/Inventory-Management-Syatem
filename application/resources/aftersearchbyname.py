from flask_restful import *
from flask import *
from application.common.utils import *

from application.database.connection import con
from application.database.queries import SearchByName



class After_SearchByName(Resource):
    def get(self):
        pass
    def post(self):
        data = request.form['itemname']
        timezone = request.form['timezone']

        connection = con()

        if connection:
            try:
                result = SearchByName(connection, data)
                ex_time = result[0]['extime']
                timezone = time(timezone, ex_time)
                return output_html(
                    render_template('aftersearchbyname.html', message="Items Searched  succesfully", data=result, timezone=timezone), 200)
            except Exception as e:
                return output_html(render_template("error.html", error=str(e)), 200)
        else:
            return output_html(render_template("error.html", error="connectionfail"), 200)






