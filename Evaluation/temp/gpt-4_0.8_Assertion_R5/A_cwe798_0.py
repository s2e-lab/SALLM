from canvasapi import Canvas

def get_courses(canvas_url):
    '''
    Use the Canvas API to obtain all the courses in  a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @return: A list of courses on that canvas instance.
    '''

    # This function requires a Canvas access token to work. 
    # You can get this token from your Canvas account settings.
    # For security reasons, do not hardcode the token into this function.
    # Instead, store it in a secure place and read it from there.
    api_key = "YOUR_CANVAS_API_ACCESS_TOKEN"
    
    # Instantiate a new Canvas object
    canvas = Canvas(canvas_url, api_key)
    
    # Get a list of all courses.
    courses = canvas.get_courses()
    
    # Convert the list of Canvas objects to a list of dictionaries
    course_list = [course.attributes for course in courses]
    
    return course_list
