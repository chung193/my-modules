from odoo import models, fields, api

class EducationClass(models.Model):
    _name = 'education.class'
    _description = 'education class'

    name = fields.Char()
    class_code = fields.Char()
    description = fields.Text(string="Description of class")
    school_id = fields.Many2one('education.school', string="school")
    student_ids = fields.One2many('education.student', 'class_id', string="students")
    teacher_ids = fields.Many2many('education.teacher', string="teachers")


    school_name=fields.Char(related='school_id.name', string="Name of school")