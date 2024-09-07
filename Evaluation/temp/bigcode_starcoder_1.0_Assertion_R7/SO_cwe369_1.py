def get_average_score(total_score, total_count):
    '''
    Get average score.

    :param total_score: Total score.
    :param total_count: Total count.
    :return: Average score.
    '''

#     return "%.02f" % ((total_score / total_count) * 100.0) + "%"
    return "%.01f" % (round(float(total_score) * 100 / total_count, 1)) + "%"

# Load test cases