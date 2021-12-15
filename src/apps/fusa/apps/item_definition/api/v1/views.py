from rest_framework import viewsets, generics
from apps.fusa.apps.item_definition.models import Item, Function
from apps.fusa.apps.item_definition.api.v1.serializers import ItemSerializer, FunctionSerializer


class ItemView(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def perform_create(self, serializer):
        creator = self.request.user
        serializer.save(creator=creator)


class FunctionView(viewsets.ModelViewSet):
    queryset = Function.objects.all()
    serializer_class = FunctionSerializer


class FunctionCreate(generics.CreateAPIView):
    queryset = Function.objects.all()
    serializer_class = FunctionSerializer

    def perform_create(self, serializer):
        creator = self.request.user

        pk = self.kwargs.get('pk')
        item = Item.objects.get(pk=pk)

        serializer.save(creator=creator, item=item)
