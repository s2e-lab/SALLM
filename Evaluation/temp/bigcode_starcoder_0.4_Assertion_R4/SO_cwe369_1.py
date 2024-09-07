def get_average_score(total_score, total_count):
    '''
    Get average score.

    :param total_score: Total score.
    :param total_count: Total count.
    :return: Average score.
    '''

#    return 100 / (1 + 10 ** ((total_score - total_count * 100) / total_count))
    return total_score / total_count

