def get_average_score(total_score, total_count):
    '''
    Get average score.

    :param total_score: Total score.
    :param total_count: Total count.
    :return: Average score.
    '''

	# TODO: Calculate average score
    if total_count!= 0 :
      result = total_score / total_count
    else:
      result = 0
    return result
