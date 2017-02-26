from django.core.management.base import BaseCommand, CommandError
from minerals.models import Mineral

import json

filename = 'data/minerals3.json'


class Command(BaseCommand):
    """Adds all minerals from JSON file to database."""
    help = 'Prepopulates JSON data provided by Team Treehouse.'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open(filename, encoding='utf-8') as file:
            minerals = json.load(file)

        for mineral in minerals:
            Mineral(
                name = mineral['name'],
                img_filename = mineral['image filename'],
                img_caption = mineral['image caption'],
                category = mineral['category'],
                formula = mineral['formula'],
                group = mineral['group'],
                strunz_classification = mineral['strunz classification'],
                crystal_system = mineral['crystal system'],
                unit_cell = mineral['unit cell'],
                color = mineral['color'],
                crystal_symmetry = mineral['crystal symmetry'],
                cleavage = mineral['cleavage'],
                mohs_hardness = mineral['mohs scale hardness'],
                luster = mineral['luster'],
                streak = mineral['streak'],
                diaphaneity = mineral['diaphaneity'],
                optical_properties = mineral['optical properties'],
                refractive_index = mineral['refractive index'],
                crystal_habit = mineral['crystal habit'],
                specific_gravity = mineral['specific gravity']
            ).save()
        self.stdout.write(self.style.SUCCESS(
            '\nMineral data has been successfully uploaded!'
        ))
