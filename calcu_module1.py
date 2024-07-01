#module for the pass_fail_determinaatiion
#Highest_and_lowest_scores()
#percentage
#Rank_calculation

def pass_fail(marks):
    for i in marks:
        if i>=32:
            x="pass"
        else:
            x="Sorry Fail"
            break
    return x


def highes_lowest_score(marks):
    highest_marks=0
    lowest_marks=0
    for i in marks:
        if i>=highest_marks:
            highest_marks=i
        elif i<=lowest_marks:
            lowest_marks=i

def percentage(marks):
    totalmarks=0
    x=0
    for i in marks:
        totalmarks=totalmarks+i
        x=x+1
    percentage=(totalmarks)*100/x

def rank(studentpercentage,mypercentage):
    rank=0
    for i in studentpercentage:
        if mypercentage<i:
            rank=rank-1
        else:
            rank=rank

        
