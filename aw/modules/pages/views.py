from flask import render_template

from aw.modules.pages import pages


@pages.route('/')
@pages.route('/<any(about,solutions,home):page>')
def show_page(page=None):
    if page is None:
        page = 'home'
    return render_template('pages/{0}.html'.format(page), **locals())
