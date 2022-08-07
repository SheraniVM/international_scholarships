from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from organizations.models import Organization
from organizations.serializers import OrganizationSerializer

# Create your views here.

class OrganizationView(APIView):
    def get(self, request):
        organizations = Organization.objects.all()
        print(organizations)
        serializer = OrganizationSerializer(organizations, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)        
