def score_choice():
  score_choice_input = raw_input("How would you like to score this turn? ")
  score_choice_input_lower = score_choice_input.lower()

  scoring_option_words = ['ones','twos','threes','fours','fives','sixes',
  '3 of a kind','three of a kind','4 of a kind','four of a kind','full house','small straight',
  'large straight','yahtzee','chance']

  while score_choice_input_lower not in scoring_option_words:
      print "This isn't a valid scoring option"
      score_choice_input = raw_input("How would you like to score this turn? ")
      score_choice_input_lower = score_choice_input.lower()

  if score_choice_input_lower == "ones":
      score_choice_value = 0
  elif score_choice_input_lower == "twos":
      score_choice_value = 1
  elif score_choice_input_lower == "threes":
      score_choice_value = 2
  elif score_choice_input_lower == "fours":
      score_choice_value = 3
  elif score_choice_input_lower == "fives":
      score_choice_value = 4
  elif score_choice_input_lower == "sixes":
      score_choice_value = 5
  elif score_choice_input == "3 of a kind" or score_choice_input == "three of a kind":
      score_choice_value = 6
  elif score_choice_input == "4 of a kind" or score_choice_input == "four of a kind":
      score_choice_value = 7
  elif score_choice_input_lower == "full house":
      score_choice_value = 8
  elif score_choice_input_lower == "small straight":
      score_choice_value = 9
  elif score_choice_input_lower == "large straight":
      score_choice_value = 10
  elif score_choice_input_lower == "yahtzee":
      score_choice_value = 11
  elif score_choice_input_lower == "chance":
      score_choice_value = 12
  else:
      print "This is not a valid option"


  result = [score_choice_value, score_choice_input]

  return result
