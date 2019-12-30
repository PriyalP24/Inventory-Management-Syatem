from flask_restful import *
from flask import *
from application.common.utils import *

class Update(Resource):
    def get(self):
        return output_html(render_template('update.html'),200)
    def post(self):
        return output_html(render_template('update.html'), 200)

