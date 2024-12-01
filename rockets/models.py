from django.db import models


class Rocket(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Component(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    weight = models.FloatField()
    capacity = models.FloatField(null=True, blank=True)
    parent = models.ForeignKey(
        'self', null=True, blank=True, related_name='subcomponents', on_delete=models.CASCADE
    )
    rocket = models.ForeignKey(
        Rocket, null=True, blank=True, related_name='components', on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
