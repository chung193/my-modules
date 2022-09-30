from odoo import fields, models, api

class EducationStudentStage(models.Model):
    _name = 'education.student.stage'
    _description = 'Education Student Stage'
    _order = 'name asc'
    
    name = fields.Char(string="Name")    
    student_state = fields.Char(string="Student state")