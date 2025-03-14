from odoo import models, fields

class Asset(models.Model):
    _name = 'x_employee.asset'
    _description = 'Employee Asset'
    name = fields.Char(string="Asset Name", required=True)
    asset_type = fields.Selection([
        ('laptop', 'Laptop'),
        ('phone', 'Phone'),
        ('monitor', 'Monitor'),
        ('other', 'Other')
    ], string="Asset Type", required=True)
    serial_number = fields.Char(string="Serial Number", unique=True)
    status = fields.Selection([
        ('available', 'Available'),
        ('assigned', 'Assigned'),
        ('maintenance', 'Under Maintenance'),
        ('retired', 'Retired')
    ], string="Status", default="available")
    employee_id = fields.Many2one('hr.employee', string="Assigned To")
