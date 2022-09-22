from odoo import models, fields, api

class EducationCompany(models.Model):
    _name="education.company"
    _description="Company support for school"
    
    name=fields.Char("Name of company")
    # from_date = fields.Date("When company start support for school")
    # end_date = fields.Date("When company stop support for school")
    school_ids = fields.Many2many("education.school", string="schools support")