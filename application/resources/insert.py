from flask_restful import *
from application.common.utils import *
from application.database.queries import *
from application.database.connection import *

class Insert(Resource):
    def get(self):
        return output_html(render_template('item.html'),200)
    def post(self):
        return output_html(render_template('item.html'), 200)
