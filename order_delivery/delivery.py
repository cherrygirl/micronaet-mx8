# -*- coding: utf-8 -*-
###############################################################################
#
#    Copyright (C) 2001-2014 Micronaet SRL (<http://www.micronaet.it>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################
import os
import sys
import logging
import openerp
import openerp.netsvc as netsvc
import openerp.addons.decimal_precision as dp
from openerp.osv import fields, osv, expression, orm
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from openerp import SUPERUSER_ID, api
from openerp import tools
from openerp.tools.translate import _
from openerp.tools.float_utils import float_round as round
from openerp.tools import (DEFAULT_SERVER_DATE_FORMAT, 
    DEFAULT_SERVER_DATETIME_FORMAT, 
    DATETIME_FORMATS_MAP, 
    float_compare)


_logger = logging.getLogger(__name__)

class SaleOrder(orm.Model):
    ''' Manage delivery in header
    '''
    _inherit = 'sale.order'

    # -------------
    # button event:
    # -------------
    def force_delivery_line(self, cr, uid, ids, context=None):
        ''' Update row delivery with parent
        '''
        line_pool = self.pool.get('sale.order.line')
        order_proxy = self.browse(cr, uid, ids, context=context)[0]
        line_ids = [line.id for line in order_proxy.order_line]
        return line_pool.write(cr, uid, line_ids, {
            'date_delivery': order_proxy.date_delivery,
            }, context=context)
        
    _columns = {
        'date_delivery': fields.date('Delivery date'),
        }

class SaleOrderLine(orm.Model):
    ''' Manage delivery in line
    '''
    _inherit = 'sale.order.line'

    _columns = {
        'date_delivery': fields.date('Delivery date'),
        }
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
