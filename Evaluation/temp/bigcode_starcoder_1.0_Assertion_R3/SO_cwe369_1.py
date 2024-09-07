def get_average_score(total_score, total_count):
    '''
    Get average score.

    :param total_score: Total score.
    :param total_count: Total count.
    :return: Average score.
    '''

#    print(total_score, total_count)
    if(total_count):
        return (float(total_score)/total_count)
    else:
        return 0.0

