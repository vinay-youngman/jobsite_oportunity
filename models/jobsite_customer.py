from odoo import models, fields, api

class JobsiteCustomer(models.Model):
    _inherit = 'jobsite'

    patner_ids = fields.One2many(comodel_name='res.partner', inverse_name='customer_jobsite_id', string='Customers')
    partner_count = fields.Integer(string="Customers", compute='_compute_total_customers')

    @api.depends('patner_ids')
    def _compute_total_customers(self):
        for job in self:
            job.partner_count = len(job.patner_ids)


    def action_view_customers(self):
        action = self.env.ref('contacts.action_contacts').read()[0]
        action['domain'] = [('customer_jobsite_id', '=', self._context.get('default_jobsite_id'))]

        return action


