from rest_framework import serializers
from TestApp.models import Answer,Question, Test, Results

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['answer','сorrect_answer']

class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)
    class Meta:
        model = Question
        fields = ['question', 'multiple_choice', 'answers']

class TestSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)
    class Meta:
        model = Test
        fields = ['test_name', 'questions']

class TestOnlyTestNameFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ['test_name']


class ResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Results
        fields= ["username", "testname", "result"]