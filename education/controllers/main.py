from odoo import http
from odoo.http import request
import json
import datetime

class Main(http.Controller):
    
    @http.route('/api/json/teacher/', type="json", auth='none')
    def _teacher_json_request(self):
        teacher = request.env['education.teacher'].sudo().search([])
        res = {"menu": {
              "id": "file",
              "value": "File",
              "popup": {
                "menuitem": [
                  {"value": "New", "onclick": "CreateNewDoc()"},
                  {"value": "Open", "onclick": "OpenDoc()"},
                  {"value": "Close", "onclick": "CloseDoc()"}
                ]
              }
            }}

        return json.dumps(res)
    
    @http.route('/api/http/teacher/', type="http", auth='none')
    def _teacher_http_request(self):
        teacher = request.env['education.teacher'].sudo().search([])
        html_result = '<html><body><ul>'
        for teacher in teacher:
            html_result += "<li> %s </li>" % teacher.name
        html_result += '</ul></body></html>'
        return html_result
    
    @http.route('/api/http/student/', type="http", auth='none')
    def _student_http_request(self):
        student = request.env['education.student'].sudo().search([])
        html_result = '<html><body><ul>'
        for student in student:
            dob = datetime.datetime.strptime(str(student.dob), "%Y-%m-%d").strftime("%d-%m-%Y")
            html_result += "<li>%s - %s - %s</li>" % (student.name , student.student_code, dob)
        html_result += '</ul></body></html>'
        return html_result
    
    # @http.route('/api/http/student/', type="http", auth='none')
    # def _student_http_request(self):
    #     student = request.env['education.student'].sudo().search([])
    #     html_result = '<html><body><ul>'
    #     for student in student:
    #         html_result += "<li>%s - %s - %s</li>" % (student.name , student.student_code, student.dob)
    #     html_result += '</ul></body></html>'
    #     return html_result
    #

    
    
    
    
    