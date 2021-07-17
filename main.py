# mahdi_habibi
import random

humans = []
humans_with_fitscore = []


def human_creator(id):
    age = random.randint ( 1 , 100 )
    weight = random.randint ( 20 , 150 )
    height = random.randint ( 20 , 350 )
    health = random.randint ( 0 , 100 )
    human = { 'id': id, 'age': age, 'weight': weight, 'height': height,
              'health': health}
    return human


def cross_over(human1, human2):
    weights = (human1['weight'], human2['weight'])
    heights = (human1['height'], human2['height'])
    healths = (human1['health'], human2['health'])
    id = human1['id'] + human2['id']
    age = 0
    weight = random.sample( weights, 1)  # return a list have 1 element
    height = random.sample( heights, 1)
    health = random.sample( healths, 1)
    child = {'id': id , 'age': age, 'weight': weight[0], 'height': height[0],
             'health': health[0]}
    return child


def fittness_score(human):  # age*height*health/weight
    fittness_score = human['age'] * human['health'] * human['height'] / human['weight']
    return fittness_score


def sort_tuple(tupls):
    tupls.sort(key=lambda x: x[1])
    return tupls


for id in range(1, 21):
    human = human_creator(id)
    humans.append(human)

for human in humans:
    humans_with_fitscore.append((human, fittness_score(human)))

for i in range(20):
    sort_tuple(humans_with_fitscore)
    for j in range(0, 8, 2):
        child = cross_over(humans_with_fitscore[j][0], humans_with_fitscore[j + 1][0])
        humans.append(child)
        humans_with_fitscore.append((child, fittness_score(child)))

print(len(humans_with_fitscore))
print(len(humans))
