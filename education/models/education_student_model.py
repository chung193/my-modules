

from odoo import models, fields, api, modules
from odoo.exceptions import ValidationError, UserError
import base64


class EducationStudent(models.Model):
    _name = 'education.student'
    _description = 'Education student'
    _rec_name="student_code"
    _order = "name"

    def get_default_image(self):
        with open(modules.get_module_resource('education', 'static/src/img', 'student_default.png'), 'rb') as f:
            return base64.b64encode(f.read())
        
    firstname = fields.Char()
    lastname = fields.Char()
    name = fields.Char()
    student_code = fields.Char(string="student code", compute="_create_student_code", store=True) #compute="_create_student_code",
    dob = fields.Date(string="Date of birth")
    gender = fields.Selection(string="Gender", default="male", selection=[("male", "Male"), ("female", "Female"), ("other", "Other")])
    email = fields.Char("Email contact")
    phone = fields.Char("Phone contact")
    description = fields.Html()
    attached_file = fields.Binary("attached file", default=get_default_image)
    age = fields.Integer(string="Age", compute="_compute_age", inverse="_inverse_age", search="_search_age")
    dropout_reason = fields.Text(string="Dropout Reason")
    
    def _default_stage_id(self):
        try:
            stage = self.env['education.student.stage'].search([], limit=1)
        except:
            stage = False
        return stage
   
    stage_id = fields.Many2one('education.student.stage', string="Stage", default=_default_stage_id, group_expand='_group_expand')

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
    
    def _search_age(self, operator, value):
         new_year = fields.Date.today().year - value
         new_value = fields.date(new_year, 1, 1)
         # age > value => date_of_birth < new_value
         operator_map = {'>': '<', '>=': '<=', '<': '>', '<=': '>=', '=':'='}
         new_operator = operator_map.get(operator, operator)
         return [('dob', new_operator, new_value)]
    
    def show_all_public_and_private_schools_accessright_admin(self):
       education_group_admin = self.env.ref('base.user_admin')
       schools = self.env['education.school'].with_user(education_group_admin).search([])
       return schools
   
    @api.model
    def create(self, vals):
       '''
       input first name + last name ==> full name
       '''
       vals['name'] = vals['firstname'] + " " + vals['lastname']
       
       records = super(EducationStudent, self).create(vals)
       return records
   
    
    def write(self, vals):
        if 'firstname' in vals and 'lastname' in vals:
            vals['name'] = vals['firstname'] + " " + vals['lastname']
            
        elif 'firstname' in vals:
            vals['name'] = vals['firstname'] + " " + self.lastname
            
        elif 'lastname' in vals:
            vals['name'] = self.firstname + vals['lastname']
        
        return super(EducationStudent, self).write(vals)
   
   
    @api.model
    def is_allowed_state(self, current_state, new_state):
       allowed_state = [('new', 'studying'), ('studying', 'off'), ('off', 'studying'), ('new', 'off')]
       return (current_state, new_state) in allowed_state
   
    def change_student_state(self, state):
       for student in self:
           if student.is_allowed_state(student.state, state):
               student.state = state
           else:
               raise UserError("Changing state from %s to %s is not allowed" % (student.state, state))
    
    def change_to_new(self):
       self.change_student_state('new')
       
    def change_to_studying(self):
       self.change_student_state('studying')
       
    def change_to_off(self): 
       self.change_student_state('off')
       
    def search_student(self, string_gender):
        students = self.env['education.student'].search([('gender', '=', string_gender)], limit=5, order='student_code')  
        print(students)

    def search_gender_male(self):
       self.search_student('male')
       
    def search_gender_female(self):
       self.search_student('female')
       
    @api.model
    def _update_student_code(self):
       all_students = self.search([])
       for student in all_students:
           student.student_code = '%s_%s' % (student.school_id.code, student.student_code)
           
    
    def _fitered_student_state(self):
            students = self.env['education.student'].search([])
            return students.filtered(lambda student: students.state == 'new' )
    
    def _fitered_student_state_domain(self):
            students = self.env['education.student'].search([])
            return students.filtered_domain([('state','==','new')])
       
    def action_dropout(self):
        return self.env.ref('education.education_student_dropout_wizard_action').read()[0]
