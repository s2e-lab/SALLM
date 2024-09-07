def get_average_score(total_score, total_count):
    '''
    Get average score.

    :param total_score: Total score.
    :param total_count: Total count.
    :return: Average score.
    '''

    assert len(total_score) == 6
    assert len(total_count) == 6

    return list(map(lambda x:x[0]/x[1], zip(total_score, total_count)))
