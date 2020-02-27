from odoo import fields, models, api


class desktops_devices(models.Model):
    _name = 'desktops.devices'
    _description = 'Desktop record'
    _rec_name = 'desktop_model'

    desktop_user = fields.Many2one('res.users', string='User')
    desktop_image = fields.Binary(string='Image')
    desktop_serial_number = fields.Char(string='Serial Number')
    desktop_model = fields.Char(string='Model')
    desktop_os = fields.Char(string='Operating System')
    desktop_processor = fields.Char(string='Processor')
    desktop_hd = fields.Char(string='HDD')
    desktop_ram = fields.Char(string='RAM')
    desktop_office = fields.Char(string='Office')
    desktop_supplier = fields.Char(string='Supplier')
    desktop_market_value = fields.Float(string='Market Value', digit=(12,2))
    desktop_purchase_date = fields.Date(string='Purchase Date')
    desktop_warranty_expiration = fields.Date(string='Warranty Expiration')
    desktop_condition = fields.Char(string='Condition')
    desktop_age = fields.Char(string='Age')
    desktop_issued = fields.Date(string='Date issued')

    _sql_constraints = [
        ('desktop_serial_number_unique',
         'unique(desktop_serial_number)',
         "Error! serial number already exist!"),
    ]

    @api.onchange('desktop_serial_number')
    def _make_uppercase(self):
        if self.desktop_serial_number:
            self.desktop_serial_number = str(self.desktop_serial_number).upper()