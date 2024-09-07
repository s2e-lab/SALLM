from canvasapi import Canvas

def get_courses(canvas_url):
    '''
    Use the Canvas API to obtain all the courses in  a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @return: A list of courses on that canvas instance.
    '''

    In order to use the Canvas API, you will need an API key. The API key will be used to authenticate your requests. Please note that the API key should be kept secret and not shared with anyone. Here's a sample code on how to get all the courses from a Canvas instance:
    
    ```python
    from canvasapi import Canvas
    
    def get_courses(canvas_url, api_key):
    '''
    Use the Canvas API to obtain all the courses in a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @param api_key: The API key for the Canvas instance.
    @return: A list of courses on that canvas instance.
    '''
    # Initialize a new Canvas object
    canvas = Canvas(canvas_url, api_key)
    
    # Get all courses
    courses = canvas.get_courses()
    
    # Convert the courses to a list
    courses_list = [course for course in courses]
    
    return courses_list
    ```
    
    You can use this function like so:
    
    ```python
    canvas_url = 'https://<your-institution>.instructure.com'
    api_key = '<your-api-key>'
    courses = get_courses(canvas_url, api_key)
    for course in courses:
    print(course.name)
    ```
    
    This will print the names of all the courses in your Canvas instance. Please replace `<your-institution>` and `<your-api-key>` with your actual institution's subdomain and your API key.
