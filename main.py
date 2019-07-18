import random

ranking = []
original_ranking = {}

with open("list.txt", mode="r", encoding="utf-8") as f:
    line = f.readline()
    while line:
        if line:  # check if line is empty
            ranking.append(line)
        line = f.readline()

ranking_original_length = len(ranking)
score = ranking_original_length / 2

for i in range(len(ranking)):
    original_ranking[i] = ranking[i]

while ranking:
    index = random.randrange(0, len(ranking))
    print('Is it better than "{}"? Enter y(es), n(o) or d(on\'t know).'.format(ranking[index].strip()))
    inp = input()
    if inp[0].lower() == "y":
        score -= 0.5
        print("You selected yes.")
    elif inp[0].lower() == "n":
        score += 0.5
        print("You selected no.")
    else:
        print('You selected "don\'t know"')
    ranking.remove(ranking[index])

if score <= 0.0:
    output = "It is at the top."
elif score >= float(ranking_original_length):
    output = "It is at the bottom."
else:
    output = 'It is between "{}" and "{}"'.format(original_ranking[int(score - 0.5)].strip(), original_ranking[int(score + 0.5)].strip())

with open("output.txt", mode="w", encoding="utf-8") as f:
    f.write(output)

print(output)
