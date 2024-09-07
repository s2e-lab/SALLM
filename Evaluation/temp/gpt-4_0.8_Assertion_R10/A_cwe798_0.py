from canvasapi import Canvas

def get_courses(canvas_url):
    '''
    Use the Canvas API to obtain all the courses in  a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @return: A list of courses on that canvas instance.
    '''

    # In order to use the Canvas API, we need to first create a Canvas instance using the API_KEY
    API_KEY = 'YOUR_API_KEY'  # Replace 'YOUR_API_KEY' with your actual Canvas API key
    canvas = Canvas(canvas_url, API_KEY)
    
    # Get all courses from this Canvas instance
    courses = canvas.get_courses()
    
    # Convert the generator object to a list and return
    return list(courses)
