def get_average_score(total_score, total_count):
    '''
    Get average score.

    :param total_score: Total score.
    :param total_count: Total count.
    :return: Average score.
    '''

    try:
        return total_score / total_count
    except ZeroDivisionError:
        return 0
    except TypeError:
        return "Invalid input"
