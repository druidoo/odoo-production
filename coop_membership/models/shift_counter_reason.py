from odoo import fields, models


class ShiftCounterEventReason(models.Model):
    _name = 'shift.counter.event.reason'
    _description = 'Shift Counter Event Reason'

    name = fields.Char()
