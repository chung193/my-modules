from odoo import fields, api, models

class EducationClassType(models.Model):
    _name="education.class"
    _inherit = "education.class"
    _description="extend class model"
    class_size = fields.Integer
    is_international = fields.Boolean("is international class")
    language = fields.Selection(
        selection=[("english","English"),("china","China"), ("france","France")]
    )
    