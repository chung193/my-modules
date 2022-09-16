from odoo import models, fields, api

class EducationClass(models.Model):
    _name = 'education.class'
    _description = 'education class'

    name = fields.Char()
    class_code = fields.Char()
    description = fields.Text(string="Description of class")

