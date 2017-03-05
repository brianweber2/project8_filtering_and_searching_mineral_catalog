from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.db.models import F, Q

from .models import Mineral
from . import forms

import random
import string


# Constants
letters = string.ascii_uppercase
letter_start = letters[0]
groups = ['silicates', 'oxides', 'sulfates', 'sulfides', 'carbonates',
          'halides', 'sulfosalts', 'phosphates', 'borates',
          'Organic Minerals', 'asenates', 'Native Elements', 'other']

def mineral_list(request):
    """Returns a list of all minerals."""
    # minerals = Mineral.objects.all()
    minerals = Mineral.objects.filter(name__istartswith=letter_start).values(
        'name', 'pk')
    random_mineral = random.choice(minerals)

    return render(
        request,
        'minerals/mineral_list.html',
        {
            'minerals': minerals,
            'random_mineral': random_mineral,
            'letters': letters,
            'active_letter': letter_start,
            'mineral_groups': groups
        }
    )

def mineral_detail(request, pk):
    """Returns a single mineral."""
    mineral = get_object_or_404(Mineral, pk=pk)
    minerals = Mineral.objects.all()
    random_mineral = random.choice(minerals)

    return render(
        request,
        'minerals/mineral_detail.html',
        {
            'mineral': mineral,
            'random_mineral': random_mineral,
            'letters': letters,
            'mineral_groups': groups
        }
    )

def mineral_list_letter_filter(request, letter):
    """Returns a list of all minerals that begin with letter."""
    all_minerals = Mineral.objects.all()
    random_mineral = random.choice(all_minerals)
    minerals = Mineral.objects.filter(name__istartswith=letter)

    return render(
        request,
        'minerals/mineral_list.html',
        {
            'minerals': minerals,
            'random_mineral': random_mineral,
            'letters': letters,
            'active_letter': letter,
            'mineral_groups': groups
        }
    )

def mineral_search(request):
    """Returns a list of minerals that match the search query."""
    result = []
    query = request.GET.get('q', None)

    minerals = Mineral.objects.all().values('name', 'pk')
    random_mineral = random.choice(minerals)

    if query:
        result = Mineral.objects.filter(name__icontains=query)
    return render(
        request,
        'minerals/search.html',
        {
            'query': query,
            'result': result,
            'random_mineral': random_mineral,
            'letters': letters,
            'mineral_groups': groups
        }
    )

def mineral_group_filter(request, group):
    """Returns a list of all minerals in a specified group."""
    if group == 'organic_minerals':
        group = 'Organic Minerals'
    elif group == 'native_elements':
        group = 'Native Elements'

    all_minerals = Mineral.objects.all().values('name', 'pk')
    random_mineral = random.choice(all_minerals)
    minerals = all_minerals.filter(group__iexact=group)

    return render(
        request,
        'minerals/mineral_group_filter.html',
        {
            'minerals': minerals,
            'random_mineral': random_mineral,
            'letters': letters,
            'active_group': group,
            'mineral_groups': groups
        }
    )
