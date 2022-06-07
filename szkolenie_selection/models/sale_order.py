from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"
    
    selection = fields.Selection(string ='Selection', selection=[('a1', 'AAA'), ('b2', 'BBB')])