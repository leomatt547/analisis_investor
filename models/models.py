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



