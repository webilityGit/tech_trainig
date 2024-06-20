import re
from odoo import api, models, fields
import datetime
from odoo.exceptions import ValidationError

class MotorcycleRegistry(models.Model):
    _name = "motorcycle.registry"
    _description = "Motorcycle Registry"
    _rec_name = "registry_number"
    _sql_constraints= [('vin_unique', 'UNIQUE(vin)', 'The VIN number needs to be unique.')]
    
    certificate_title = fields.Binary()
    current_mileage = fields.Float()
    date_registry = fields.Date()
    license_plate = fields.Char()
    registry_number = fields.Char(string="Registry Number", default="MNR0000", copy=False, required=True, readonly=True)
    vin = fields.Char(required=True)
    owner_id = fields.Many2one(comodel_name="res.partner", string="Owner")
    email = fields.Char(related="owner_id.email")
    phone = fields.Char(related="owner_id.phone")
    make = fields.Char(compute="_compute_from_vin")
    model = fields.Char(compute="_compute_from_vin")
    year = fields.Char(compute="_compute_from_vin")
    

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

    @api.depends('vin')
    def _compute_from_vin(self):
        registries_with_vin = self.filtered(lambda r: r.vin)
        registries_with_vin._check_vin_pattern()
        for registry in registries_with_vin:
            registry.make = registry.vin[:2]
            registry.model = registry.vin[2:4]
            registry.year = registry.vin[4:6]
        for registry in (self - registries_with_vin):
            registry.make = False
            registry.model = False
            registry.year = False
                
#    @api.depends("vin")
#    def _compute_make(self):
#        for record in self:
#            if record:
#                record.make = record.vin[0:2]

#    @api.depends("vin")
#    def _compute_model(self):
#        for record in self:
#            record.model = record.vin[2:4]

#    @api.depends("vin")
#    def _compute_year(self):
#        for record in self:
#            record.year = record.vin[4:6]
    

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