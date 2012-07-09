from flask import abort, render_template

from aw.modules.pages import pages


allowed_pages = ['home', 'about', 'solutions', 'normal-distribution-calculator']



@pages.route('/application-for-everplaces')
def application_everplaces():
    resume = [
        {
            'period': '2001-2005', 
            'title': 'Studying Graphic Design at KTS (Copenhagen Technical College)',
            'body': 'Some explanation'
        },
        {
            'period': '2005-2007',
            'title': 'High School (Studenterkursus) at VUF (VoksenUddannelsesCenter Frederiksberg)',
            'body': 'Some text'
        },
        {
            'period': '2007-present',
            'title': 'Working at my company Alphabits',
            'body': 'Explaining'
        },
        {
            'period': '2009-present',
            'title': 'Studying Mathematics and Technology at DTU',
            'body': 'Explaining'
        },
        {
            'period': '2010-present',
            'title': 'Kassekladde.dk',
            'body': 'Explaining'
        }
    ]
    return render_template('pages/application-for-everplaces.html', **locals())


@pages.route('/', defaults={'page': allowed_pages[0]})
@pages.route('/<page>')
def show_page(page):
    if not page in allowed_pages:
        abort(404)
    return render_template('pages/{0}.html'.format(page), **locals())
