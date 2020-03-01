from odoo import models, fields, api

class laptops_devices(models.Model):
    _name = 'laptops.devices'
    _description = 'Laptop record'
    _rec_name = 'laptop_model'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    laptop_image = fields.Binary(string='Image')
    laptop_user = fields.Many2one('res.users',string='User', track_visibility='always', required=1, ondelete='set null')
    laptop_serial_number = fields.Char(string='Serial Number', track_visibility='always', required=1)
    laptop_os = fields.Char(string='Operating System', track_visibility='always')
    laptop_brand = fields.Char(string='Brand', track_visibility='always')
    laptop_model = fields.Char(string='Model name', track_visibility='always', required=1)
    laptop_processor = fields.Char(string='Processor', track_visibility='always')
    laptop_hdd = fields.Char(string='HDD', track_visibility='always')
    laptop_ram = fields.Char(string='RAM', track_visibility='always')
    laptop_office = fields.Char(string='Office', track_visibility='always')
    laptop_supplier = fields.Many2one('res.partner', string='Supplier', track_visibility='always', ondelete='set null')
    laptop_market_value = fields.Float(string='Market Value', digits=(12,2), track_visibility='always')
    laptop_purchase_date = fields.Date(string='Purchase Date', track_visibility='always')
    laptop_warranty_expiration = fields.Date(string='Warranty Expire', track_visibility='always')
    laptop_condition = fields.Boolean(string='Unit in use', default=1)
    laptop_age = fields.Char(string='Age')
    laptop_note = fields.Text(string='Internal Note')
    laptop_issued = fields.Date(string='Date issued', track_visibility='always')

    _sql_constraints = [
        ('laptop_serial_number_unique',
         'unique(laptop_serial_number)',
         "Error! serial number already exist!"),
    ]

    @api.onchange('laptop_serial_number')
    def _make_uppercase_serial(self):
        if self.laptop_serial_number:
            self.laptop_serial_number = str(self.laptop_serial_number).upper()

    @api.onchange('laptop_brand')
    def _make_uppercase_brand(self):
        if self.laptop_brand:
            self.laptop_brand = str(self.laptop_brand).upper()

    @api.onchange('laptop_hdd')
    def _make_uppercase_hdd(self):
        if self.laptop_hdd:
            self.laptop_hdd = str(self.laptop_hdd).upper()

    @api.onchange('laptop_ram')
    def _make_uppercase_ram(self):
        if self.laptop_ram:
            self.laptop_ram = str(self.laptop_ram).upper()
