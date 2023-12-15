from odoo import api, models, fields


class WaiterSection(models.Model):
    _name = "waiter.section"
    _description = "Waiter Section to accomplish the Customer order"
    # Enter the rec name which will directly fetct and show the name on the top of the form view
    _rec_name = "customer_name_id"

    # Get the name of the Regestered Customer By Many2One relation fields
    # After selecting the customer by the waiter, Waiter will allocate the seat number (Dinning Table number)
    # After selecting the customer by the waiter, The waiter will able to see all the memebers of that person

    # 1) Customer name, Customer Phone Number
    # 2) Other Member's name Who are come with the customer, and There Phone Number
    # 3) The list of food must be come from Menu Model using the concept of Many2many Field.


    # Creating Many2One Field.
    # 1) Give the name of that model from where we have to fetch the names of the customer who were register. 
    # 2) So that's why we are giving the model name as --> customer.section    
    customer_name_id = fields.Many2one('customer.section')
    customer_Phone = fields.Char(related="customer_name_id.customer_phoneNumber")
    



        
