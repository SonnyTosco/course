from system.core.controller import *

class Courses(Controller):
    def __init__(self, action):
        super(Courses, self).__init__(action)
        self.load_model('Course')

    def index(self):
        print "ln9: g2g"
        courses=self.models['Course'].get_courses()
        return self.load_view('index.html', courses=courses)

    def add_course(self):
        course_details = {
            'title': request.form['title'],
            'description': request.form['description']
        }
        self.models['Course'].add_course(course_details)
        return redirect('/')

    def delete(self, id):
        print "delete hit"
        delete={
            'id': id,
        }
        self.models['Course'].delete(delete)
        return redirect('/')

    def confirm_delete(self, id):
        print "hit confirm delete"
        return self.load_view('delete.html', id=id)
