from flask_restful import *

from application.common.utils import *

from application.database.connection import con
from application.database.queries import update


class After_Update(Resource):
    def get(self):
        pass
    def post(self):

        inventory_id=request.form['id']
        quantity = request.form['quantity']



        connection = con()

        if connection:
            try:
                update(connection,quantity,inventory_id)
                return output_html(render_template('response.html',message="Item updated succesfully"),200)
            except Exception as e:
                return output_html(render_template("error.html",error=str(e)),200)
        else:
            return output_html(render_template("error.html",error="connection fail"),200)

