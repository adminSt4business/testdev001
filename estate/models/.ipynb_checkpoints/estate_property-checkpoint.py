# _*_ coding: utf-8 _*_
from odoo import models, fields, api

class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'datos de propiedades inmobiliarias'
    
    name = fields.Char(string='Title',required=True)
    description = fields.Text(string='Description')
    postcode = fields.Char(string='Postcode')
    date_availability = field.Date(string='Date Availability')
    expected_price = field.Float(string='Expectated Price',required=True)
    selling_price = field.Float(string='Selling Price')
    bedrooms = field.Float(string='Bedrooms')
    living_area = field.Float(string='Living Area')
    facades = field.Float(string='Facades')
    garage = field.Boolean(string='Garage')
    garden = field.Boolean(string='Garden')
    garden_area = field.Float(string='Garden Area')
    garden_orientation = field.Selection(string='Garden Orientation',
                                        selection=[('north','North'),
                                                   ('south','South'),
                                                   ('east','East'),
                                                   ('west','West')
                                                  ],
                                        copy=False)