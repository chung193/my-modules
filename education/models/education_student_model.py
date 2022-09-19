

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class EducationStudent(models.Model):
    _name = 'education.student'
    _description = 'Education student'
    _rec_name="student_code"
    _order = "name"

    name = fields.Char()
    student_code = fields.Char(string="student code", required=True)
    dob = fields.Date(string="Date of birth")
    gender = fields.Selection(string="Gender", default="male", selection=[("Male", "male"), ("Female", "female"), ("Other", "other")])
    email = fields.Char("Email contact")
    phone = fields.Char("Phone contact")
    description = fields.Html()
    attached_file = fields.Binary("attached file")
    class_id = fields.Many2one('education.class')
    age = fields.Integer(string="Age", compute="_compute_age")
    
    class_name=fields.Char(related='class_id.name', string="Name of class")
    
    _sql_constraints = [
        ('unique_student_code','unique(student_code)','student code must be unique')
        ]

    @api.constrains('dob')
    def _check_dob(self):
        for r in self:
            if self.dob > fields.Date.today():
                raise ValidationError("Date of birth must be before today")
            
    @api.depends('dob')
    def _compute_age(self):
        current_year = fields.Date.today().year
        for r in self:
            if r.dob and r.age:
                r.age = current_year - r.dob.year
