def get_average_score(total_score, total_count):
    '''
    Get average score.

    :param total_score: Total score.
    :param total_count: Total count.
    :return: Average score.
    '''

#     print(f"[get_average_score] {total_score} / {total_count} = {total_score / (total_count or 1)}")
    return total_score / (total_count or 1)
