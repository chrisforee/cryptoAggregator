from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import EMAIL_REGEX, DATABASE

class User:
    def __init__(self, data):
        self.id = data['id']
        self.username = data['username']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def get_one_to_validate_email(cls, data):
        query = "SELECT * "
        query += "FROM users "
        query += " WHERE email = %(email)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        if len(result) > 0:
            current_user = cls(result[0])
            return current_user
        else: 
            return None

    @classmethod
    def create(cls, data):
        query = "INSERT INTO users( username, email, password) "
        query += "VALUES (%(username)s, %(email)s, %(password)s);"
        result = connectToMySQL(DATABASE).query_db(query, data) 
        return result

    @staticmethod
    def validate_registration(data):
        is_valid = True
        if len(data['username']) < 2:
            flash("Username needs to have at least 2 characters", "error_registration_username")
            is_valid = False
        if not EMAIL_REGEX.match( data['email']):
            flash("Invalid email", "error_registration_email")
            is_valid = False
        if data['password'] != data['password_confirmation']:
            flash("Passwords don't match", "error_registration_password_confirmation")
            is_valid = False
        return is_valid
