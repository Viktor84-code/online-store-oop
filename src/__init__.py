"""Складывает общую стоимость двух продуктов (цена × количество)."""

from .category import Category
from .lawngrass import LawnGrass
from .product import Product
from .smartphone import Smartphone

__all__ = ['Product', 'Smartphone', 'LawnGrass', 'Category']
