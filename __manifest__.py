# -*- coding: utf-8 -*-
{
    'name': "account_statement_import_txt_xlsx_bank_knab",

    'summary': """
        Bank statement import for KNAB""",

    'description': """
        Bank statement import for KNAB
    """,

    'author': "Bert Driehuis",
    'website': "https://github.com/driehuis/account_statement_import_txt_xlsx_bank_knab",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Accounting',
    'version': '0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account', 'account_statement_import_txt_xlsx'],

    # always loaded
    'data': [
        'data/statement-import-template-knab.xml',
    ],
}
