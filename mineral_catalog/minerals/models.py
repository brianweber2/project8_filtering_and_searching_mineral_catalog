from django.db import models


class Mineral(models.Model):
    name = models.CharField(max_length=255)
    img_filename = models.CharField(max_length=255)
    img_caption = models.TextField(max_length=255, blank=True, default='')
    category = models.CharField(max_length=255)
    formula = models.CharField(max_length=255)
    strunz_classification = models.CharField(max_length=255)
    crystal_system = models.CharField(max_length=255)
    unit_cell = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    crystal_symmetry = models.CharField(max_length=255, blank=True, default='')
    cleavage = models.CharField(max_length=255)
    mohs_hardness = models.CharField(max_length=255)
    luster = models.CharField(max_length=255)
    streak = models.CharField(max_length=255)
    diaphaneity = models.CharField(max_length=255)
    optical_properties = models.CharField(max_length=255)
    refractive_index = models.CharField(max_length=255, blank=True, default='')
    crystal_habit = models.CharField(max_length=255, blank=True, default='')
    specific_gravity = models.CharField(max_length=255, blank=True, default='')

    class Meta:
        ordering = ['name']


    def __str__(self):
        return self.name
