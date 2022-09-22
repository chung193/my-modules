from odoo import api, models, fields

class EducationClassSize(models.Model):
    _name="education.class"
    _inherit = "education.class"
    _description="Extend class, defined class size"
    
    size = fields.Integer("class size", default=20)