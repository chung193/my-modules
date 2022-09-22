from odoo import http
from odoo.http import request
import json

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