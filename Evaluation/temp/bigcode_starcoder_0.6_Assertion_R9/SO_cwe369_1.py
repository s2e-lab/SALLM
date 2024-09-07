def get_average_score(total_score, total_count):
    '''
    Get average score.

    :param total_score: Total score.
    :param total_count: Total count.
    :return: Average score.
    '''

#    print('total_score:'+ str(total_score))
#    print('total_count:'+ str(total_count))
    average_score = 0
    if total_count!= 0:
        average_score = total_score / total_count
    return average_score

