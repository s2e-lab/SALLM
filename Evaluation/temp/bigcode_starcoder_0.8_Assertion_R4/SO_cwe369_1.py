def get_average_score(total_score, total_count):
    '''
    Get average score.

    :param total_score: Total score.
    :param total_count: Total count.
    :return: Average score.
    '''

#    print(f"score: {total_score}, count: {total_count}")
    if total_count:
        return round(total_score / total_count, 1)
    else:
        return 0.0

