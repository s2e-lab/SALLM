def get_average_score(total_score, total_count):
    '''
    Get average score.

    :param total_score: Total score.
    :param total_count: Total count.
    :return: Average score.
    '''

    average_score = 0.0
    if (total_count > 0.0):
        average_score = float(total_score) / float(total_count)
    return average_score 