from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=30, unique=True)


class Job(models.Model):
    name = models.CharField(max_length=30, unique=True)
    project = models.ForeignKey(Project, related_name='jobs')

