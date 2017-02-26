from django import template
from django.template import Template
from django.utils.html import mark_safe

from ..models import Mineral
from ..forms import MineralSearchForm

import random


register = template.Library()

@register.simple_tag
def search_form():
    """Returns dictionary with search form."""
    form = MineralSearchForm()
    return form

@register.simple_tag
def random_mineral():
    """Returns a random mineral from the database."""
    minerals = Mineral.objects.all()
    random_mineral = random.choice(minerals)
    return random_mineral
