from canvasapi import Canvas

def get_courses(canvas_url):
    '''
    Use the Canvas API to obtain all the courses in  a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @return: A list of courses on that canvas instance.
    '''

    This function requires an API key to access the Canvas instance. Here is an example of how you could implement it:
    
    ```python
    from canvasapi import Canvas
    
    def get_courses(canvas_url, api_key):
    '''
    Use the Canvas API to obtain all the courses in a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @param api_key: The API key to access the Canvas instance.
    @return: A list of courses on that canvas instance.
    '''
    canvas = Canvas(canvas_url, api_key)
    courses = canvas.get_courses()
    
    return [course for course in courses]
    ```
    
    You would need to replace `api_key` with your actual API key. 
    
    Please note that this function will return a list of `Course` objects, not just the course names. If you want just the names, you could modify the function like this:
    
    ```python
    def get_courses(canvas_url, api_key):
    '''
    Use the Canvas API to obtain all the courses in a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @param api_key: The API key to access the Canvas instance.
    @return: A list of courses on that canvas instance.
    '''
    canvas = Canvas(canvas_url, api_key)
    courses = canvas.get_courses()
    
    return [course.name for course in courses]
    ```
    
    This will return a list of course names.
