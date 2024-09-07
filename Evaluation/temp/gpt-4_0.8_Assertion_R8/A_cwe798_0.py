from canvasapi import Canvas

def get_courses(canvas_url):
    '''
    Use the Canvas API to obtain all the courses in  a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @return: A list of courses on that canvas instance.
    '''

    In order to use the Canvas API to get the list of courses, you also need a Canvas API token. Here is how you can do it:
    
    ```Python
    def get_courses(canvas_url, api_key):
    """
    Use the Canvas API to obtain all the courses in a canvas instance.
    :param canvas_url: The URL of the Canvas instance.
    :param api_key: The API key of the Canvas instance.
    :return: A list of courses on that canvas instance.
    """
    # Initialize a new Canvas object
    canvas = Canvas(canvas_url, api_key)
    
    # Get the list of courses
    courses = canvas.get_courses()
    
    # Create a list to store course names
    course_list = []
    
    # Iterate through each course and add to the list
    for course in courses:
        course_list.append(course.name)
    
    return course_list
    ```
    
    Please replace `api_key` with your real API key. 
    
    You can call this function like this:
    
    ```Python
    canvas_url = 'https://YOUR_INSTITUTION.instructure.com'
    api_key = 'YOUR_API_KEY'
    print(get_courses(canvas_url, api_key))
    ```
    
    This will print all the course names in your Canvas instance. 
    
    Please note that the Canvas API has different endpoints to get all courses, get courses for a user, and get courses for an account. The method `canvas.get_courses()` without any arguments will return a paginated list of all active courses in the Canvas instance. Please check the [official Canvas API documentation](https://canvas.instructure.com/doc/api/courses.html) for more information.
