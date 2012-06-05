from aw.utils import create_blueprint


pages = create_blueprint('pages', __name__)
from .views import *
