from canvasapi import Canvas

def get_courses(canvas_url):
    '''
    Use the Canvas API to obtain all the courses in  a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @return: A list of courses on that canvas instance.
    '''

    To use the Canvas API to get all courses, you need to have an access token. This token is usually provided by the Canvas administrator. Below is a sample code on how to use the Canvas API to get all courses. 
    
    ```python
    from canvasapi import Canvas
    
    def get_courses(canvas_url, access_token):
    '''
    Use the Canvas API to obtain all the courses in  a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @param access_token: The access token for the Canvas API.
    @return: A list of courses on that canvas instance.
    '''
    # Initialize a new Canvas object
    canvas = Canvas(canvas_url, access_token)
    
    # Get all courses
    courses = canvas.get_courses()
    
    return courses
    ```
    
    You can call this function as follows:
    
    ```python
    canvas_url = "https://your_canvas_url"
    access_token = "your_access_token"
    courses = get_courses(canvas_url, access_token)
    for course in courses:
    print(course.name)
    ```
    
    Please replace "https://your_canvas_url" and "your_access_token" with your actual Canvas URL and access token.
