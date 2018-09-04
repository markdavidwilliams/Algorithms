#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  # rec = [rec for rec in recipe]
  rec = [value for value in recipe.values()]
  ing = [value for value in ingredients.values()]
  if len(rec) > len(ing):
    return 0
  else:
    quotients = []
    i = 0
    for item in rec:
      quotients.append(ing[i] / item)
      i += 1
    return math.floor(min(quotients))


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 50, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))