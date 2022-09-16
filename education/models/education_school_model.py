

from odoo import models, fields, api


class EducationSchool(models.Model):
    _name = 'education.school'
    _description = 'Education school'

    name = fields.Char()
    school_code = fields.Char()
    description = fields.Text()

