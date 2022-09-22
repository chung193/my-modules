

from odoo import models, fields, api

class EducationTeacher(models.Model):
    _name = 'education.teacher'
    _description = 'Education teacher'

    name = fields.Char()
    dob = fields.Date(string="Date of birth")
    gender = fields.Selection(string="Gender", selection=[("male","Male"), ("female","Female"), ("other","Other")])
    email = fields.Char("Email contact")
    phone = fields.Char("Phone contact")
    description = fields.Html()
    attached_file = fields.Binary("attached file")
    class_ids = fields.One2many('education.class','teacher_id', string="classes")

    age = fields.Integer(string="Age", compute="_compute_age", inverse="_inverse_age", store=False, readonly=False)
    
    @api.depends('dob')
    def _compute_age(self):
        current_year = fields.Date.today().year
        for r in self:
            if r.dob:
                r.age = current_year - r.dob.year    
            else:
                r.age = 0
       
    def _inverse_age(self):
        current_year = fields.Date.today().year
        for r in self:
            if r.dob and r.age:
                dob_year = current_year - r.age
                dob_month = r.dob.month
                dob_day = r.dob.day
                r.dob = fields.date(dob_year,dob_month,dob_day)

    
                