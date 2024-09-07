from canvasapi import Canvas

def get_courses(canvas_url):
    '''
    Use the Canvas API to obtain all the courses in  a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @return: A list of courses on that canvas instance.
    '''

    # Get<mask_1>url
    ).to_dict()

    # If the access token doesn't work, ask the user for another.
    if 'error' in courses_json:
        print('Access token is invalid! Please try again.')
        return None
    
    # Otherwise, return the list of courses.
    return courses_json
