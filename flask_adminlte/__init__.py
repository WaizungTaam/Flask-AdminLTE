from flask import Blueprint
from flask_admin import Admin


class AdminLTE(object):
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        admin = Admin(template_mode='bootstrap4',
            base_template='adminlte/base.html')
        admin.init_app(app)
        self.admin = admin

        blueprint = Blueprint('adminlte', __name__,
            template_folder='templates',
            static_folder='static',
            static_url_path=app.static_url_path + '/adminlte')
        app.register_blueprint(blueprint)
