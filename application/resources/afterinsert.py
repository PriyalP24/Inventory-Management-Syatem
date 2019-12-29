from flask_restful import *

from application.common.utils import *
import os
from application.database.connection import con
from application.database.queries import insert


class After_Insert(Resource):
    def get(self):
        pass
    def post(self):
        file=open("common/data.txt","r")
        id=file.read()

        name = request.form['name']
        category = request.form['category']
        extime = request.form['expirytime']
        quantity = request.form['quantity']
        mnftime = request.form['manufacturingtime']
        image = request.files['image']

        filename = "image" + str(id) + '.' + image.filename.rsplit('.', 1)[1].lower()

        path = os.path.dirname(os.path.abspath(__file__))
        image.save(os.path.join(os.path.join(path, '../statics/images/'), filename))
        image_path = os.path.join(os.path.join(path, '../statics/images/'), filename)
        print("extime before conversion :", extime)
        extime = datetime1(extime)
        print("extime after conversion :",extime)
        mnftime = datetime1(mnftime)


        connection = con()

        if connection:
            try:
                insert(connection,name,extime,mnftime,image_path,quantity,category)
                id= str(int(id) +1)
                file=open("common/data.txt","w")
                file.write(id)
                return output_html(render_template('response.html',message="Item added succesfully"+image_path),200)
            except Exception as e:
                return output_html(render_template("error.html",error=str(e)),200)
        else:

            return output_html(render_template("error.html",error="Connection fails"),200)

