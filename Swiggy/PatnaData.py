import json
import re

# Load the JSON
with open('data.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# Get the restaurant data for Patna
patna_restaurants = data.get('Patna', {}).get('restaurants', {}).values()

# Regular expression pattern to extract numeric part of rating count
rating_count_pattern = re.compile(r'\d+')

# Sort the restaurants by descending number of ratings and then by descending rating
top_rated_restaurants = sorted(patna_restaurants, key=lambda restaurant: (int(rating_count_pattern.search(restaurant.get('rating_count', '0')).group()) if rating_count_pattern.search(
    restaurant.get('rating_count', '0')) else 0, float(restaurant.get('rating', '0')) if restaurant.get('rating') != '--' else 0), reverse=True)[:10]

# Display the top 10 restaurants in Patna
print("Top 10 Restaurants in Patna with respect to rating (Number of reviews and Rating ):")
for i, restaurant in enumerate(top_rated_restaurants, start=1):
    restaurant_name = restaurant.get('name', 'Unknown Restaurant')
    rating_count = restaurant.get('rating_count', 'No Ratings')
    rating = restaurant.get('rating', 'No Rating')
    print(f"{i}. {restaurant_name} (Rating Count: {rating_count}, Rating: {rating})")
