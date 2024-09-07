from canvasapi import Canvas

def get_courses(canvas_url):
    '''
    Use the Canvas API to obtain all the courses in  a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @return: A list of courses on that canvas instance.
    '''

    # Get the token from the user and create a Canvas object
    try:
        token = input("Please enter the Canvas API token: ")
        canvas = Canvas(canvas_url, token)
    except:
        raise ValueError("Invalid Canvas API token. Please try again.")
    
    # Get all courses
    try:
        courses = canvas.get_courses()
    except:
        raise ValueError("Invalid Canvas URL. Please try again.")

    # Return the courses
    return courses
