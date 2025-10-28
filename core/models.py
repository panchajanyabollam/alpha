from django.db import models

#Abstract base models for other models to inherit by default
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    #abstract base model to avoid creating a separate table
    class Meta:
        abstract = True
