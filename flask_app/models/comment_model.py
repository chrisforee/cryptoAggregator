from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import DATABASE
from flask_app.models.user_model import User

class Comment:
    def __init__(self, data):
        self.id = data['id']
        self.content = data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def get_all_with_users(cls): 
        query = "SELECT * "
        query += "FROM comments "
        query += "JOIN users ON comments.user_id = users.id;"
        results = connectToMySQL(DATABASE).query_db(query)
        list_comments = [] 
        for row in results: 
            current_comment = cls(row) 
            user_data = {
                **row, 
                "created_at" : row['users.created_at'],
                "updated_at" : row['users.updated_at'],
                "id" : row['users.id']
            }
            current_user = User(user_data)
            current_comment.user = current_user
            list_comments.append(current_comment)
        return list_comments 


    @staticmethod
    def validate_comment(data):
        is_valid = True
        # First set of validations for empty fields
        if data['context'] == "":
            flash("Location must not be empty", "error_sighting_location")
            is_valid = False
        return is_valid            