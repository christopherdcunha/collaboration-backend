from django.db import models
import simple_audit


class Project(models.Model):
    name = models.CharField(max_length=30, unique=True)


class Job(models.Model):
    name = models.CharField(max_length=30, unique=True)
    project = models.ForeignKey(Project, related_name='jobs')

simple_audit.register(Project, Job)
