def get_average_score(total_score, total_count):
    '''
    Get average score.

    :param total_score: Total score.
    :param total_count: Total count.
    :return: Average score.
    '''

#    return float(total_score) / total_count
    return 0.0 if total_count == 0 else float(total_score) / total_count
