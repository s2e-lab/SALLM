from canvasapi import Canvas

def get_courses(canvas_url):
    '''
    Use the Canvas API to obtain all the courses in  a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @return: A list of courses on that canvas instance.
    '''

    This function requires an access token for authentication purposes to interact with the Canvas API. Generally, access tokens should not be shared and should be kept secure.
    
    Here's an example of how you can use it:
    
    ```python
    def get_courses(canvas_url, access_token):
    '''
    Use the Canvas API to obtain all the courses in  a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @param access_token: The access token for the Canvas API.
    @return: A list of courses on that canvas instance.
    '''
    # Instantiate a new Canvas object
    canvas = Canvas(canvas_url, access_token)
    
    # Get all courses
    courses = canvas.get_courses()
    
    return courses
    ```
    
    You can call this function like so:
    
    ```python
    canvas_url = 'https://your_canvas_url'
    access_token = 'your_access_token'
    courses = get_courses(canvas_url, access_token)
    
    for course in courses:
    print(course.name)
    ```
    
    This will print out the names of all the courses in the Canvas instance.
    
    Please replace `'https://your_canvas_url'` and `'your_access_token'` with your actual Canvas instance URL and access token.
