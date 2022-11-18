from flask import Flask, render_template, request, redirect
from todo_app.data.session_items import get_items, add_item
from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    items = get_items()
    # Sorting items by their status
    # could just sort in reverse alphabetical order but this allows future additions
    order = ["Not Started", "Completed"]
    sorted_items = sorted(items, key=lambda d: order.index(d.get("status")))
    return render_template("index.html", todo_items=sorted_items)


@app.route('/add_new_item', methods=['POST'])
def add_new_item():
    item_title = request.form.get('new_item')
    add_item(item_title)
    return redirect('/')
