from odoo import models, fields, api

class JobsiteOpportunity(models.Model):
    _inherit = 'jobsite'

    opportunity_ids = fields.One2many(comodel_name='crm.lead', inverse_name='jobsite_id', string='Opportunities')
    opportunity_count = fields.Integer("Opportunity", compute='_compute_opportunity_count')

    @api.depends('opportunity_ids')
    def _compute_opportunity_count(self):
        for record in self:
            record.opportunity_count = len(record.opportunity_ids)

    def action_view_opportunity(self):
        action = self.env.ref('crm.crm_lead_opportunities').read()[0]
        action['context'] = {'default_jobsite_id': self.id}
        action['domain'] = [('jobsite_id', '=', self.id)]
        return action
