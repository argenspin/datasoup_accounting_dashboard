{
    'name': "Accounting Dashboard",
    'author': 'Datasoup',
    'version': "16.0.1.0",
    'depends': ['base','account'],
    'data': [
        'security/groups.xml',
        'views/dashboard_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'datasoup_accounting_dashboard/static/src/scss/style.scss',
            'datasoup_accounting_dashboard/static/lib/bootstrap-toggle-master/css/bootstrap-toggle.min.css',
            'datasoup_accounting_dashboard/static/src/js/account_dashboard.js',
            'datasoup_accounting_dashboard/static/lib/Chart.bundle.js',
            'datasoup_accounting_dashboard/static/lib/Chart.bundle.min.js',
            'datasoup_accounting_dashboard/static/lib/Chart.min.js',
            'datasoup_accounting_dashboard/static/lib/Chart.js',
            'datasoup_accounting_dashboard/static/lib/bootstrap-toggle-master/js/bootstrap-toggle.min.js',
            'datasoup_accounting_dashboard/static/src/xml/template.xml',
        ],
    },
    'demo': [],
    'summary': "Accounting Dashbaord by Datasoup",
    'description': "",
    'installable': True,
    'auto_install': False,
    'license': "LGPL-3",
    'application': False
}