from odoo import models, fields, api


class printers_devices(models.Model):
    _name = 'printers.devices'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Printer record'
    _rec_name = 'printer_model'

    printer_user = fields.Many2one('res.users', string='User', required=True, track_visibility='always')
    printer_image = fields.Binary(string='Image')
    printer_serial_number = fields.Char(string='Serial Number', required=1, track_visibility='always')
    printer_brand = fields.Char(string='Brand', track_visibility='always')
    printer_model = fields.Char(string='Model name', track_visibility='always')
    printer_supplier = fields.Many2one('res.partner', string='Supplier', track_visibility='always')
    printer_market_value = fields.Float(string='Market Value', digits=(12, 2), track_visibility='always')
    printer_purchase_date = fields.Date(string='Purchase Date', track_visibility='always')
    printer_warranty_expiration = fields.Date(string='Warranty Expiration', track_visibility='always')
    printer_condition = fields.Boolean(string='Unit in use', default=1)
    printer_age = fields.Char(string='Age')
    printer_comment = fields.Text(string='Internal Comment')
    printer_location = fields.Selection([('LMS', 'LMS(Laguna)'), ('HO',
                                                                 'HO(Head Office)')], default='LMS', string='Location')

    _sql_constraints = [
        ('printer_serial_number_unique',
         'unique(printer_serial_number)',
         "Error! serial number already exist!"),
    ]

    @api.onchange('printer_serial_number')
    def _make_uppercase(self):
        if self.printer_serial_number:
            self.printer_serial_number = str(self.printer_serial_number).upper()

    @api.onchange('printer_brand')
    def _make_uppercase(self):
        if self.printer_brand:
            self.printer_brand = str(self.printer_brand).upper()
