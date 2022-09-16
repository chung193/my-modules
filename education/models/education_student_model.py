

from odoo import models, fields, api


class EducationStudent(models.Model):
    _name = 'education.student'
    _description = 'Education student'

    name = fields.Char()
    student_code = fields.Char()
    dob = fields.Date(string="Date of birth")
    gender = fields.Selection(string="Gender", selection=[("Male", "male"), ("female", "Female"), ("Other", "other")])
    email = fields.Char("Email contact")
    phone = fields.Char("Phone contact")
    description = fields.Text()

