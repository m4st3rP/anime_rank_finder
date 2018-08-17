import random

ranking = []
original_ranking = {}

with open("list.txt", mode="r", encoding="utf-8") as f:
    line = f.readline()
    while line:
        ranking.append(line)
        line = f.readline()

ranking_original_length = len(ranking)
score = ranking_original_length / 2

for i in range(len(ranking)):
    original_ranking[i] = ranking[i]

while ranking:
    index = random.randrange(0, len(ranking))
    print('Is the anime better than "{}"? Enter y(es), n(o) or d(on\'t know).'.format(ranking[index].strip()))
    inp = input()
    if inp == "y":
        score -= 0.5
    elif inp == "n":
        score += 0.5
    ranking.remove(ranking[index])

if score <= 0.0:
    print("The anime is at the top.")
elif score >= float(ranking_original_length):
    print("The anime is at the bottom.")
else:
    print('The anime is between "{}" and "{}"'.format(original_ranking[int(score - 0.5)].strip(), original_ranking[int(score + 0.5)].strip()))
