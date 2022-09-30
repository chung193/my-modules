from odoo import fields, api, models

class EducationCourseExtend(models.Model):
    _name="education.course.advance"
    _description="Course extend basic course"
    _inherits={'education.course':'extend_course_id'}
    
    name=fields.Char("Name of advance course")
    extend_course_id = fields.Many2one("education.course", string="Extend class")
    
    bonus_price = fields.Integer("Bonus price")
    total_price = fields.Integer("Total price of course", compute="_calculator_total")
    
    is_international = fields.Boolean("is international course or not")
    
    @api.depends('bonus_price','extend_course_id')
    def _calculator_total(self):
        for record in self:
            record.total_price = record.basic_price + record.bonus_price