from odoo import api, fields, models

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', required=True, tracking=True)
    age = fields.Integer(string='Age', tracking=True)
    gender = fields.Selection([
        ('male','Male'),
        ('female', 'Female')
    ], string='Gender', tracking=True)
    date_of_birth = fields.Date(string='Date of Birth', tracking=True)
    ref = fields.Char(string='Reference', default='patients', tracking=True)
    active = fields.Boolean('Active', default=True)
    patients = fields.Boolean(string="Is Patient", default=True)