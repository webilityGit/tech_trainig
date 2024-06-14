from odoo import models, fields
import datetime

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
    registry_number = fields.Char(required=True)
    vin = fields.Char(required=True)