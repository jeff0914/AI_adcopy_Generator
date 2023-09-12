from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import AdCopy
from .serializers import AdCopySerializer
from django.http import JsonResponse
from .gpt_service import generate_ad_copy  
from django.core.exceptions import ObjectDoesNotExist

def index(request):
    return render(request, 'index.html')

# CRUD API
class AdCopyViewSet(viewsets.ViewSet):

    # Set Permission 
    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        return [IsAuthenticated()]

   # Create
    def create(self, request):
        user_input = request.data.get('user_input')
        if not user_input:
            return Response({"error": "User input is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        generated_text = generate_ad_copy(user_input)
        if not generated_text:
            return Response({"error": "Could not generate text"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        new_ad = AdCopy(user_input=user_input, generated_text=generated_text)
        new_ad.save()
        
        serializer = AdCopySerializer(new_ad)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # Read (List)
    def list(self, request):
        queryset = AdCopy.objects.all()
        serializer = AdCopySerializer(queryset, many=True)
        return Response(serializer.data)

    # Update
    def update(self, request, pk=None):
        try:
            ad_copy = AdCopy.objects.get(uuid=pk)
        except ObjectDoesNotExist:
            return Response({"error": "AdCopy not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = AdCopySerializer(instance=ad_copy, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete
    def destroy(self, request, pk=None):
        try:
            ad_copy = AdCopy.objects.get(uuid=pk)
            ad_copy.delete()
        except ObjectDoesNotExist:
            return Response({"error": "AdCopy not found"}, status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)


def ad_copy_api(request):
    if request.method == 'POST':
        # Implement your POST logic here
        pass
    return JsonResponse({'message': 'Hello, world!'})
