{
    'name': 'MyOdoo - szkolenie',
    'summary': 'MyOdoo - szkolenie',
    'description': '''
    Moduł szkoleniowy dla MyOdoo.pl.
    ''',
    'author': 'myOdoo.pl',
    'website': 'https://myodoo.pl',
    'category': 'Templates',
    'version': '1.0',
    'depends': ['sale', 'purchase'], #uzupełniamy 
    'data': [
        'views/fields.xml' #uzupełniamy nazwami plików
    ],
    'installable': True,
    'auto_install': False
}
