# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Investor(models.Model):
    _name = 'investors.investor'
    _description = 'Menyimpan Basis data asli dari Investor'

    nama = fields.Char(string="Nama", required=True)
    alamat = fields.Text(string="Alamat", required=False)
    email = fields.Char(string="Email", required=False)
    pendapatan = fields.Float(string="Pendapatan", required=True)
    current_asset = fields.Float(string="Current Asset", required=True)
    total_asset = fields.Float(string="Total Aset", required=True)
    current_liabilities = fields.Float(string="Current Liabilities", required=True)

class InvestorOmzet(models.Model):
    _name = 'investors.investor.omzet'
    _description = 'Menyimpan Basis data untuk analisis omzet investor'
    _order = 'pendapatan desc'

    nama = fields.Char(string="Nama", required=True)
    alamat = fields.Text(string="Alamat", required=False)
    email = fields.Char(string="Email", required=False)
    pendapatan = fields.Float(string="Pendapatan", required=True)

class InvestorDayaBayar(models.Model):
    _name = 'investors.investor.dayabayar'
    _description = 'Menyimpan Basis data untuk analisis daya bayar investor'
    _order = 'current_ratio desc'

    nama = fields.Char(string="Nama", required=True)
    alamat = fields.Text(string="Alamat", required=False)
    email = fields.Char(string="Email", required=False)
    current_asset = fields.Float(string="Current Asset", required=True)
    current_liabilities = fields.Float(string="Current Liabilities", required=True, store=True)

    @api.depends('current_asset', 'current_liabilities')
    def _compute_current_ratio(self):
        for x in self:
            if x.current_asset and x.current_liabilities:
                x.current_ratio = x.current_asset/x.current_liabilities
            else:
                x.current_ratio = 0.0
            
    def _search_ratio(self, operator, value):
        return [('name', operator, value)]

    current_ratio = fields.Float(string="Current Ratio", compute='_compute_current_ratio', store=True, search='_search_ratio')

    
'''
class Cat(models.Model):
    _name = 'cats.cat'
    _description = 'Deskripsi Kucing'


    name = fields.Char(string="Nama", required=True)
    color = fields.Selection(selection=[
        ('0', 'Merah'), ('1', 'Kuning'), ('2', 'Hijau'), ('3', 'Biru'), ('4', 'Ungu'), 
    ], string="Warna", required=True)
    type = fields.Many2one('cats.cat.type', string="Jenis")


class CatType(models.Model):
    _name = 'cats.cat.type'
    _description = 'Jenis Kucing'


    name = fields.Char(string="Nama")
'''



