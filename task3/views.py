from django.views.generic import TemplateView
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from task3.serializers import InputDataSerializer


class SchedulingApiView(APIView):
    """
    Scheduling API View

    API endpoint to calculate the maximum number of interviews that can be scheduled.

    Attributes:
        view_name (str): The name of the API view.
        description (str): A brief description of the API view.
        renderer_classes (list): List of renderer classes for the API view.
        parser_classes (list): List of parser classes for the API view.
    """
    view_name = 'Scheduling API'
    description = 'Returns maximum number of interviews that can be scheduled.'
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    parser_classes = [JSONParser]

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests to calculate the maximum number of interviews.

        Args:
            request (Request): The HTTP request object.
            *args: Additional arguments passed to the view.
            **kwargs: Additional keyword arguments passed to the view.

        Returns:
            Response: The API response containing the results of the scheduling calculation.
        """
        # Deserialize the input data
        serializer = InputDataSerializer(data=request.data)

        if serializer.is_valid():
            # Access the validated data
            start_times = serializer.validated_data['start_times']
            end_times = serializer.validated_data['end_times']

            # Perform business logic to generate schedule
            schedule = self.generate_schedule(start_times, end_times)

            # Create the expected output
            output_data = {"max_interviews": len(schedule)}

            return Response(output_data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def generate_schedule(self, start_times, end_times):
        """
        Generate a schedule based on start times and end times.

        Args:
            start_times (list): List of start times for interviews.
            end_times (list): List of end times for interviews.

        Returns:
            list: List of intervals representing the calculated schedule.
        """
        # Combine start_times and end_times into intervals
        intervals = list(zip(start_times, end_times))

        # Sort intervals based on end times (earliest finishing time first)
        sorted_intervals = sorted(intervals, key=lambda x: x[1])

        # Initialize the schedule
        schedule = []

        while sorted_intervals:
            # Select the interval with the earliest finishing time
            selected_interval = sorted_intervals.pop(0)

            # Remove intervals intersecting with the selected_interval
            sorted_intervals = [interval for interval in sorted_intervals if interval[0] >= selected_interval[1]]

            # Add the selected interval to the schedule
            schedule.append(selected_interval)

        return schedule


class HomeView(TemplateView):
    """
    Home View

    Template view for Scheduling API.

    Attributes:
        template_name (str): The name of the template file.
    """
    template_name = "task3/home.html"

