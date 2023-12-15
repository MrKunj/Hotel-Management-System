from odoo import api, models, fields


class MenuSection(models.Model):
    _name = "menu.section"
    _description = "Waiter Section to accomplish the Customer order"
    # Enter the rec name which will directly fetct and show the name on the top of the form view
    _rec_name = ""
    