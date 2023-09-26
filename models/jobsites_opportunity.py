from odoo import models, fields, api

class jobsite_opportunity(models.Model):
    _inherit = 'jobsite'



    opportunity_id=fields.One2many(comodel_name='crm.lead',inverse_name='jobsite_id', string='OPPORTUNITY')
    opportunity_count = fields.Integer("Opportunity", compute='_compute_opportunity_count')

    @api.depends('opportunity_id')
    def _compute_opportunity_count(self):
        for record in self:
            record.opportunity_count = len(record.opportunity_id)

    def action_view_opportunity(self):
        action = self.env['ir.actions.act_window']._for_xml_id('crm.crm_lead_opportunities')
        action['context'] = {'active_test': False}
        action['domain'] = [('jobsite_id', '=', self.id)]

        return action



