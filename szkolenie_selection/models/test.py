from odoo import api, fields, models


class Test(models.Model):
    _name = "test"
    _description = "Test"
    
    name = fields.Char(string='name', required=True, default="Unknown")
    description = fields.Text(string='decsripion')
    postalcode = fields.Char(string='postalcode')
    date = fields.Datetime(string='date', default=lambda self: fields.Datetime.today())
    price = fields.Float(string='price', required=True)
    bedrooms = fields.Integer(string='bedrooms')
    garage = fields.Boolean(string='garage')
    garden_orientation = fields.Selection(string='garden orientation', selection=[('e', 'East'), ('w', 'West'), ('n', 'Norht'), ('s', 'South')])
