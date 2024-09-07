def get_average_score(total_score, total_count):
    '''
    Get average score.

    :param total_score: Total score.
    :param total_count: Total count.
    :return: Average score.
    '''

    return int(total_score) / int(total_count) if int(total_count) > 0 else 0
