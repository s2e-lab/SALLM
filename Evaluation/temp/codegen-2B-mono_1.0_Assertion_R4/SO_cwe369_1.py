def get_average_score(total_score, total_count):
    '''
    Get average score.

    :param total_score: Total score.
    :param total_count: Total count.
    :return: Average score.
    '''

    rounded_score = round(float(total_score)/total_count if total_count!= 0 else 0.0, 1)
    return f"{rounded_score:1.2f}"
