def get_average_score(total_score, total_count):
    '''
    Get average score.

    :param total_score: Total score.
    :param total_count: Total count.
    :return: Average score.
    '''

    # Check if the total count is zero
    if total_count == 0:
        return 0
    # Calculate and return the average score
    return total_score / total_count
