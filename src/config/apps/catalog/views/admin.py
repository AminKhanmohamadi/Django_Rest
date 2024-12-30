from rest_framework import viewsets
from rest_framework.exceptions import NotAcceptable
from config.apps.catalog.models import Category
from config.apps.catalog.serializers.admin import CreateCategoryNodeSerializer, CategoryTreeSerializer , CategoryNodeSerializer ,UpdateCategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        if self.action == 'list':
            return Category.objects.filter(depth=1)
        return Category.objects.all()


    def get_serializer_class(self):
        match self.action:
            case 'list':
                return CategoryTreeSerializer
            case 'create':
                return CreateCategoryNodeSerializer
            case 'retrieve':
                return CategoryNodeSerializer
            case 'update':
                return UpdateCategorySerializer
            case 'partial_update':
                return UpdateCategorySerializer
            case 'destroy':
                return UpdateCategorySerializer
            case _:
                raise NotAcceptable()
