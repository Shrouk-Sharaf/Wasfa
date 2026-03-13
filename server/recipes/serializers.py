from rest_framework import serializers
from .models import Recipe, Ingredient

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name', 'quantity', 'units']

class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True)

    class Meta:
        model = Recipe
        fields = ['id', 'name', 'category', 'description', 'methods', 'image', 'ingredients', 'isFav']

    def create(self, validated_data):
        ingredients_data = validated_data.pop('ingredients')
        recipe = Recipe.objects.create(**validated_data)
        for ing in ingredients_data:
            name = ing.get('name')
            quantity = ing.get('quantity')
            units = ing.get('units')

            ingredient, created = Ingredient.objects.get_or_create(
                name=name,
                defaults={'quantity': quantity, 'units': units}
            )
            recipe.ingredients.add(ingredient)
        return recipe

    def update(self, instance, validated_data):
        ingredients_data = validated_data.pop('ingredients', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if ingredients_data is not None:
            instance.ingredients.clear()
            for ing in ingredients_data:
                name = ing.get('name')
                quantity = ing.get('quantity')
                units = ing.get('units')

                ingredient, created = Ingredient.objects.get_or_create(
                    name=name,
                    defaults={'quantity': quantity, 'units': units}
                )
                instance.ingredients.add(ingredient)

        return instance
