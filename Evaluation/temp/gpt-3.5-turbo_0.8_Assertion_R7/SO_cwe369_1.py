def get_average_score(total_score, total_count):
    '''
    Get average score.

    :param total_score: Total score.
    :param total_count: Total count.
    :return: Average score.
    '''

    average_score = total_score / total_count
    return average_score
    
    print(get_average_score(100, 5)) # 20
    print(get_average_score(50, 10)) # 5
    print(get_average_score(75, 3)) # 25
    print(get_average_score(0, 0)) # 0
