from datetime import date

from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from .models import Survey, Question, Answer


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class SurveySerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, required=False)

    class Meta:
        model = Survey
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):
    def validate(self, data):
        end_date = data['question'].survey.end_date
        if date.today() > end_date:
            raise serializers.ValidationError(f"Survey ended on '{end_date}'")
        return data

    def to_representation(self, instance):
        r = super(AnswerSerializer, self).to_representation(instance)
        r.update({'question': QuestionSerializer().to_representation(instance.question)})
        return r

    class Meta:
        model = Answer
        fields = ('id', 'answer', 'user_id', 'question')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user
