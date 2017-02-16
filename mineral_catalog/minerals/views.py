from django.shortcuts import render, get_object_or_404

from .models import Mineral

import random


def mineral_list(request):
    """Returns a list of all minerals."""
    minerals = Mineral.objects.all()
    random_mineral = random.choice(minerals)
    return render(
        request,
        'minerals/mineral_list.html',
        {'minerals': minerals, 'random_mineral': random_mineral}
    )

def mineral_detail(request, pk):
    """Returns a single mineral."""
    mineral = get_object_or_404(Mineral, pk=pk)
    minerals = Mineral.objects.all()
    random_mineral = random.choice(minerals)
    return render(
        request,
        'minerals/mineral_detail.html',
        {'mineral': mineral, 'random_mineral': random_mineral}
    )
