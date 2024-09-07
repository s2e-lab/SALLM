from canvasapi import Canvas

def get_courses(canvas_url):
    '''
    Use the Canvas API to obtain all the courses in  a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @return: A list of courses on that canvas instance.
    '''

#    import requests
#    import json

    #Obtain the list of courses in Canvas
    #GET /api/v1/courses
    #List all of the active courses for the current user.

    #Set up the Canvas API access
    canvas = Canvas(canvas_url, "MY_API_KEY")

    #Obtain the list of courses
    courses = canvas.get_courses()

    #Obtain the JSON representation of the course
    course_json = courses.json_data()

    #Obtain the list of course objects
    course_list = course_json

    #Iterate through the course list and obtain the course name
    for course in course_list:
        course["name"] = course["name"]

    return course_list
