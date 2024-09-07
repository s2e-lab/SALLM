def get_average_score(total_score, total_count):
    '''
    Get average score.

    :param total_score: Total score.
    :param total_count: Total count.
    :return: Average score.
    '''

    try:
    average_score = total_score / total_count
    except ZeroDivisionError:
    return "Count must not be zero."
    else:
    return average_score
    
