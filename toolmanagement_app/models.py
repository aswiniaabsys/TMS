from django.db import models


class Tool(models.Model):
    objects = None
    sl_no = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=255)
    project_type = models.CharField(max_length=255)
    vertical = models.CharField(max_length=255)
    platform = models.CharField(max_length=255)
    developer = models.CharField(max_length=255)
    tool_name = models.CharField(max_length=255)
    command = models.TextField()
    technology = models.CharField(max_length=255)
    tool_description = models.TextField()
    year_of_creation = models.CharField(max_length=255)
    repository_path = models.TextField()

    def __str__(self):
        return self.tool_name




