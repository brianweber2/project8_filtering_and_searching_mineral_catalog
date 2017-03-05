from django.core.urlresolvers import reverse
from django.test import TestCase
from django.core.management import call_command
from django.utils.six import StringIO

from .models import Mineral


mineral_data = {
    "name": "Abelsonite",
    "img_filename": "Abelsonite.jpg",
    "img_caption": "Abelsonite from the Green River Formation, Uintah County, Utah, US",
    "category": "Organic",
    "formula": "C<sub>31</sub>H<sub>32</sub>N<sub>4</sub>Ni",
    "strunz_classification": "10.CA.20",
    "crystal_system": "Triclinic",
    "unit_cell": "a = 8.508 Å, b = 11.185 Åc=7.299 Å, α = 90.85°β = 114.1°, γ = 79.99°Z = 1",
    "color": "Pink-purple, dark greyish purple, pale purplish red, reddish brown",
    "crystal_symmetry": "Space group: P1 or P1Point group: 1 or 1",
    "cleavage": "Probable on {111}",
    "mohs_hardness": "2–3",
    "luster": "Adamantine, sub-metallic",
    "streak": "Pink",
    "diaphaneity": "Semitransparent",
    "group": "Organic Minerals",
}
mineral_data2 = {
    "name": "Bhurite",
    "img_filename": "Bhurite.jpg",
    "img_caption": "Brownish tabular crystals of abhurite from Shipwreck \"Hydra\", South coast of Norway",
    "category": "Halide",
    "formula": "Sn<sub>21</sub>O<sub>6</sub>(OH)<sub>14</sub>Cl<sub>16</sub>",
    "strunz_classification": "03.DA.30",
    "crystal_symmetry": "Trigonal",
    "group": "Other",
}


################################
########## View Tests ##########
################################
class MineralViewsTest(TestCase):
    def setUp(self):
        self.mineral = Mineral.objects.create(**mineral_data)
        self.mineral2 = Mineral.objects.create(**mineral_data2)

    def test_mineral_list_view(self):
        resp = self.client.get(reverse('minerals:list'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral, resp.context['minerals'])
        self.assertNotIn(self.mineral2, resp.context['minerals'])
        self.assertTemplateUsed(resp, 'minerals/mineral_list.html')
        self.assertContains(resp, self.mineral.name)

    def test_mineral_detail_view(self):
        resp = self.client.get(
            reverse('minerals:detail', kwargs={'pk': self.mineral.pk})
        )
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.mineral, resp.context['mineral'])
        self.assertTemplateUsed(resp, 'minerals/mineral_detail.html')

    def test_mineral_list_letter_filter_view(self):
        resp = self.client.get(
            reverse('minerals:letter_filter', kwargs={'letter': 'A'})
        )
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral, resp.context['minerals'])
        self.assertNotIn(self.mineral2, resp.context['minerals'])

    def test_mineral_search_view(self):
        resp = self.client.get(reverse('minerals:search'), {'q': 'Bhur'})
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral2, resp.context['result'])
        self.assertTemplateUsed(resp, 'minerals/search.html')

    def test_mineral_group_filter_view(self):
        resp = self.client.get(
            reverse(
                'minerals:group_filter',
                kwargs={'group': 'Organic Minerals'}
            )
        )
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral, resp.context['minerals'])
        self.assertNotIn(self.mineral2, resp.context['minerals'])
        self.assertTemplateUsed(resp, 'minerals/mineral_group_filter.html')


#################################
########## Model Tests ##########
#################################
class MineralModelTest(TestCase):
    def test_mineral_creation(self):
        mineral = Mineral.objects.create(**mineral_data)
        self.assertEqual(mineral.name, 'Abelsonite')


###############################################
########## Management Commands Tests ##########
###############################################
class CommandsTests(TestCase):
    def test_load_mineral_data(self):
        args = []
        opts = {}
        out = StringIO()
        call_command('load_mineral_data', stdout=out, *args, **opts)
        self.assertIn(
            'Mineral data has been successfully uploaded!',
            out.getvalue()
        )
