from flask import Blueprint


def create_blueprint(name, package):
    return Blueprint(name, package, template_folder='templates',
            static_folder='static')
