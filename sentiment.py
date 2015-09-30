#!/usr/bin/env python

romantic_words = ['love', 'sigh', 'happy', 'gaze', 'cherish', 'enchanting', 
                  'everlasting', 'gorgeous', 'handsome', 'wonderful']

hp = open('HarryPotter.txt')
hp_word_counter = 0
hp_romance_counter = 0

for line in hp:
    line = line.strip()
    words = line.split()
    for word in words:
        hp_word_counter = hp_word_counter + 1
        if word in romantic_words:
            hp_romance_counter = hp_romance_counter + 1

#print(str(hp_romance_counter) + '/' + str(hp_word_counter))

tw = open('Twilight.txt')
tw_word_counter = 0
tw_romance_counter = 0

for line in tw:
    line = line.strip()
    words = line.split()
    for word in words:
        tw_word_counter = tw_word_counter + 1
        if word in romantic_words:
            tw_romance_counter = tw_romance_counter + 1

#print(str(tw_romance_counter) + '/' + str(tw_word_counter))

if (tw_romance_counter/float(tw_word_counter)) > (hp_romance_counter/float(hp_word_counter)):
    print ('Twilight is more romantic.')
else:
    print ('Harry Potter is more romantic.')
