import random

import art 
import game_data


def choose_random_person():
  return random.choice(data)

logo = art.logo
data = game_data.data
vs = art.vs

print(logo)
# print(data)

person_a = choose_random_person()

person_b = choose_random_person()

print(f"Compare A: {person_b['name']}, a {person_b['description']}, from {person_b['country']}.")

print(vs)

print(f"Compare B: {person_a['name']}, a {person_a['description']}, from {person_a['country']}.")