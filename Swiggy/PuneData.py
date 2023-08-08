import json
import re

# Function to extract numerical value from rating count strings


def extract_rating_count(count_str):
    match = re.search(r'\d+', count_str)
    if match:
        return int(match.group())
    return 0


# Load the JSON data from your file
with open('data.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# Initialize a list to store all restaurant data
all_restaurants = []

# Iterate through subregions in Pune
if 'Pune' in data:
    pune_data = data['Pune']
    for subregion_data in pune_data.values():
        if 'restaurants' in subregion_data:
            all_restaurants.extend(subregion_data['restaurants'].values())

# Sort the restaurants by a popularity metric (rating_count or extracted numerical value if present)
top_popular_restaurants = sorted(all_restaurants, key=lambda restaurant: extract_rating_count(
    restaurant.get('rating_count', '0')), reverse=True)[:5]

# Display the top 5 most popular restaurants in Pune
print("Top 5 Most Popular Restaurants in Pune with highest visitors:")
for i, restaurant in enumerate(top_popular_restaurants, start=1):
    restaurant_name = restaurant.get('name', 'Unknown Restaurant')
    rating_count = restaurant.get('rating_count', 'No Ratings')
    print(f"{i}. {restaurant_name} (Rating Count: {rating_count})")
