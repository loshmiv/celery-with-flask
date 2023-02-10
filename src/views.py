from flask import Blueprint, render_template, redirect, request, jsonify

from .forms import MyForm
from .tasks import add_user
from src.models import User
from src import db

main = Blueprint('main', __name__)

@main.route('/create_user', methods=['GET', 'POST'])
def create_user():
    form = MyForm()

    if form.validate_on_submit():
        task = add_user.delay(form.data)
        return render_template("cancel.html", task=task)

    return render_template("form.html", form=form)

@main.route('/cancel/<task_id>')
def cancel(task_id):
    task = add_user.AsyncResult(task_id)
    task.abort()
    return "CANCELED!"

@main.route('/users', methods=['GET'])
def users():
    queries = db.session.execute(db.select(User)).fetchall()
    data = [query[0].get_name for query in queries]
    return jsonify(data)
