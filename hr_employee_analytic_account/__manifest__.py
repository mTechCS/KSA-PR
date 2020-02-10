# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Employee Analytic Accounting',
    'version': '1.0',
    'category': 'Human Resources',
	'author' : 'Me',
    'description': """This module lets you choose the analytic account in the employee screen for a specific salary rule""",
    'depends': ['hr','hr_payroll_account'],
    'website':'http://www.mycompany.com/',
    'data': ['views/hr_payroll_analytic_account_view.xml'],
    'demo': [],
    'installable': True,
    'auto_install': False,
}

