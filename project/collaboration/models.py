from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=30)


class Job(models.Model):
    name = models.CharField(max_length=30)
