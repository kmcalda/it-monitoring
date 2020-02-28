from odoo import models, fields, api

class laptops_devices(models.Model):
    _name = 'laptops.devices'
    _description = 'Laptop record'
    _rec_name = 'laptop_model'

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
    laptop_supplier = fields.Many2one('res.partner', string='Supplier')
    laptop_market_value = fields.Float(string='Market Value', digits=(12,2))
    laptop_purchase_date = fields.Date(string='Purchase Date')
    laptop_warranty_expiration = fields.Date(string='Warranty Expire')
    laptop_condition = fields.Boolean(string='Unit in use', default=1)
    laptop_age = fields.Char(string='Age')
    laptop_note = fields.Text(string='Internal Note')
    laptop_issued = fields.Date(string='Date issued')

    _sql_constraints = [
        ('laptop_serial_number_unique',
         'unique(laptop_serial_number)',
         "Error! serial number already exist!"),
    ]

    @api.onchange('laptop_serial_number')
    def _make_uppercase(self):
        if self.laptop_serial_number:
            self.laptop_serial_number = str(self.laptop_serial_number).upper()