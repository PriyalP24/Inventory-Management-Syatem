from flask_restful import *

from application.common.utils import time

from application.database.connection import con
from application.database.queries import SearchByCategory



class After_TimeZone(Resource):
    def get(self):
        pass



    def post(self):

        time = request.form['timezone']

        connection = con()
        time = time(time)
        print(time)
        if connection:
            try:
                result = SearchByCategory(connection, data)
                return output_html(
                    render_template('aftersearchbycategory.html', message="Items Searched  succesfully", time=time), 200)
            except Exception as e:
                return output_html(render_template("error.html", error=str(e)), 200)
        else:
            return output_html(render_template("error.html", error="connectionfail"), 200)






