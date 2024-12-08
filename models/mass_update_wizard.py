from odoo import models, fields, api


class MassUpdateWizard(models.TransientModel):
    _name = 'crm.mass_update_wizard'
    _description = 'CRM Mass Update Wizard'

    company_name = fields.Char('Company Name')
    stage_id = fields.Many2one('crm.stage', 'New Stage')

    @api.multi
    def update_records(self):
        active_ids = self._context.get('active_ids')
        leads = self.env['crm.lead'].browse(active_ids)

        for lead in leads:
            if self.company_name:
                lead.company_name = self.company_name
            if self.stage_id:
                lead.stage_id = self.stage_id

        return {'type': 'ir.actions.act_window_close'}


class CrmLead(models.Model):
    _inherit = 'crm.lead'
