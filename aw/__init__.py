from datetime import datetime

from flask import Flask

from aw.lib.pygments_extension import PygmentsExtension
from aw.modules.blog import blog
from aw.modules.pages import pages


def build_app(debug=False):
    app = Flask(__name__)
    app.register_blueprint(blog, url_prefix='/blog')
    app.register_blueprint(pages)
    ext_name = "aw.lib.pygments_extension.PygmentsExtension"
    app.jinja_env.extensions[ext_name] = PygmentsExtension(app.jinja_env)
    @app.context_processor
    def inject_now():
        return dict(now=datetime.now())
    return app
