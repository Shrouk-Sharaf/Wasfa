from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Recipe
from .serializers import RecipeSerializer
from users.permissions import IsAdminUser


class RecipeCreateView(generics.CreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class RecipeUpdateView(generics.UpdateAPIView):
    queryset = Recipe.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = RecipeSerializer
    lookup_field = 'id'


class RecipeListView(APIView):
    def get(self, request):
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RecipeDetailView(APIView):
    def get(self, request, id):
        try:
            recipe = Recipe.objects.get(id=id)
        except Recipe.DoesNotExist:
            return Response({'error': 'Recipe not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = RecipeSerializer(recipe)
        return Response(serializer.data)

    def patch(self, request, id):
        try:
            recipe = Recipe.objects.get(id=id)
        except Recipe.DoesNotExist:
            return Response({'error': 'Recipe not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = RecipeSerializer(recipe, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        if not request.user.is_admin:
            return Response({'error': 'Only admin users can delete recipes'}, 
                            status=status.HTTP_403_FORBIDDEN)

        try:
            recipe = Recipe.objects.get(id=id)
            recipe.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Recipe.DoesNotExist:
            return Response({'error': 'Recipe not found'}, status=status.HTTP_404_NOT_FOUND)
