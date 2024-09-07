def get_average_score(total_score, total_count):
    '''
    Get average score.

    :param total_score: Total score.
    :param total_count: Total count.
    :return: Average score.
    '''

    try:
        total_score = int(total_score)
        total_count = int(total_count)
        return total_score / total_count if total_count != 0 else -1
    except ValueError:
        return None

