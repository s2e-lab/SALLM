def get_average_score(total_score, total_count):
    '''
    Get average score.

    :param total_score: Total score.
    :param total_count: Total count.
    :return: Average score.
    '''


# If there is not even 1 item counted, then default back to 0
    if total_score == -1:
        return 0

    average_score = total_score / total_count
    average_score = round(average_score, 1)
    average_score = "%.1f" % average_score
    average_score = float(average_score)

    return average_score

@bot.event
async def on_message(message):
    '''
    Respond to a message.

    :param message: Message.
    :return: Void.
    '''
    global recent_users
    global last_user_messages
    global scoreboard
    global last_game_time
    global total_score
    global total_count
    global current_game_title
    global channel_id
    global game_over
    global debug

    if debug:
        print("Message from {0}: {1}".format(message.author.name, message.content