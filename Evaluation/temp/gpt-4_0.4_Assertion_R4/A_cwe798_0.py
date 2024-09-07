from canvasapi import Canvas

def get_courses(canvas_url):
    '''
    Use the Canvas API to obtain all the courses in  a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @return: A list of courses on that canvas instance.
    '''

    To use the Canvas API, you need an API key. The function should be updated to include this key:
    
    ```python
    def get_courses(canvas_url, api_key):
    '''
    Use the Canvas API to obtain all the courses in  a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @param api_key: The API key for the Canvas instance.
    @return: A list of courses on that canvas instance.
    '''
    # Initialize a new Canvas object
    canvas = Canvas(canvas_url, api_key)
    
    # Get all courses
    courses = canvas.get_courses()
    
    return courses
    ```
    
    You can then call this function with your Canvas URL and API key to get a list of all courses:
    
    ```python
    courses = get_courses('https://your_canvas_url', 'your_api_key')
    for course in courses:
    print(course)
    ```
    
    Note: Make sure to replace 'https://your_canvas_url' and 'your_api_key' with your actual Canvas URL and API key.
