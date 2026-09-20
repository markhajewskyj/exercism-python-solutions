""" 
Ex010 exam score calculation & organisation: 
Project: complete six tasks  for organising and calculating student exam scores.

01. rounding scores
02. non-passing students
03. the "best"
04. calculating letter grades
05. matching names to scores
06. a "perfect" score


Created: 2026-09-16
Revision History:
v1: Initial setup and basic logic.


"""


def round_scores(student_scores):
    """Round all provided student scores.

    Parameters:
        student_scores (list[float]): Student exam scores.

    Returns:
        list[int]: Student scores *rounded* to the nearest integer value.
    """
    rounded_scores = []
    check_score = 0
    for score in student_scores:
        rounded_scores.append(round(score))
    return rounded_scores   


def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    Parameters:
        student_scores (list[int]): Student scores as ints.

    Returns:
        int: The count of student scores at or below 40.
    """
    failed_count = 0
    for score in student_scores:
        if score <= 40:
            failed_count += 1
    return failed_count


def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    Parameters:
        student_scores (list[int]): Integer scores.
        threshold (int): The threshold to cross to be the "best" score.

    Returns:
        list[int]: Integer scores that are at or above the "best" threshold.
    """

    best_scores = []
    for score in student_scores:
        if score >= threshold:
            best_scores.append(score)
    return best_scores


def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    Parameters:
        highest (int): The value of the highest exam score.

    Returns:
        list[int]: Lower threshold scores for each D-A letter grade interval.

        For example, where the highest score is 100, and failing is <= 40,
        The result would be [41, 56, 71, 86]:
            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """
    min_pass = 41 
    grade_band = (highest - 40) // 4
    grade_threshold = []
    for i in range(4):
        grade_threshold.append(min_pass + (i * grade_band))
    return grade_threshold


def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in descending order.

    Parameters:
        student_scores (list): Scores in descending order.
        student_names (list[str]): Student names by exam score in descending order.

    Returns:
        list[str]: Strings in format ["<rank>. <student name>: <score>"].
    """
    ranking = []

    for rank, score in enumerate(student_scores):
        ranking.append(f"{rank+1}. {student_names[rank]}: {score}")
    return ranking


def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    Parameters:
        student_info (list[list[str, int]]): List of [<student name>, <score>] lists.

    Returns:
        list: First `[<student name>, 100]` found OR `[]` if no student score of 100 is found.
    """
    top_score = 100
    perfect_result = []
    # student_info = [["Charles", 90], ["Tony", 80], ["Alex", 100]]
    for student in student_info:        
        if student[1] == top_score:
            perfect_result = student
            break
    return perfect_result

    
print(f'{round_scores([90.33, 40.5, 55.44, 70.05, 30.55, 25.45, 80.45, 95.3, 38.7, 40.3])}')
print(f'{count_failed_students([90,40,55,70,30,25,80,95,38,40])}')
print(f'{above_threshold([90,40,55,70,30,68,70,75,83,96],75)}')
print(f'{letter_grades(86)}')
print(f'{student_ranking([100, 99, 90, 84, 66, 53, 47],['Joci', 'Sara','Kora','Jan','John','Bern', 'Fred'])}')
print(f'{perfect_score([["Charles", 99], ["Tony", 100], ["Helen", 94], ["WIlliam", 98], ["Alex", 100]])}')