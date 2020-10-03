# -*- coding: utf-8 -*-
################################################################################
# Author      : Hanoi Calvo Fernandez
# Copyright(c): 2020-Present Hanoi Calvo Fernandez hanoi.calvo@uic.cu
# All Rights Reserved.
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#################################################################################
{
    "name" : "Odoo POS Reservation Order",
    "author": "Hanoi Calvo Fernandez",
    "version" : "13.0.0.3",
    "category" : "Point of Sale",
    'summary': 'Reservas en el pos,',
    "description": """
       Modulo para hacer reservas desde el pos de odoo. hecho para confiterias marfen en españa, basado en operaciones de
       aspl sin usar su logica y hecho desde cero, resolviendo los problemas con los formatos de fechas y otros.
    """,
    "license" : "GPL-3",
    "depends" : ['base','point_of_sale','account'],
    "data": [
        'views/pos_view.xml',
    ],
    'qweb': [
        'static/src/xml/reserve_order_xml.xml',
    ],
    "auto_install": False,
    "price": 200,
    "currency": 'EUR',
    "installable": True,
    "live_test_url":'https://youtu.be/FkuzfnM-Doc',
    "images":["static/description/main_screenshot.jpg"],
    "category" : "Point of Sale",
}