from flask_restful import *
from flask import *
from application.common.utils import *

from application.database.connection import con
from application.database.queries import SearchByCategory



class After_SearchByCategory(Resource):
    def get(self):
        pass



    def post(self):
        data = request.form['itemcategory']
        t = request.form['timezone']


        connection = con()


        if connection:
            try:
                result = SearchByCategory(connection, data)
                ex_time = result[0]['extime']
                t = time(t,ex_time)
                return output_html(
                    render_template('aftersearchbycategory.html', message="Items Searched  succesfully", data=result,t=t), 200)
            except Exception as e:

                return output_html(render_template("error.html", error=str(e)), 200)
        else:
            return output_html(render_template("error.html", error="connectionfail"), 200)






