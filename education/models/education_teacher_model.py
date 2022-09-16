

from odoo import models, fields, api


class EducationTeacher(models.Model):
    _name = 'education.teacher'
    _description = 'Education teacher'

    name = fields.Char()
    dob = fields.Date(string="Date of birth")
    gender = fields.Selection(string="Gender", selection=[("Male", "male"), ("Female", "female"), ("Other", "other")])
    email = fields.Char("Email contact")
    phone = fields.Char("Phone contact")
    description = fields.Text()
