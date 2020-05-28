from rest_framework import status
from rest_framework import views, generics
from rest_framework.response import Response
from rest_framework import exceptions
from rest_framework.parsers import JSONParser, FormParser
from rest_framework.permissions import IsAuthenticated
from TestApp.serializers import  TestSerializer, TestOnlyTestNameFieldSerializer, Results, ResultsSerializer, Test
# Create your views here.

class AlbumAPIView(views.APIView):
    #permission_classes = (IsAuthenticated,)
    def get_objects(self, test_name):
        if test_name:
            tests = Test.objects.filter(test_name=str(test_name))
            if len(tests) == 0:
                raise exceptions.ValidationError(f'Тест ({test_name}) с заданным именем не найден')
        else:
            tests = Test.objects.all()
        return tests

    def get(self, request, format=None):
        test_name = request.GET.get('test_name')
        tests =self.get_objects(test_name)
        serializer = TestSerializer(tests, many=True)
        return Response(serializer.data)

class TestListAPIView(generics.ListAPIView):
    #permission_classes = (IsAuthenticated,)
    queryset = Test.objects.all()
    serializer_class = TestOnlyTestNameFieldSerializer

class ResultsAPIView(views.APIView):
    #parser_classes = (JSONParser, FormParser)
    permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        results = Results.objects.filter(username=request.user)
        serializer = ResultsSerializer(results, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        request.data['username'] = str(request.user)
        serializer = ResultsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)