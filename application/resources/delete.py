from flask_restful import *
from flask import *
from application.common.utils import *
from application.database.queries import select
from application.database.connection import con

class Delete(Resource):
    def get(self):
        connection = con()
        data = select(connection)

        return output_html(render_template('delete.html',data=data),200)
    def post(self):
        connection = con()
        data = select(connection)


        return output_html(render_template('delete.html',data=data), 200)

