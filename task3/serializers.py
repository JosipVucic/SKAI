from rest_framework import serializers


class InputDataSerializer(serializers.Serializer):
    start_times = serializers.ListField(child=serializers.IntegerField())
    end_times = serializers.ListField(child=serializers.IntegerField())

    def validate(self, data):
        start_times = data.get('start_times', [])
        end_times = data.get('end_times', [])

        # Check if start_times and end_times have the same length
        if len(start_times) != len(end_times):
            raise serializers.ValidationError("Start times and end times must have the same length.")

        return data
