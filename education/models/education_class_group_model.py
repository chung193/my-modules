from odoo import api, models, fields

class EducationClassGroup(models.Model):
    _name="education.class.group"
    _description = "Group class in a school"
    
    name=fields.Char("Name of group")
    group_code=fields.Char("Code of group")
    description = fields.Html("Description of a Group")
    
    school_id = fields.Many2one("education.school", string="School")
    class_ids = fields.One2many("education.class", "group_id")