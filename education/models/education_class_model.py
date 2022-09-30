from odoo import models, fields, api

class EducationClass(models.Model):
    _name = 'education.class'
    _description = 'education class'

    name = fields.Char()
    class_code = fields.Char(compute="_create_class_code", default="CLASS001", store=True)
    description = fields.Text(string="Description of class", readonly=True)
    school_id = fields.Many2one('education.school', string="school")
    
    student_ids = fields.One2many('education.student', 'class_id', string="students", domain="[('school_id', '=', school_id)]")
    teacher_id = fields.Many2one('education.teacher', string="teachers")
    group_id = fields.Many2one("education.class.group", domain="[('school_id', '=', school_id)]")

    school_name=fields.Char(related='school_id.name', string="Name of school")
    
    group_name = fields.Char(related="group_id.name")
    
    @api.depends('school_id', 'group_id')
    def _create_class_code(self):
        year = self.school_id.created
        group = self.group_id.group_code
        if year and group:
            current_year = fields.date.today().year
            num = current_year - year
            temp_code = str(group)+str(num)
            num_class = len(self.env['education.class'].search([('class_code','ilike',temp_code)]))
            self.class_code = temp_code + 'DH' + str(num_class + 1)
        else:
            self.class_code = "CLASS001"
            
        
        
        
        
        