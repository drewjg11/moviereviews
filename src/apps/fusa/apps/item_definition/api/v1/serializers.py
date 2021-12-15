from rest_framework import serializers
from apps.fusa.apps.item_definition.models import Item, Function


class FunctionSerializer(serializers.ModelSerializer):
    creator = serializers.StringRelatedField(read_only=True)
    item = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Function
        fields = "__all__"


class ItemSerializer(serializers.ModelSerializer):
    creator = serializers.StringRelatedField(read_only=True)
    function = FunctionSerializer(many=True, read_only=True)

    class Meta:
        model = Item
        fields = "__all__"
