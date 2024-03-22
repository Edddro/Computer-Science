'''
Author: Edward Drobnis
Date: March 22, 2024
Title: Election
Description: Calculates the votes for two politicians in three states
'''

print("Election Results for New York:")
awbrey = int(input("Awbrey: "))
martinez = int(input("Martinez: "))

print("\nElection Results for New Jersey:")
awbrey += int(input("Awbrey: "))
martinez += int(input("Martinez: "))

print("\nElection Results for Connecticut:")
awbrey += int(input("Awbrey: "))
martinez += int(input("Martinez: "))

votes = awbrey + martinez
awbreyPercent = awbrey / votes * 100
martinezPercent = martinez / votes * 100

print("\n{:<15}{:<9}{}".format("Candidate", "Votes", "Percentage"))
print("{:<15}{:<9}{:.2f} %".format("Awbrey", awbrey, awbreyPercent))
print("{:<15}{:<9}{:.2f} %".format("Martinez", martinez, martinezPercent))
print("{:<15}{}".format("TOTAL VOTES:", votes))