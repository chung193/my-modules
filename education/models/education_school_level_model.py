from odoo import fields, api, models

class EducationSchoolLevel(models.Model):
    _name="education.school.level"
    _description="Level of a school"
    
    name=fields.Char(string="Name of level")
    school_ids = fields.One2many("education.school","level_id")