from flask import render_template

from aw.modules.pages import pages


@pages.route('/<any(about,solutions,home):page>')
def show_page(page):
    return render_template('pages/{0}.html'.format(page), **locals())
