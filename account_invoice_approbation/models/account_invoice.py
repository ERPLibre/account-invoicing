# Copyright 2020 TechnoLibre. (https://technolibre.ca)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, models, fields


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    def has_to_be_signed(self, also_in_draft=False):
        # return (self.state == 'sent' or (self.state == 'draft' and also_in_draft)) and self.require_signature and not self.signature
        return True

    def has_to_be_paid(self, also_in_draft=False):
        # transaction = self.get_portal_last_transaction()
        # return (self.state == 'sent' or (self.state == 'draft' and also_in_draft)) and self.require_payment and transaction.state != 'done' and self.amount_total
        return True
