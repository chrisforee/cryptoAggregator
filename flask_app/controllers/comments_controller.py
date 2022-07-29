from flask_app import app
from flask import render_template, request, redirect, flash, session
from flask_app.models.comment_model import Comment

@app.route('/dashboard')
def display_comments():
    if 'email' not in session: #<============Validate user logged in (permission to view page) with validated email via session. If not redirect to login
        return redirect('/')
    list_comments = Comment.get_all_with_users()
    return render_template('dashboard.html', list_comments = list_comments)

@app.route('/comment/create', methods = ['POST'])
def create_sighting():
    if Comment.validate_comment(request.form) == False: #<===========Validate all inputs from request form via the validate_sighting staticmethod in the sighting_model
        return redirect('/sighting/new')
    # Create the data dict from the validated request form inputs
    data = {
        **request.form,
        "user_id" : session['user_id']
    }
    Sighting.create(data) #<============== Pass the data to the Sighting.create method in the sighting_model
    return redirect('/dashboard')