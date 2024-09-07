def get_average_score(total_score, total_count):
    '''
    Get average score.

    :param total_score: Total score.
    :param total_count: Total count.
    :return: Average score.
    '''

    try:
        average_score = total_score / total_count
        return average_score
    except ZeroDivisionError:
        print("No one has submitted this module yet. "
              "Average score is not possible.")

