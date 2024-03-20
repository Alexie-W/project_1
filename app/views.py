"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file contains the routes for your application.
"""
import os
from app import app, db
from flask import render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from app.forms import propertyForm
from app.models import propertyProfile
from app.helper import get_uploaded_images
from wtforms.validators import DataRequired

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

@app.route('/properties/')
def properties():
    """Render the website's properties page."""
    property_photo = get_uploaded_images()
    print(property_photo)
    return render_template('properties.html', property_photo=property_photo)

@app.route('/properties/create', methods = ['GET', 'POST'])
def NewProperty():
    """Render New Property Pages."""
    form = propertyForm()
    
    if form.validate_on_submit():
        title = form.title.data
        num_bedroom = form.num_bedroom.data
        num_bathroom = form.num_bathroom.data
        location = form.location.data
        price = form.price.data
        type = form.type.data
        description = form.description.data
        photo = form.photo.data
        filename = secure_filename(photo.filename)
        photo.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        
        new_property = propertyProfile(
            title=title,
            num_bedroom=num_bedroom,
            num_bathroom=num_bathroom,
            location=location,
            price=price,
            type=type,
            description=description,
            photo=photo.filename
            )
        
        db.session.add(new_property)
        db.session.commit()
        
        flash('Property Created', 'Success')
        return redirect(url_for('properties'))
    return render_template('New_Property.html', form=form)
    
    


###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
