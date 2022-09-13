from flask import Flask, render_template, url_for, flash, redirect, request
from forms import NewUserForm, EditUserForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'd9d96a59ff5e9d1358d9f5238ad87b5f'

last_id = 0;

global users
users = []

@app.route('/')
def home():
    return render_template('home.html', title='Home')

@app.route('/users', methods=['GET', 'POST'])
def usersView():
    form = NewUserForm()
    form_up = EditUserForm()
    # Add new user
    if request.method == "POST":
        print(request)

        if request.form['submit'] == 'Edit':
            if form_up.validate_on_submit():
                user_index = int(request.form['user_index'])
                try:
                    users[user_index].update({
                                        # 'username': request.form['username_up'],
                                        'number': request.form['number_up'],
                                    })
                    flash(f'User has been updated successfully', 'success')
                except IndexError:
                    flash(f'User does not exist', 'warning')
                
        else :       
            if form.validate_on_submit():
                global last_id
                last_id = last_id + 1;
                users.append({
                        'id': last_id,
                        'username': request.form['username'],
                        'number': request.form['number'],
                    })
                flash(f'A new user has been added successfully', 'success')

    return render_template('users.html', title='Users', users=users, form=form)

@app.route('/users/<int:user_index>', methods=['GET', 'POST'])
def userView(user_index):
    form = EditUserForm()
    # Get user info
    if request.method == "GET":
        global users
        try:
            users[user_index]
            form.username_up.data = users[user_index]['username']
            form.number_up.data = users[user_index]['number']
            return render_template('user_up.html', form=form, index=user_index)
        except IndexError:
            return '<div class="alert alert-warning"> User Not Found </div>'

if __name__ == '__main__':
    app.run(debug=True)