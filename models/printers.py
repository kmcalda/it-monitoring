from odoo import models, fields, api


class printers_devices(models.Model):
    _name = 'printers.devices'
    _description = 'for printers'
    _rec_name = 'printer_user'

    printer_user = fields.Many2one('res.users', string='User')
    printer_image = fields.Binary(string='Image')
    printer_serial_number = fields.Char(string='Serial Number', required=1)
    printer_brand = fields.Char(string='Brand')
    printer_model = fields.Char(string='Model')
    printer_supplier = fields.Char(string='Supplier')
    printer_market_value = fields.Float(string='Market Value', digits=(12, 2))
    printer_purchase_date = fields.Date(string='Purchase Date')
    printer_warranty_expiration = fields.Date(string='Warranty Expiration')
    printer_condition = fields.Char(string='Condition')
    printer_age = fields.Char(string='Age')

    _sql_constraints = [
        ('printer_serial_number_unique',
         'unique(printer_serial_number)',
         "Error! serial number already exist!"),
    ]

    @api.onchange('printer_serial_number')
    def _make_uppercase(self):
        if self.printer_serial_number:
            self.printer_serial_number = str(self.printer_serial_number).upper()
