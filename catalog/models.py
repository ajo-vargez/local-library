from os import name
from django.db import models

class Genre(models.Model):
    """Model representing a book's genre"""

    name = models.CharField(max_length=200, help_text="Enter a book genre (eg: Science Fiction)")

    def __str__(self):
        """String for representing the model object."""
        
        return self.name
