from odoo import models, fields, api

class printers_devices(models.Model):
    _name = 'printers.devices'

    printer_user = fields.Char(string='User')
    printer_image = fields.Binary(string='Image')
    printer_serial_number = fields.Char(string='Serial Number')
    printer_brand = fields.Char(string='Brand')
    printer_model = fields.Char(string='Model')
    printer_supplier = fields.Char(string='Supplier')
    printer_market_value = fields.Char(string='Market Value')
    printer_purchase_date = fields.Datetime(string='Purchase Date')
    printer_warranty_expiration = fields.Datetime(string='Warranty Expiration')
    printer_condition = fields.Char(string='Condition')
    printer_age = fields.Char(string='Age')