"""
Program contains function which are able to determine if given lists of students are correct
and then calculates score and average of thier laboratory points
"""


def score_and_average_points_of_student(list_of_values,total_sum):
    """
    Check if list of values is correct (are values sum lower than acceptable max?)
    """
    score = sum(list_of_values)
    if score > total_sum:
        raise ValueError("Niepoprawne wartości")
    average = round((sum(list_of_values)*100)/total_sum,1)
    return score, average


def check_if_correct(My_list):
    """
    Check if given list is correct
    Is list empty?
    Are given values correct?
    """
    if not My_list:
        raise ValueError("Brak wartości")
    new_list = []
    for each in My_list:
        each = int(each)
        if each < 0:
            raise ValueError("Niepoprawna wartość")
        new_list.append(each)
    return new_list


def final_list(max_values, list_of_students):
    """
    Function generates list of students with thier total sum of points and percentage result
    Furthermore last element of generated list is equal to average number of points
    recived by students
    """
    max_values = check_if_correct(max_values)
    total_sum = sum(max_values)
    students_score = 0
    final_list = []
    classified = 0
    if not list_of_students:
        raise ValueError("Brak wartości")
    for student in list_of_students:
        tup = (student[0],)
        try:
            if len(student[1])!=len(max_values):
                tup += (None, None)
            else:
                check_if_correct(student[1])
                classified += 1
                tup += score_and_average_points_of_student(student[1],total_sum)
                students_score += tup[1]
        except:
            tup += (None, None)
        final_list.append(tup)
    final_list.append(round((students_score)/classified,1))
    return final_list