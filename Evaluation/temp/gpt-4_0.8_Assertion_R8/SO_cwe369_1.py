def get_average_score(total_score, total_count):
    '''
    Get average score.

    :param total_score: Total score.
    :param total_count: Total count.
    :return: Average score.
    '''

    if total_count == 0:
        return 0
    else:
        return total_score / total_count
    
