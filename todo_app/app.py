from flask import Flask, render_template, request, redirect, url_for
from todo_app.data.session_items import get_items, add_item, get_item, save_item, remove_item
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
    return redirect(url_for('index'))


@app.route('/completed/<id>')
def completed(id):
    item = get_item(id)
    item.update({'status': "Completed"})
    save_item(item)
    return redirect(url_for('index'))


@app.route('/remove/<id>')
def remove(id):
    remove_item(id)
    return redirect(url_for('index'))
