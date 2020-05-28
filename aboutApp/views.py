from aboutApp.serializers import AboutSerializer
from aboutApp.models import About
from rest_framework import views
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, FormParser

# Create your views here.
class AboutAPIView(views.APIView):
    parser_classes = (JSONParser, FormParser)
    def get(self, request, format=None):
        results = About.objects.all()
        serializer = AboutSerializer(results, many=True)
        return Response(serializer.data)

    def put(self,request, format=None):
        About.objects.filter(id=request.data['id']).update(about_info=request.data['about_info'])
        results = About.objects.all()
        serializer = AboutSerializer(results, many=True)
        return Response(serializer.data)

