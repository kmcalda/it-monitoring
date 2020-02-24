from odoo import fields, models, api


class desktops_devices(models.Model):
    _name = 'desktops.devices'

    desktop_user = fields.Char(string='User')
    desktop_image = fields.Binary(string='Image')
    desktop_serial_number = fields.Char(string='Serial Number')
    desktop_model = fields.Char(string='Model')
    desktop_os = fields.Char(string='Operating System')
    desktop_processor = fields.Char(string='Processor')
    desktop_hd = fields.Char(string='HDD')
    desktop_ram = fields.Char(string='RAM')
    desktop_office = fields.Char(string='Office')
    desktop_supplier = fields.Char(string='Supplier')
    desktop_market_value = fields.Char(string='Market Value')
    desktop_purchase_date = fields.Datetime(string='Purchase Date')
    desktop_warranty_expiration = fields.Datetime(string='Warranty Expiration')
    desktop_condition = fields.Char(string='Condition')
    desktop_age = fields.Char(string='Age')
    desktop_issued = fields.Datetime(string='Date issued')