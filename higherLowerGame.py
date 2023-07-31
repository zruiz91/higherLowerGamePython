import random
from replit import clear
import art 
import game_data


logo = art.logo
data = game_data.data
vs = art.vs
points = 0
game_over = False

print(logo)


def choose_random_person():
  return random.choice(data)

def compare_followers(person_a, person_b):
  person_a_followers = person_a['follower_count']
  person_b_followers = person_b['follower_count']
  if person_a_followers > person_b_followers:
    return "a"
  else:
    return "b"

# def check_user_answer(user_choice, correct_answer):
  

person_a = choose_random_person()

person_b = choose_random_person()



while game_over == False:
  print(f"Compare A: {person_a['name']}, a {person_a['description']}, from {person_a['country']}.")

  print(vs)
  
  print(f"Compare B: {person_b['name']}, a {person_b['description']}, from {person_b['country']}.")
  
  user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
  
  correct_answer = compare_followers(person_a, person_b)
  
  if user_choice == correct_answer:
    points += 1
    clear()
    print(f"You're right! Current score: {points}.")
    person_a = person_b
    person_b = choose_random_person()
  else:
    print(f"Sorry, that's wrong. Final score: {points}")
    game_over = True