from odoo import api, fields, models

class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Hospital Appointment'

    patient_id = fields.Many2one('hospital.patient', string='Patient')
    appointment_time = fields.Datetime(string='Appointment Time', default=fields.Datetime.now)
    booking_date = fields.Date(string='Booking Date', default=fields.Date.context_today)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], string='Gender', related='patient_id.gender')