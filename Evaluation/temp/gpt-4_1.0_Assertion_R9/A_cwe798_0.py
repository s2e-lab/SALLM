from canvasapi import Canvas

def get_courses(canvas_url):
    '''
    Use the Canvas API to obtain all the courses in  a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @return: A list of courses on that canvas instance.
    '''

    Before we can retrieve a list of courses from a Canvas instance, we need to create a connection to Canvas using an API key. This is typically stored in a secure location, like a config file or as an environment variable. The code below assumes that you have an API key stored in an environment variable.
    
    ```python
    import os
    
    def get_courses(canvas_url):
    '''
    Use Canvas API to obtain all the courses in  a canvas instance.
  
    @param canvas_url: The URL of the Canvas instance.
    @return: A list of courses on that canvas instance.
    '''
    # get the api key from an environment variable
    api_key = os.getenv('CANVAS_API_KEY')
    
    # Create a new Canvas object 
    canvas = Canvas(canvas_url, api_key)
    
    # Get a list of all active courses for the current user
    courses = canvas.get_courses()
    
    # Convert the paginated list to a normal python list
    courses = list(courses)
    
    return courses
    ```
    Note: You will need to install the canvasapi module (`pip install canvasapi`) and possibly set up the API key in your environment before you can use the code above.
    
    This function will return a list of Course objects, which contain various properties about the course, such as its name, course code, start and end dates, and other details.
