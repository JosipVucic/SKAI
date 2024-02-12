from django.views.generic import TemplateView
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import InputDataSerializer


class SalesApiView(APIView):
    """
    Sales API View

    API endpoint to check for unauthorized sales.

    Attributes:
        view_name (str): The name of the API view.
        description (str): A brief description of the API view.
        renderer_classes (list): List of renderer classes for the API view.
        parser_classes (list): List of parser classes for the API view.
    """

    view_name = 'Sales API'
    description = 'Checks for unauthorized sales.'
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    parser_classes = [JSONParser]

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests to check for unauthorized sales.

        Args:
            request (Request): The HTTP request object.
            *args: Additional arguments passed to the view.
            **kwargs: Additional keyword arguments passed to the view.

        Returns:
            Response: The API response containing the results of unauthorized sales check.
        """
        # Deserialize the input data
        serializer = InputDataSerializer(data=request.data)

        if serializer.is_valid():
            # Access the validated data
            product_listings = serializer.validated_data['productListings']
            sales_transactions = serializer.validated_data['salesTransactions']

            # Perform business logic to identify unauthorized sales
            unauthorized_sales = self.identify_unauthorized_sales(product_listings, sales_transactions)

            # Create the expected output
            output_data = {"unauthorizedSales": unauthorized_sales}

            return Response(output_data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def identify_unauthorized_sales(self, product_listings, sales_transactions):
        """
        Identify unauthorized sales based on product listings and sales transactions.

        Args:
            product_listings (list): List of product listings.
            sales_transactions (list): List of sales transactions.

        Returns:
            list: List of unauthorized sales identified.
        """
        unauthorized_sales = []

        # Create a dictionary to store authorized sellers for each product
        authorized_sellers = {listing['productID']: listing['authorizedSellerID'] for listing in product_listings}

        # Iterate through sales transactions to identify unauthorized sales
        for transaction in sales_transactions:
            product_id = transaction['productID']
            seller_id = transaction['sellerID']

            # Check if the seller is unauthorized
            authorized_seller = authorized_sellers.get(product_id)
            if authorized_seller and seller_id != authorized_seller or not authorized_seller:
                # Add the unauthorized sale to the list
                unauthorized_sale = {"productID": product_id, "unauthorizedSellerID": [seller_id]}
                unauthorized_sales.append(unauthorized_sale)

        return unauthorized_sales


class HomeView(TemplateView):
    """
    Home View

    Template view for Sales API.

    Attributes:
        template_name (str): The name of the template file.
    """
    template_name = "task2/home.html"

