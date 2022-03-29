import random

# main variables
hangmans = None
words_list = "squirrel bear whale coyote hedgehog lion dolphin crocodile raccoon hyena monkey panda deer leopard kangaroo tiger zebra giraffe hippo wolf elephant gorilla snake eagle antelope vulture panther parrot rhino shark rabbit reindeer lizard leopard koala frog turtle toucan spider sparrow scorpion moose iguana capybara butterfly bison raven falcon sheep buffalo wildebeest baboon ostrich flamingo jackal".upper().split()

word_choice = random.choice(words_list)
print(word_choice)