from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=100)
    manager = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='subordinates')
    
    def __str__(self):
        return self.name
    
    @property
    def is_root(self):
        return self.manager is None
    
    def get_all_subordinates(self):
        """Get all subordinates recursively"""
        result = []
        for subordinate in self.subordinates.all():
            result.append(subordinate)
            result.extend(subordinate.get_all_subordinates())
        return result
