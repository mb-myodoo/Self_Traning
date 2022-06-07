from odoo import api, fields, models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order" #odwołujemy się do nazwy klasy z której dziedziczymy 
    
    selection = fields.Selection(string ='Selection', selection=[('a1', 'AAA'), ('b2', 'BBB')])