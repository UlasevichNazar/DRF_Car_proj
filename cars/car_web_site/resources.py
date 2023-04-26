from import_export import resources
from .models import Car


class CarResources(resources.ModelResource):
    class Meta:
        model = Car
