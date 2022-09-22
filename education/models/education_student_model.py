

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class EducationStudent(models.Model):
    _name = 'education.student'
    _description = 'Education student'
    _rec_name="student_code"
    _order = "name"

    name = fields.Char()
    student_code = fields.Char(string="student code", compute="_create_student_code", store=True) #compute="_create_student_code",
    dob = fields.Date(string="Date of birth")
    gender = fields.Selection(string="Gender", default="male", selection=[("male", "Male"), ("female", "Female"), ("other", "Other")])
    email = fields.Char("Email contact")
    phone = fields.Char("Phone contact")
    description = fields.Html()
    attached_file = fields.Binary("attached file")
    age = fields.Integer(string="Age", compute="_compute_age", inverse="_inverse_age")
    
    # relationship fields
    class_id = fields.Many2one('education.class', domain="[('school_id', '=', school_id)]")
    school_id = fields.Many2one('education.school')
    
    # relate fields
    class_name=fields.Char(related='class_id.name', string="Name of class")
    school_name=fields.Char(related='school_id.name', string="Name of school")
    
    _sql_constraints = [
        ('unique_student_code','unique(student_code)','student code must be unique')
    ]
    
    @api.depends('school_id')
    def _create_student_code(self):
        for r in self:
            if r.school_id:
                last_id = self.env['education.student'].search([], order = 'id desc')
                if len(last_id) == 0:
                    temp = 1
                else:
                    temp = last_id[0].id + 1
                r.student_code = r.school_id.school_code + str(temp)

    @api.constrains('dob')
    def _check_dob(self):
        for r in self:
            if self.dob > fields.Date.today():
                raise ValidationError("Date of birth must be before today")
            
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
            if r.dob:
                dob_day = r.dob.day
                dob_month = r.dob.month
                dob_year = current_year-r.age
                r.dob = fields.date(dob_year, dob_month, dob_day)
        
        
