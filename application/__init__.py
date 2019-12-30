from .app import create_app , init_task
from application.common.utils import get_logger
from flask import render_template
from flask_restful import Api



def run_server():
    """Eventlet Server"""
    app.run(port=app.config.get('PORT'))

__all__ = ["app", "api", "cache_store", "socket", "jwt", "run_server"]

app = create_app()
api = Api(app)

init_task(api)


@app.errorhandler(404)
def not_found(e):
    return render_template("error.html" , error ="Page Not Found")



