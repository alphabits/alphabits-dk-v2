from flask import render_template

from aw.modules.pages import pages


@pages.route('/<page>')
def show_page(page):
    code = 'import this\n\ndef me():\n    return code'
    return render_template('pages/page.html', **locals())
