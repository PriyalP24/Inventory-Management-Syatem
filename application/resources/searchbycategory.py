from flask_restful import *
from flask import *
from application.common.utils import *

class SearchByCategory(Resource):
    def get(self):
        return output_html(render_template('searchbycategory.html'), 200)
    def post(self):
        return output_html(render_template('searchbycategory.html'), 200)

