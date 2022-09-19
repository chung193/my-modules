

from odoo import models, fields, api

class EducationTeacher(models.Model):
    _name = 'education.teacher'
    _description = 'Education teacher'

    name = fields.Char()
    dob = fields.Date(string="Date of birth")
    gender = fields.Selection(string="Gender", default="male", selection=[("Male", "male"), ("Female", "female"), ("Other", "other")])
    email = fields.Char("Email contact")
    phone = fields.Char("Phone contact")
    description = fields.Html()
    attached_file = fields.Binary("attached file")
    class_ids = fields.Many2many('education.class', string="classes")

    age = fields.Integer(string="Age", compute="_compute_age", reserve="_reserve_age", readonly=False)
    
    @api.depends('dob')
    def _compute_age(self):
        current_year = fields.Date.today().year
        for r in self:
            r.age = current_year - r.dob.year
            
    def _reserve_age(self):
        current_year = fields.Date.today().year
        for r in self:
            if self.dob and self.age:
                dob_year = current_year - self.age
                r.dob = fields.date(dob_year,1,1)