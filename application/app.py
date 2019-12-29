from flask import *
from flask_restful import Api

import logging
from application.config import configure_app

app = Flask(__name__)
api = Api(app,catch_all_404s=True)



__all__ = ['create_app', 'app_init_task', 'ws_init']

def create_app():
    """Initialize Flask Application"""
    app = Flask(__name__)
    configure_app(app)
    return app



@app.errorhandler(404)
def not_found(e):
    return render_template("error.html")


def init_task(api):
    from application.resources.index import Index
    from application.resources.delete import Delete
    from application.resources.insert import Insert
    from application.resources.searchbyname import SearchByName
    from application.resources.searchbycategory import SearchByCategory
    from application.resources.update import Update
    from application.resources.afterinsert import After_Insert
    from application.resources.afterupdate import After_Update
    from application.resources.afterdelete import After_Delete
    from application.resources.aftersearchbyname import After_SearchByName
    from application.resources.aftersearchbycategory import After_SearchByCategory

    api.add_resource(Index, '/')
    api.add_resource(Delete, '/delete')
    api.add_resource(Insert, '/item')
    api.add_resource(SearchByName, '/searchbyname')
    api.add_resource(SearchByCategory, '/searchbycategory')
    api.add_resource(Update, '/update')
    api.add_resource(After_Insert, '/afterinsert')
    api.add_resource(After_Update, '/afterupdate')
    api.add_resource(After_Delete, '/afterdelete')
    api.add_resource(After_SearchByName, '/aftersearchbyname')
    api.add_resource(After_SearchByCategory, '/aftersearchbycategory')


if __name__ == '__main__':
    app.run(debug=True)




