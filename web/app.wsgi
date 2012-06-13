import site
site.addsitedir('/home/anders/alphabits.dk/env-aw/lib/python2.6/site-packages')
import sys
sys.path.append('/home/anders/alphabits.dk')

from aw import build_app


app = build_app()
