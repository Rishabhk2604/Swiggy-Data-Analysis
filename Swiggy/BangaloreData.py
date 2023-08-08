import json
import re

# JSON loAd
with open('data.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

#  a list to store restaurant data
all_restaurants = []

# Iteratation in Bangalore
if 'Bangalore' in data:
    bangalore_data = data['Bangalore']
    for subregion_data in bangalore_data.values():
        if 'restaurants' in subregion_data:
            all_restaurants.extend(subregion_data['restaurants'].values())

# Regular expression pattern to extract numeric part of rating count
rating_count_pattern = re.compile(r'\d+')

# Sort by rating coUnt
top_rated_restaurants = sorted(all_restaurants, key=lambda restaurant: int(rating_count_pattern.search(restaurant.get('rating_count', '0')).group(
)) if restaurant.get('rating_count') and rating_count_pattern.search(restaurant.get('rating_count')) else 0, reverse=True)[:10]

# Display the top 10 restaurants with maximum ratingS
print("Top 10 Restaurants with Maximum Ratings in Bangalore:")
for i, restaurant in enumerate(top_rated_restaurants, start=1):
    restaurant_name = restaurant.get('name', 'Unknown Restaurant')
    rating_count = restaurant.get('rating_count', 'No Ratings')
    print(f"{i}. {restaurant_name} (Rating Count: {rating_count})")
