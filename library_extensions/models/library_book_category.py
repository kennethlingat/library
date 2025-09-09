from odoo import models, fields, api
from odoo.exceptions import ValidationError

class LibraryBookCategory(models.Model):
    _name = 'library.book.category'
    _description = 'Book Category'


    _sql_constraints = [
        (
            'name_unique', 
            'unique(name)', 
            'The category name must be unique.'
         )
    ]

    name = fields.Char(string='Category Name', required=True)