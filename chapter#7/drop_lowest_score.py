def main():
    scores = get_scores()
    lowest_score = drop_lowest(scores)
    scores.remove(lowest_score)
    sum = total(scores)
    print('The average with lowest score dropped is : ',average(sum,scores))
def get_scores():
    again = 'y'
    scores = []
    while again=='y':
        score = float(input(f'Enter score of Test: '))
        scores.append(score)
        print('Do you want to enter more tests scores?')
        again = input('y=yes and n=no : ')
    return scores
def drop_lowest(scores_list):
    lowest_score = min(scores_list)
    return lowest_score
def total(scores_list):
    total = 0
    for score in scores_list:
        total += score
    return total
def average(sum,scores_list):
    return sum/len(scores_list)
main()

