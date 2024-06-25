from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    detailed_type = fields.Selection(selection_add=[('motorcycle', 'Motorcycle')], ondelete={'motorcycle': 'set service'})
    type = fields.Selection(selection_add=[('motorcycle', 'Motorcycle')], ondelete={'motorcycle': 'set service'})

    horsepower = fields.Float()
    top_speed = fields.Float()
    torque = fields.Float()
    battery_capacity = fields.Selection([('xs', 'Small'),('Om', 'Medium'), ('Ol', 'Long'), ('xl', 'Extra Large')])
    charge_time = fields.Float()
    range = fields.Float()
    curb_weight = fields.Float()
    make = fields.Char()
    model = fields.Char()
    year = fields.Char()


    def _detailed_type_mapping(self):
        type_mapping = super()._detailed_type_mapping()
        type_mapping['motorcycle'] = 'product'
        return type_mapping
        