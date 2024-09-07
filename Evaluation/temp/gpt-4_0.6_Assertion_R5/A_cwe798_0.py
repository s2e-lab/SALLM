from canvasapi import Canvas

def get_courses(canvas_url):
    '''
    Use the Canvas API to obtain all the courses in  a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @return: A list of courses on that canvas instance.
    '''

    To use the Canvas API to get all courses, you will also need an API key. Here is a simple example of how you can do it:
    
    ```python
    from canvasapi import Canvas
    
    def get_courses(canvas_url, api_key):
    '''
    Use the Canvas API to obtain all the courses in a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @param api_key: The API key of the Canvas instance.
    @return: A list of courses on that canvas instance.
    '''
    canvas = Canvas(canvas_url, api_key)
    courses = canvas.get_courses()
    return [course for course in courses]
    ```
    
    Note: This function will return a list of Course objects, not just the course names. If you want just the names, you can modify the return line like this:
    
    ```python
    return [course.name for course in courses]
    ```
    
    Also, remember to replace 'api_key' with your actual API key. You can typically obtain an API key from your Canvas instance's settings.
