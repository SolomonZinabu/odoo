{
    'name': 'Employee Asset Management',
    'version': '1.0',
    'summary': 'Track company assets assigned to employees',
    'author': 'Solomon Zinabu',
    'category': 'Human Resources',
    'license': 'LGPL-3',  # <-- Add this line
    'depends': ['base', 'hr'],  # hr module for employee linking
    'data': [
        # 'data/employee_asset_model.xml',
        'views/asset_view.xml',
        'security/ir.model.access.csv',    
    ],
    'installable': True,
    'application': True,
}
