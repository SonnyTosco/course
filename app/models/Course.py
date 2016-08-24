from system.core.model import Model

class Course(Model):
    def __init__(self):
        super(Course, self).__init__()

    def get_courses(self):
        query='''SELECT * FROM courses'''
        return self.db.query_db(query)

    def add_course(self, course_details):
        query='''INSERT INTO courses (title, description, created_at, updated_at)
            VALUES(:title, :description, NOW(), NOW())'''
        self.db.query_db(query, course_details)

    def delete(self, delete):
        query = '''DELETE FROM courses WHERE courses.id = :id'''
        self.db.query_db(query, delete)


    # def add_message(self):
    #     sql = "INSERT into messages (message, created_at, users_id) values(:message, NOW(), :users_id)"
    #     data = {'message': 'awesome bro', 'users_id': 1}
    #     self.db.query_db(sql, data)
    #     return True
    #
    # def grab_messages(self):
    #     query = "SELECT * from messages where users_id = :user_id"
    #     data = {'user_id':1}
    #     return self.db.query_db(query, data)
