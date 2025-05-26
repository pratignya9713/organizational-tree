from django.core.management.base import BaseCommand
from people.models import Person

class Command(BaseCommand):
    help = 'Load initial organizational data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Person.objects.all().delete()
        
        # Create root person (John)
        john = Person.objects.create(name="John")
        
        # Create second level
        steve = Person.objects.create(name="Steve", manager=john)
        rohan = Person.objects.create(name="Rohan", manager=john)
        
        # Steve's subordinates
        lee = Person.objects.create(name="Lee", manager=steve)
        bob = Person.objects.create(name="Bob", manager=steve)
        ella = Person.objects.create(name="Ella", manager=steve)
        
        # Rohan's subordinates
        sal = Person.objects.create(name="Sal", manager=rohan)
        emma = Person.objects.create(name="Emma", manager=rohan)
        
        # Emma's subordinates
        tom = Person.objects.create(name="Tom", manager=emma)
        raj = Person.objects.create(name="Raj", manager=emma)
        
        # Tom's subordinate
        bill = Person.objects.create(name="Bill", manager=tom)
        
        self.stdout.write(self.style.SUCCESS('Successfully loaded organizational data')) 