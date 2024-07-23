from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .models import Profile
from .serializers import ProfileSerializer

from property.serializers import ReservationsListSerializer


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def landlord_detail(request, pk):
    profile = Profile.objects.get(pk=pk)

    serializer = ProfileSerializer(profile, many=False)

    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def reservations_list(request):
    user = request.user
    # print(user)
    profile = Profile.objects.get(user=user)
    
    reservations = profile.reservations.all()

    # print('user', request.user)
    # print(reservations)
    
    serializer = ReservationsListSerializer(reservations, many=True)
    return JsonResponse(serializer.data, safe=False)