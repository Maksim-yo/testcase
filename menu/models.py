from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=40, unique=True)


class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, null=False, blank=False)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='childrens')
    name = models.CharField(max_length=40, null=False, blank=False)
    url = models.CharField(max_length=255, null=False, blank=False)