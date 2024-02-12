from rest_framework import serializers


class ProductListingSerializer(serializers.Serializer):
    productID = serializers.CharField()
    authorizedSellerID = serializers.CharField()


class SalesTransactionSerializer(serializers.Serializer):
    productID = serializers.CharField()
    sellerID = serializers.CharField()


class InputDataSerializer(serializers.Serializer):
    productListings = ProductListingSerializer(many=True)
    salesTransactions = SalesTransactionSerializer(many=True)
