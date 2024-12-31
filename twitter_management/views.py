from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .crew_ai.main import generate_tweets

# Create your views here.

class TestView(APIView):
    def get(self, request):
        return Response({"message": "Hello, Twitter Management!"}, status=status.HTTP_200_OK)

class CreatePostView(APIView):
    def post(self, request):
        keywords = request.data.get('keywords')
        description = request.data.get('description')
        prompt = request.data.get('prompt')
        print(keywords, description, prompt)
        if not keywords or not description:
            return Response(
                {'error': 'Keyword and description are required'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            tweets = generate_tweets(description,keywords, prompt)
            
            return Response({
                'status': 'success',
                'tweets': tweets
            }, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response({
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

