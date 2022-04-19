# _*_ coding: utf-8 _*_
from odoo import models, fields, api

class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'datos de propiedades inmobiliarias'
    
    name = fields.Char(string='Title',required=True)
    description = fields.Text(string='Description')
    postcode = fields.Char(string='Postcode')
    date_availability = fields.Date(string='Date Availability')
    expected_price = fields.Float(string='Expectated Price',required=True)
    selling_price = fields.Float(string='Selling Price')
    bedrooms = fields.Integer(string='Bedrooms')
    living_area = fields.Integer(string='Living Area')
    facades = fields.Integer(string='Facades')
    garage = fields.Boolean(string='Garage')
    garden = fields.Boolean(string='Garden')
    garden_area = fields.Integer(string='Garden Area')
    garden_orientation = fields.Selection(string='Garden Orientation',
                                        selection=[('north','North'),
                                                   ('south','South'),
                                                   ('east','East'),
                                                   ('west','West')
                                                  ],
                                        copy=False)