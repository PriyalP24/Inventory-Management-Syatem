__all__ = ['Config']








def Config(app):
    app.config['SECRET_KEY'] = "secret_key"
    app.config['HOST'] = "localhost"
    app.config['USER'] = "root"
    app.config['PASSWORD'] = "root123"
    app.config['DATABASE_NAME'] = "inventory"




