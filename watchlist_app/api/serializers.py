from rest_framework import serializers
from watchlist_app.models import Watchlist,StreamPlatform



class WatchListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Watchlist
        fields = "__all__"


class StreamPlatformSerializer(serializers.ModelSerializer):
    # watchlist = WatchListSerializer(many=True,read_only=True)
    watchlist = serializers.StringRelatedField(many=True,read_only=True)
    class Meta:
        model = StreamPlatform
        fields = "__all__"


    
    # def validate(self,data):
    #     if data["title"] == data["description"]:
    #         raise serializers.ValidationError("Title and description cannot be the same")
    #     else:
    #         return data
    
    # def validate_name(self,value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Name must be at least 2 characters")
    #     else:
    #         return value



"""
def name_length(value):
    if  len(value) < 2:
        raise serializers.ValidationError("Title is too short")

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(validators=[name_length])
    description = serializers.CharField()
    active = serializers.BooleanField()

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance
    
    def validate(self,data):
        if data["title"] == data["description"]:
            raise serializers.ValidationError("Title and description cannot be the same")
        else:
            return data
"""