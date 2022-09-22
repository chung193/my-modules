

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class EducationSchool(models.Model):
    _name = 'education.school'
    _description = 'Education school'

    name = fields.Char()
    school_code = fields.Char()
    description = fields.Text()
    created = fields.Integer("Year this school create")
    
    class_ids = fields.One2many('education.class','school_id', string="classes")
    level_id = fields.Many2one("education.school.level", string="Level of school")
    student_ids = fields.One2many("education.student", 'school_id' )
    
    level_name = fields.Char(related="level_id.name")
    company_ids = fields.Many2many("education.company", string="company support")
    
    @api.constrains('created')
    def _check_year_create(self):
        current_year = fields.date.today().year
        if self.created > current_year:
            raise ValidationError("Created year cannot large than current year")
    