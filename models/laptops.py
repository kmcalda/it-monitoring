from odoo import models, fields, api

class laptops_devices(models.Model):
    _name = 'laptops.devices'

    laptop_image = fields.Binary(string='Image')
    laptop_user = fields.Many2one('res.users',string='User')
    laptop_serial_number = fields.Char(string='Serial Number')
    laptop_os = fields.Char(string='Operating System')
    laptop_brand = fields.Char(string='Brand')
    laptop_model = fields.Char(string='Model')
    laptop_processor = fields.Char(string='Processor')
    laptop_hd = fields.Char(string='HDD')
    laptop_ram = fields.Char(string='RAM')
    laptop_office = fields.Char(string='Office')
    laptop_supplier = fields.Char(string='Supplier')
    laptop_market_value = fields.Char(string='Market Value')
    laptop_purchase_date = fields.Date(string='Purchase Date')
    laptop_warranty_expiration = fields.Date(string='Warranty Expire')
    laptop_condition = fields.Char(string='Condition')
    laptop_age = fields.Char(string='Age')
