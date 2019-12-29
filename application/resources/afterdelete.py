from flask_restful import *

from application.common.utils import *

from application.database.connection import con
from application.database.queries import delete



class After_Delete(Resource):
    def get(self):
        pass
    def post(self):
        logger = get_logger()
        data = request.form['id_to_delete']
        print(data)

        connection = con()

        if connection:
            try:
                delete(connection, data)
                import os
                path = os.path.dirname(os.path.abspath(__file__))
                path2 = "../statics/images/image" + str(data) + '.jpeg'
                file = os.path.join(path, path2)
                os.remove(file)
                logger.debug("Images deleted successfully from local directory")
                return output_html(render_template('response.html', message="Items Deleted succesfully"), 200)
            except Exception as e:
                return output_html(render_template("error.html", error=str(e)), 200)
        else:
            return output_html(render_template("error.html", error="connection fail"), 200)




