from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Mineral
from . import forms

import random
import string


# Constants
letters = string.ascii_uppercase
letter_start = letters[0]

def mineral_list(request):
    """Returns a list of all minerals."""
    # minerals = Mineral.objects.all()
    minerals = Mineral.objects.filter(name__istartswith=letter_start)
    random_mineral = random.choice(minerals)

    return render(
        request,
        'minerals/mineral_list.html',
        {
            'minerals': minerals,
            'random_mineral': random_mineral,
            'letters': letters,
            'active_letter': letter_start
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
            'letters': letters
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
            'active_letter': letter
        }
    )

# def normalize_query(query_string, pattern = "\w+=\w+[+]\w+"):
#     """Splits the query string in individual keywords."""
#     import re
#     result = re.findall(pattern, query_string)
#     return result

def mineral_search(request):
    """Returns a list of minerals that match the search query."""
    result = []
    query = request.GET.get('q', None)

    minerals = Mineral.objects.all()
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
            'letters': letters
        }
    )

