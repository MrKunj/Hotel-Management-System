from odoo import api, models, fields

class CustomerWizard(models.TransientModel):
    _name = "customer.wizard"
    _description = "Store Details of all the checked-in customer"
    _rec_name = "customer_name_id"

    customer_name_id = fields.Many2one('customer.section', string="Customer Name")
    
    # TO Delete Record 
    def deleteCustomerRecord(self):
        checker = self.env['customer.section'].search([('id', '=', self.customer_name_id.id)])
        todlt = self.env['customer.section'].browse(checker.id)
        todlt.unlink()
    