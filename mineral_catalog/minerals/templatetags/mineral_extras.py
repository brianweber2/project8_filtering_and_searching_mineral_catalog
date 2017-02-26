from django import template

from ..models import Mineral
from ..forms import MineralSearchForm
from ..views import groups

import random


register = template.Library()

@register.simple_tag
def search_form():
    """Returns search form."""
    form = MineralSearchForm()
    return form

@register.simple_tag
def random_mineral():
    """Returns a random mineral from the database."""
    minerals = Mineral.objects.all()
    random_mineral = random.choice(minerals)
    return random_mineral

@register.simple_tag
def mineral_groups():
    """Return mineral groups."""
    return groups
