from aw.utils import create_blueprint


blog = create_blueprint('blog', __name__)
from .views import *
