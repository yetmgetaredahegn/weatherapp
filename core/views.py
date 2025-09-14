import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import City
from .serializers import CitySerializer

API_KEY = "YOUR_API_KEY"  # replace with OpenWeatherMap key

@api_view(['GET', 'POST'])
def city_list(request):
    if request.method == 'POST':
        serializer = CitySerializer(data=request.data)
        if serializer.is_valid():
            city = serializer.save()
            return Response(CitySerializer(city).data)
        return Response(serializer.errors, status=400)

    cities = City.objects.all()
    serializer = CitySerializer(cities, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def weather(request, city_name):
    """Fetch live weather data for a given city"""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"
    response = requests.get(url).json()

    if response.get("cod") != 200:
        return Response({"error": "City not found"}, status=404)

    data = {
        "city": city_name.title(),
        "temperature": response["main"]["temp"],
        "description": response["weather"][0]["description"],
        "icon": response["weather"][0]["icon"],
    }
    return Response(data)
