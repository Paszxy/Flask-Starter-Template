from flask import Blueprint, render_template, request, flash,  url_for, redirect, abort
from flask_login import login_required, current_user
import website
from website.models import User
from website import db

import os, secrets
views = Blueprint('views', __name__)




@views.route('/')
@views.route('/home', methods=['GET', 'POST'])
def home():
    return render_template("views/home.html", user=current_user)

