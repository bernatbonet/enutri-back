from rest_framework.test import APIRequestFactory

"""
1.- Login with different user groups
2.- Make different operations
3.- Check result
"""
factory = APIRequestFactory()
request = factory.post