'''
Name: Edward Drobnis
Date: April 11, 2024
Title: Random Walk
Description: Determines the number of steps needed to walk off a bridge
'''
import random

totalSteps = 0
sum = 0

for i in range(50):
    minSteps = 0
    position = 3.5

    while 0 <= position <= 7:
        step = random.randint(0, 1)
        minSteps += 1

        if step == 0:
            position += 1

        else:
            position -= 1

    sum += minSteps

    if totalSteps < minSteps:
        totalSteps = minSteps

print("Average number of steps: {:.2f}".format(sum / 50))
print("Greatest number of steps: {}".format(totalSteps))