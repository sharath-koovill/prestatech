from rest_framework_json_api import serializers

class path_serializer(serializers.Serializer):
    error_flag = serializers.CharField()
    paths = serializers.CharField()        
    
