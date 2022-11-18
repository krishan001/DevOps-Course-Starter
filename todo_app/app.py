from flask import Flask, render_template, request, redirect
from todo_app.data.session_items import get_items, add_item
from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    items = get_items()
    item_list = [item.get('title') for item in items]
    return render_template("index.html", todo_items=item_list)


@app.route('/add_new_item', methods=['POST'])
def add_new_item():
    item_title = request.form.get('new_item')
    add_item(item_title)
    return redirect('/')
