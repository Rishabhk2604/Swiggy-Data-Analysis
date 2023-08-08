import json
import re

# Load the JSON data from your file
with open('data.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

#  set to store all cities and a set for unique cities
all_cities_and_subregions = set()
unique_cities = set()

# to store restaurant counts for subregions of Delhi
delhi_subregion_restaurant_counts = {}

# list to store restaurant ratings
restaurant_ratings = []

# to store city restaurant counts
city_restaurant_counts = {}

# a list to store restaurant popularity
restaurant_popularity = []

# to store restaurant costs
restaurant_costs = {}

# to store restaurant chains and their popularity
restaurant_chains = {}

# to store restaurant popularity in Pune
restaurant_pune_popularity = {}

# Regular expression pattern to extract numeric part of cost value
cost_pattern = re.compile(r'\d+')

# Regular expression pattern to extract numeric part of popularity value
popularity_pattern = re.compile(r'\d+')

# Iterate through the data to extract cities, subregions, and restaurant data
for city_name, city_data in data.items():
    all_cities_and_subregions.add(city_name)

    if 'restaurants' in city_data:
        unique_cities.add(city_name)

        if city_name == 'delhi' and 'subregion' in city_data:
            subregion = city_data['subregion']
            if subregion in delhi_subregion_restaurant_counts:
                delhi_subregion_restaurant_counts[subregion] += len(
                    city_data['restaurants'])
            else:
                delhi_subregion_restaurant_counts[subregion] = len(
                    city_data['restaurants'])

        city_restaurant_counts[city_name] = len(city_data['restaurants'])

        for restaurant_info in city_data['restaurants'].values():
            rating = restaurant_info.get('rating')
            if rating and rating != "--" and rating != "NA":
                restaurant_ratings.append(
                    (city_name, restaurant_info['name'], float(rating)))

            popularity = restaurant_info.get('rating_count')
            if popularity and popularity != "Too Few Ratings":
                # Extract numeric part of popularity value if valid
                popularity_match = popularity_pattern.search(popularity)
                if popularity_match:
                    popularity_numeric = int(popularity_match.group())
                    restaurant_popularity.append(
                        (restaurant_info['name'], popularity_numeric))

            cost = restaurant_info.get('cost')
            if cost:
                # Extract numeric part of cost value if valid
                cost_match = cost_pattern.search(cost)
                if cost_match:
                    cost_numeric = int(cost_match.group())
                    restaurant_costs.setdefault(
                        city_name, []).append(cost_numeric)

            chain = restaurant_info.get('chain')
            if chain:
                chain_popularity = restaurant_chains.get(chain, 0)
                chain_popularity += popularity_numeric
                restaurant_chains[chain] = chain_popularity

            if city_name == 'Pune':
                restaurant_pune_popularity[restaurant_info['name']
                                           ] = popularity_numeric

# Count the total number of cities and subregions
total_cities_and_subregions = len(all_cities_and_subregions)

# Count the number of unique cities
num_unique_cities = len(unique_cities)

# Find the subregion of Delhi with the maximum number of restaurants
if delhi_subregion_restaurant_counts:
    max_subregion = max(delhi_subregion_restaurant_counts,
                        key=delhi_subregion_restaurant_counts.get)
    max_restaurant_count = delhi_subregion_restaurant_counts[max_subregion]


# Sort restaurant ratings in descending order
restaurant_ratings.sort(key=lambda x: x[2], reverse=True)

# Print the top 5 restaurants with maximum ratings
print("\nTop 5 Restaurants with Maximum Ratings:")
for i, (city, restaurant_name, rating) in enumerate(restaurant_ratings[:5], start=1):
    print(f"{i}. {city} - {restaurant_name} (Rating: {rating})")

# Sort restaurant ratings in ascending order
restaurant_ratings.sort(key=lambda x: x[2])

# Print the top 5 restaurants with minimum ratings
print("\nTop 5 Restaurants with Minimum Ratings:")
for i, (city, restaurant_name, rating) in enumerate(restaurant_ratings[:5], start=1):
    print(f"{i}. {city} - {restaurant_name} (Rating: {rating})")

# Sort cities by the number of restaurants in descending order
top_cities = sorted(city_restaurant_counts.keys(),
                    key=lambda city: city_restaurant_counts[city], reverse=True)
print("\nTop 10 Cities with the Highest Number of Restaurants:")
for i, city in enumerate(top_cities[:10], start=1):
    print(
        f"{i}. {city} (Number of Restaurants: {city_restaurant_counts[city]})")

# Sort restaurant popularity in descending order
restaurant_popularity.sort(key=lambda x: x[1], reverse=True)

# Print top 5 most popular restaurants in Pune
print("\nTop 5 Most Popular Restaurants:")
for i, (restaurant_name, popularity) in enumerate(restaurant_popularity[:5], start=1):
    print(f"{i}. {restaurant_name} (Popularity: {popularity})")

# Find the subregion least expensive restaurant in cost
least_expensive_subregion = None
min_cost = float('inf')
for city, costs in restaurant_costs.items():
    avg_cost = sum(costs) / len(costs)
    if avg_cost < min_cost and city == 'Delhi':
        min_cost = avg_cost
        least_expensive_subregion = city


# Sort restaurant chains by popularity in descending order
for city_name, city_data in data.items():
    if "restaurants" in city_data:  # Check if the key exists in the city data
        for restaurant_id, restaurant_info in city_data["restaurants"].items():
            restaurant_name = restaurant_info["name"]
            if restaurant_name in restaurant_chains:
                restaurant_chains[restaurant_name] += 1
            else:
                restaurant_chains[restaurant_name] = 1

# Sort the restaurant chains by popularity
sorted_chains = sorted(restaurant_chains.items(),
                       key=lambda x: x[1], reverse=True)
print("\n")
print("Top 5 most popular restaurant chains in India:")
# Get the top 5 most popular chains
top_5_chains = sorted_chains[:5]

# Print the top 5 most popular chains
for i, (chain_name, popularity) in enumerate(top_5_chains, start=1):
    print(f"{i}. {chain_name}: {popularity} restaurants")
