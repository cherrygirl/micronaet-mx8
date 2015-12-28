#!/usr/bin/python
# -*- coding: utf-8 -*-
###############################################################################
#
# ODOO (ex OpenERP) 
# Open Source Management Solution
# Copyright (C) 2001-2015 Micronaet S.r.l. (<http://www.micronaet.it>)
# Developer: Nicola Riolini @thebrush (<https://it.linkedin.com/in/thebrush>)
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. 
# See the GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################


{
    'name' : 'Italian localization - Mx Quotation report aeroo',
    'version' : '0.1',
    'category' : 'Localization/Italy/Reporting',
    'description' : '''
        Base order in Aeroo:
        ''',
    'author': 'Micronaet S.r.l. - Nicola Riolini',
    'website': 'http://www.micronaet.it',
    'license': 'AGPL-3',
    'depends' : [
        'base',
        'purchase',
        #'sale',
        
        'mx_sale', # TODO reintegrated!
        'report_aeroo',
        
        #'report_aeroo_ooo',
        ],
    'init_xml' : [], 
    'data' : [
        'purchase_view.xml',
        #'sale_view.xml',
        'report/purchase_report.xml',
        #'report/sale_report.xml',
        ],
    'demo_xml' : [],
    'test': [],
    'active' : False, 
    'installable' : True, 
    }

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
