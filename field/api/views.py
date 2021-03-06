from rest_framework import generics
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from field.models import Field
from .serializers import FieldModelSerializer
from ..models import Field
from django.db.models import Q
from .pagination import StandardResultsSetPagination


class FieldAPIView(generics.ListAPIView):
    serializer_class = FieldModelSerializer
    pagination_class = StandardResultsSetPagination
    queryset = Field.objects.all()
    def get_queryset(self, *args, **kwargs):

        order = self.request.GET.get("order", None)
        if order is not None:

            if(int(order) == 0):
                return  Field.objects.order_by("name")
            elif (int(order) == 1):
                return  Field.objects.order_by("-price")
            else:
                return Field.objects.all()

        return Field.objects.all()


