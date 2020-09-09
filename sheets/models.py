from django.db import models
from django.utils.text import slugify


# A blank character sheet to create from scratch
class EmptyCharacterSheet(models.Model):
    user = models.ForeignKey(
        'authentication.CustomUser', on_delete=models.CASCADE, default=None)
    name = models.CharField(blank=False, null=True, max_length=120)
    slug = models.SlugField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True, max_length=300)
    hp = models.IntegerField(blank=True, null=True, default=0)

    def save(self, *args, **kwargs):
        name = self.name
        self.slug = slugify(name, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


# Feat model that ties to character sheets.
# For example: A 'STR' feat with a value of 10.
class Feat(models.Model):
    featName = models.CharField(max_length=120, blank=True, null=False)
    featVal = models.CharField(max_length=120, blank=True, null=False)
    characterSheet = models.ForeignKey(
        EmptyCharacterSheet, related_name="charactersheetfeat", on_delete=models.CASCADE)

    def __str__(self):
        return self.featName
