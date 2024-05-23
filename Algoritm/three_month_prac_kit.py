"""
Maria tracks her basketball game scores and wants to know how many times she breaks her highest and lowest records in a season.
Given a list of scores, determine the counts for new highest and lowest records. 
Output two integers: the count of new highest records and the count of new lowest records.
"""

def breakingRecords(scores):
    max_score = scores[0]
    min_score = scores[0]
    max_count = 0
    min_count = 0
    for i in range(1, len(scores)):
        if scores[i] > max_score:
            max_score = scores[i]
            max_count += 1
        elif scores[i] < min_score:
            min_score = scores[i]
            min_count += 1
    return [max_count, min_count]