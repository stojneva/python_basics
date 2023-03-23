import sys

count_movies = int(input())
count_rating = 0
max_rating = -sys.maxsize
low_rating = sys.maxsize
max_name = ""
low_name = ""
average_rating = 0

for movie in range(count_movies):
    movie_name = input()
    rating = float(input())
    average_rating += rating

    if rating > max_rating:
        max_rating = rating
        max_name = movie_name
    if rating < low_rating:
        low_rating = rating
        low_name = movie_name

    average_r = average_rating / count_movies
print(f"{max_name} is with highest rating: {max_rating:.1f}")
print(f"{low_name} is with lowest rating: {low_rating:.1f}")
print(f"Average rating:{average_r:.1f}")





