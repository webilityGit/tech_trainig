import re
from odoo import api, fields, models

class Session(models.Model):
    _name="motorcycle.session"
    _description="Motorcycle Session Info"
#    _sql_constraints= [('vin_unique', 'UNIQUE(vin)', 'Error Message.')]

    name = fields.Char(string="Title")

    registry_number = fields.Char(string="Registry Number", default="MNR0000", copy=False, required=True, readonly=True)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('registry_number', ('MNR0000')) == ('MNR0000'):
                vals['registry_number'] = self.env['ir.sequence'].next_by_code('registry.number')
        return super().create(vals_list)

    @api.constrains('license_plate')
    def _check_license_plate_size(self):
        pattern = '^[A-Z]{1,3}/d{1,4}[A-Z]{0,2}$'
        for registry in self.filtered(lambda r: r.license_plate):
            match = re.match(pattern, registry.license_plate)
            if not match:
                raise ValidationError('Invalid License Plate')
 
    @api.constrains('vin')
    def _check_vin_pattern(self):
        pattern = '^[A-Z]{4}/d{2}[A-Z0-9]{2}/d{5}$'
        for registry in self.filtered(lambda r: r.vin):
            match = re.match(pattern, registry.vin)
            if not match:
                raise ValidationError('Invalid VIN')
            if not registry.vin[0:2] == 'KA':
                raise ValidationError('Only motorcycles from Kawil Motors are allowed')

#    @api.constrains
#    def vin_number(self, self.vin):
#        record = self.browse(self.vin)
#        pattern = '^[A-Z]{4}\d{2}[A-Z0-9]{2}\d{5}$'
#        for data in record:
#            if re.match(pattern, data.vin) == None:
#                retrun False
#        return data.vin

    