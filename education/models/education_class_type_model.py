from odoo import fields, api, models

class EducationClassType(models.Model):
    _name="education.class"
    _inherit = "education.class"
    _description="extend class model"
    class_size = fields.Integer("Number of limit student")

    