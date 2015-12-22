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

{
    'name': 'Note manager',
    'version': '0.1',
    'category': 'Customization',
    'description': '''        
        Manage note in document:
        Add pre / post note all detail
        Add pre / post note detail
        >> All note could be migrated down in modules 
        (ex. note in sale >> go in picking)
        
        Manage database with particular text for different object position):
           sale.order, sale.order.line
           stock.picking, stock.picking.line
           account.invoice, account.invoice.line
        
        Note: to activate elements use extra modules, like:
        note_manage_sale, note_manager_invoice, note_manager_ddt    
        ''',
    'author': 'Micronaet S.r.l. - Nicola Riolini',
    'website': 'http://www.micronaet.it',
    'license': 'AGPL-3',
    'depends': [
        'base',
        ],
    'init_xml': [],
    'demo': [],
    'data': [
        'security/ir.model.access.csv',
        'note_view.xml',
        ],
    'active': False,
    'installable': True,
    'auto_install': False,
    }
