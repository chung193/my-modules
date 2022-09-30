from odoo import models, api, fields

class EducationCourse(models.Model):
    _name="education.course"
    _description="Course basic of school"
    
    name=fields.Char("Name of Course")
    course_code = fields.Char("Code of course")
    basic_price = fields.Integer("Price of course")
    
    # course_ids = fields.One2many("education.course.extend","extend_course_id")
    
    