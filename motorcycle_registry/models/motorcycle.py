import re
from odoo import api, models, fields
import datetime
from odoo.exceptions import ValidationError

class MotorcycleRegistry(models.Model):
    _name = "motorcycle.registry"
    _description = "Motorcycle Registry"
    _rec_name = "registry_number"
    
    certificate_title = fields.Binary()
    current_mileage = fields.Float()
    date_registry = fields.Date()
    first_name = fields.Char(required=True)
    last_name = fields.Char()
    license_plate = fields.Char()
    registry_number = fields.Char(string="Registry Number", default="MNR0000", copy=False, required=True, readonly=True)
    vin = fields.Char(required=True)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('registry_number', ('MNR0000')) == ('MNR0000'):
                vals['registry_number'] = self.env['ir.sequence'].next_by_code('registry.number')
        return super().create(vals_list)

#class Session(models.Model):
#    _name="motorcycle.session"
#    _description="Motorcycle Session Info"
#    _sql_constraints= [('vin_unique', 'UNIQUE(vin)', 'Error Message.')]

#    name = fields.Char(string="Title")
#    registry_number = fields.Char(string="Registry Number", default="MNR0000", copy=False, required=True, readonly=True)

    @api.constrains('license_plate')
    def _check_license_plate_size(self):
        pattern = '^[A-Z]{1,3}\\d{1,4}[A-Z]{0,2}$'
        for registry in self.filtered(lambda r: r.license_plate):
            match = re.match(pattern, registry.license_plate)
            if not match:
                raise ValidationError('Invalid License Plate')
 
    @api.constrains('vin')
    def _check_vin_pattern(self):
        pattern = '^[A-Z]{4}\\d{2}[A-Z0-9]{2}\\d{5}$'
        for registry in self.filtered(lambda r: r.vin):
            match = re.match(pattern, registry.vin)
            if not match:
                raise ValidationError('Invalid VIN')
            if not registry.vin[0:2] == 'KA':
                raise ValidationError('Only motorcycles from Kawil Motors are allowed')

#class Session(models.Model):
#    _name="motorcycle.session"
#    _description="Motorcycle Session Info"
#    _sql_constraints= [('vin_unique', 'UNIQUE(vin)', 'Error Message.')]

#    name = fields.Char(string="Title")
#    registry_number = fields.Char(string="Registry Number", default="MNR0000", copy=False, required=True, readonly=True)

#    @api.model_create_multi
#    def create(self, vals_list):
#        for vals in vals_list:
#            if vals.get('registry_number', ('MNR0000')) == ('MNR0000'):
#                vals['registry_number'] = self.env['ir.sequence'].next_by_code('registry.number')
#        return super().create(vals_list)

#    @api.constrains('license_plate')
#    def _check_license_plate_size(self):
#       pattern = '^[A-Z]{1,3}/d{1,4}[A-Z]{0,2}$'
#        for registry in self.filtered(lambda r: r.license_plate):
#            match = re.match(pattern, registry.license_plate)
#            if not match:
#                raise ValidationError('Invalid License Plate')
 
#    @api.constrains('vin')
#    def _check_vin_pattern(self):
#        pattern = '^[A-Z]{4}/d{2}[A-Z0-9]{2}/d{5}$'
#        for registry in self.filtered(lambda r: r.vin):
#           match = re.match(pattern, registry.vin)
#            if not match:
#                raise ValidationError('Invalid VIN')
#            if not registry.vin[0:2] == 'KA':
#                raise ValidationError('Only motorcycles from Kawil Motors are allowed')
    

#    @api.constrains('license_plate')
#    def _check_license_plate_size(self):
#        pattern = '^[A-Z]{1,3}\d{1,4}[A-Z]{0,2}$'
#        for registry in self.filtered(lambda r: r.license_plate):
#            match = re.match(pattern, registry.license_plate)
#            if not match:
#                raise ValidationError('Invalid License Plate')
 
#    @api.constrains('vin')
#    def _check_vin_pattern(self):
#        pattern = '^[A-Z]{4}\d{2}[A-Z0-9]{2}\d{5}$'
#        for registry in self.filtered(lambda r: r.vin):
#            match = re.match(pattern, registry.vin)
#            if not match:
#                raise ValidationError('Invalid VIN')
#            if not registry.vin[0:2] == 'KA':
#                raise ValidationError('Only motorcycles from Kawil Motors are allowed')