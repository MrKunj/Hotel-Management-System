{
    'name': "Capple Restaurent",
    'version': '1.0',
    'category': 'Category',
    'author': 'Kunj', # This is the author_name, which we have to mention for our daily usage    
    'sequence': -100,
    'application':True,
    'depends': ['base'],
    'description': """
    To Meet the Requirement of Restaurent....
    """,
    
    # Loading all the xml files. 
    # data files always loaded at installation, also to show the effect of xml file 
    'data': [
        'security/ir.model.access.csv',
        'views/customer_view.xml',
        'wizard/customer_wizard.xml',
        'views/waiter_view.xml', 
        'views/menus.xml'
    ],
}