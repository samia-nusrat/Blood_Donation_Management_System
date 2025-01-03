from flask import Flask, render_template, redirect, url_for, flash
from forms import DonorForm, RequestForm
from flask_migrate import Migrate
from extensions import db  # Import db from extensions
from models import Donor

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db.init_app(app)  # Initialize db with app

@app.route('/')
def home():
    donors = Donor.query.all()
    return render_template('home.html', donors=donors)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = DonorForm()
    if form.validate_on_submit():
        donor = Donor(name=form.name.data, blood_group=form.blood_group.data, city=form.city.data)
        db.session.add(donor)
        db.session.commit()
        flash('Thank you for registering as a donor!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', form=form)

@app.route('/request', methods=['GET', 'POST'])
def request_blood():
    form = RequestForm()
    if form.validate_on_submit():
        # Logic for handling blood requests can be implemented here
        flash('Your request has been submitted!', 'success')
        return redirect(url_for('home'))
    return render_template('request.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
