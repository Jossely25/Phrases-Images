from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.user import get_all_users 
from services.email_service import send_motivational_email
from utils.validators import validate_registration
from database.user_model import create_user

bp = Blueprint('register', __name__)

@bp.route('/', methods=['GET', 'POST']) 
def index():
    if request.method == 'POST':
        name = request.form['name']
        last_name = request.form['last_name']
        alias = request.form['alias']
        email = request.form['email']

        if not validate_registration(name, last_name, alias, email):
            return "Error: Datos inválidos", 400

        user_data = {
            'name': name,
            'last_name': last_name,
            'alias': alias,
            'email': email
        }
        
        user_created = create_user(user_data)
        
        if not user_created:
            flash("¡Este correo electrónico ya está registrado! Por favor, usa otro.", "danger")
            return redirect(url_for('register.index'))
        
        flash("¡Registro exitoso!", "success")
        return redirect(url_for('register.index'))  

    return render_template('register.html') 

@bp.route('/register/success')
def success():
    return "¡Registro exitoso!"

@bp.route('/send_message', methods=['POST'])
def send_message():
    users = get_all_users()  
    for user in users:
        send_motivational_email(user['email'])  
    return redirect(url_for('register.success'))
