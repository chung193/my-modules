

from odoo import models, fields, api


class EducationStudent(models.Model):
    _name = 'education.student'
    _description = 'Education student'
    _rec_name="student_code"
    _order = "name"

    name = fields.Char()
    student_code = fields.Char(string="student code", required=True)
    dob = fields.Date(string="Date of birth")
    gender = fields.Selection(string="Gender", selection=[("Male", "male"), ("Female", "female"), ("Other", "other")])
    email = fields.Char("Email contact")
    phone = fields.Char("Phone contact")
    description = fields.Text()

