# -*- coding: utf-8 -*-
################################################################
#    License, author and contributors information in:          #
#    __openerp__.py file at the root folder of this module.    #
################################################################

from openerp import models, fields
from openerp.tools.translate import _
        

class CrmStageReason(models.Model):
    """ Explanation on why an opportunity is in current case stage.
    """
    _name = 'crm.stage.reason'
    _description = _('Reason for case stage')

    _rec_name = 'name'
    _order = 'name ASC'

    # --------------------------- ENTITY  FIELDS ------------------------------

    name = fields.Char(
        string='Reason',
        required=True,
        readonly=False,
        translate=True,
        default='',
    )

    description = fields.Text(
        string='Description',
        required=False,
        readonly=False,
        translate=True,
        default='',
    )

    active = fields.Boolean(
        string="Active",
        default=True,
        store=True,
    )

    crm_stages_ids = fields.Many2many(
        comodel_name='crm.case.stage',
        relation='crm_stage_to_reason_rel',
        string='Available stages',
        select=True,
        ondelete='restrict',
        required=False,
        default=False,
    )