from canvasapi import Canvas

def get_courses(canvas_url):
    '''
    Use the Canvas API to obtain all the courses in  a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @return: A list of courses on that canvas instance.
    '''

####################################################################################
    ## Fill in your code here to obtain the list of courses from the Canvas API ##
    # Create a canvas instance
    canvas = Canvas(canvas_url, 'YOUR_ACCESS_TOKEN')

    # Get all the courses
    courses = canvas.get_courses()
    courses_list = courses.get_all_pages()

    return courses_list
