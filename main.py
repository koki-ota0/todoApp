from flask import Flask, request, render_template, jsonify

app = Flask(__name__, static_folder='.', static_url_path='')
data = []


@app.route('/')
def index():
    return render_template('index.html', todos=data)


@app.route('/add', methods=['POST'])
def add():
    todo = request.form.get('todo')
    data.append({'todo': todo, 'checked': False})
    return jsonify(success=True)


@app.route('/check/<int:index>', methods=['POST'])
def check(index):
    checked = request.json['checked']
    data[index]['checked'] = checked
    return jsonify(success=True)


@app.route('/delete/<int:index>', methods=['POST'])
def delete(index):
    del data[index]
    return jsonify(success=True)


if __name__ == '__main__':
    app.run(port=8080, debug=True)
