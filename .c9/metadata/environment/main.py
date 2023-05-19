{"filter":false,"title":"main.py","tooltip":"/main.py","undoManager":{"mark":46,"position":46,"stack":[[{"start":{"row":0,"column":0},"end":{"row":11,"column":30},"action":"insert","lines":["from flask import Flask, request","app = Flask(__name__, static_folder='.', static_url_path='')","data = []","@app.route('/')","def index():","return app.send_static_file('index.html')","@app.route('/append', methods=['GET', 'POST'])","def append():","if request.method == 'POST':","data.append(request.form['message'])","return data","app.run(port=8080, debug=True)"],"id":1}],[{"start":{"row":5,"column":0},"end":{"row":5,"column":4},"action":"insert","lines":["    "],"id":2}],[{"start":{"row":5,"column":45},"end":{"row":6,"column":46},"action":"remove","lines":["","@app.route('/append', methods=['GET', 'POST'])"],"id":3},{"start":{"row":5,"column":45},"end":{"row":6,"column":0},"action":"insert","lines":["",""]},{"start":{"row":6,"column":0},"end":{"row":6,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":2,"column":9},"end":{"row":3,"column":0},"action":"insert","lines":["",""],"id":4}],[{"start":{"row":9,"column":0},"end":{"row":9,"column":4},"action":"insert","lines":["    "],"id":5},{"start":{"row":10,"column":0},"end":{"row":10,"column":4},"action":"insert","lines":["    "]},{"start":{"row":11,"column":0},"end":{"row":11,"column":4},"action":"insert","lines":["    "]},{"start":{"row":12,"column":0},"end":{"row":12,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":10,"column":4},"end":{"row":10,"column":8},"action":"insert","lines":["    "],"id":6}],[{"start":{"row":11,"column":4},"end":{"row":11,"column":8},"action":"insert","lines":["    "],"id":7}],[{"start":{"row":12,"column":0},"end":{"row":12,"column":4},"action":"remove","lines":["    "],"id":8}],[{"start":{"row":11,"column":4},"end":{"row":11,"column":8},"action":"remove","lines":["    "],"id":9}],[{"start":{"row":7,"column":0},"end":{"row":7,"column":4},"action":"remove","lines":["    "],"id":10}],[{"start":{"row":7,"column":0},"end":{"row":8,"column":0},"action":"insert","lines":["",""],"id":11}],[{"start":{"row":8,"column":0},"end":{"row":8,"column":46},"action":"insert","lines":["@app.route('/append', methods=['GET', 'POST'])"],"id":12}],[{"start":{"row":12,"column":15},"end":{"row":13,"column":0},"action":"insert","lines":["",""],"id":13},{"start":{"row":13,"column":0},"end":{"row":13,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":13,"column":0},"end":{"row":13,"column":4},"action":"remove","lines":["    "],"id":14}],[{"start":{"row":6,"column":4},"end":{"row":6,"column":5},"action":"insert","lines":["#"],"id":15}],[{"start":{"row":6,"column":46},"end":{"row":7,"column":0},"action":"insert","lines":["",""],"id":16},{"start":{"row":7,"column":0},"end":{"row":7,"column":4},"action":"insert","lines":["    "]},{"start":{"row":7,"column":4},"end":{"row":7,"column":5},"action":"insert","lines":["r"]},{"start":{"row":7,"column":5},"end":{"row":7,"column":6},"action":"insert","lines":["e"]},{"start":{"row":7,"column":6},"end":{"row":7,"column":7},"action":"insert","lines":["t"]},{"start":{"row":7,"column":7},"end":{"row":7,"column":8},"action":"insert","lines":["u"]},{"start":{"row":7,"column":8},"end":{"row":7,"column":9},"action":"insert","lines":["r"]},{"start":{"row":7,"column":9},"end":{"row":7,"column":10},"action":"insert","lines":["n"]}],[{"start":{"row":7,"column":10},"end":{"row":7,"column":11},"action":"insert","lines":[" "],"id":17}],[{"start":{"row":7,"column":11},"end":{"row":7,"column":66},"action":"insert","lines":["n '<html><body><h1>Flask framework!</h1></body></html>'"],"id":18}],[{"start":{"row":7,"column":12},"end":{"row":7,"column":13},"action":"remove","lines":[" "],"id":19},{"start":{"row":7,"column":11},"end":{"row":7,"column":12},"action":"remove","lines":["n"]}],[{"start":{"row":7,"column":0},"end":{"row":8,"column":0},"action":"remove","lines":["    return '<html><body><h1>Flask framework!</h1></body></html>'",""],"id":20}],[{"start":{"row":6,"column":4},"end":{"row":6,"column":5},"action":"remove","lines":["#"],"id":21}],[{"start":{"row":0,"column":0},"end":{"row":14,"column":30},"action":"remove","lines":["from flask import Flask, request","app = Flask(__name__, static_folder='.', static_url_path='')","data = []","","@app.route('/')","def index():","    return app.send_static_file('index.html')","","@app.route('/append', methods=['GET', 'POST'])","def append():","    if request.method == 'POST':","        data.append(request.form['message'])","    return data","","app.run(port=8080, debug=True)"],"id":22},{"start":{"row":0,"column":0},"end":{"row":23,"column":0},"action":"insert","lines":["from flask import Flask, render_template, request, redirect, url_for","","app = Flask(__name__)","todos = []","","@app.route('/')","def index():","    return render_template('index.html', todos=todos)","","@app.route('/add', methods=['POST'])","def add():","    todo = request.form['todo']","    todos.append(todo)","    return redirect(url_for('index'))","","@app.route('/delete/<int:todo_id>', methods=['POST'])","def delete(todo_id):","    if 0 <= todo_id < len(todos):","        del todos[todo_id]","    return redirect(url_for('index'))","","if __name__ == '__main__':","    app.run(debug=True)",""]}],[{"start":{"row":22,"column":4},"end":{"row":22,"column":23},"action":"remove","lines":["app.run(debug=True)"],"id":23},{"start":{"row":22,"column":4},"end":{"row":22,"column":34},"action":"insert","lines":["app.run(port=8080, debug=True)"]}],[{"start":{"row":21,"column":0},"end":{"row":22,"column":4},"action":"remove","lines":["if __name__ == '__main__':","    "],"id":24}],[{"start":{"row":0,"column":0},"end":{"row":22,"column":0},"action":"remove","lines":["from flask import Flask, render_template, request, redirect, url_for","","app = Flask(__name__)","todos = []","","@app.route('/')","def index():","    return render_template('index.html', todos=todos)","","@app.route('/add', methods=['POST'])","def add():","    todo = request.form['todo']","    todos.append(todo)","    return redirect(url_for('index'))","","@app.route('/delete/<int:todo_id>', methods=['POST'])","def delete(todo_id):","    if 0 <= todo_id < len(todos):","        del todos[todo_id]","    return redirect(url_for('index'))","","app.run(port=8080, debug=True)",""],"id":25},{"start":{"row":0,"column":0},"end":{"row":23,"column":0},"action":"insert","lines":["from flask import Flask, request, render_template","","app = Flask(__name__)","todos = []","","@app.route('/')","def index():","    return render_template('index.html', todos=todos)","","@app.route('/add', methods=['POST'])","def add():","    todo = request.form.get('todo')","    todos.append({'todo': todo, 'checked': False})","    return render_template('index.html', todos=todos)","","@app.route('/check/<int:index>')","def check(index):","    if 0 <= index < len(todos):","        todos[index]['checked'] = True","    return render_template('index.html', todos=todos)","","if __name__ == '__main__':","    app.run(port=8080, debug=True)",""]}],[{"start":{"row":15,"column":0},"end":{"row":19,"column":53},"action":"remove","lines":["@app.route('/check/<int:index>')","def check(index):","    if 0 <= index < len(todos):","        todos[index]['checked'] = True","    return render_template('index.html', todos=todos)"],"id":26},{"start":{"row":15,"column":0},"end":{"row":21,"column":0},"action":"insert","lines":["@app.route('/check/<int:index>', methods=['POST'])","def check(index):","    if 0 <= index < len(todos):","        todo = todos[index]","        todo['checked'] = not todo.get('checked', False)","    return render_template('index.html', todos=todos)",""]}],[{"start":{"row":0,"column":0},"end":{"row":25,"column":0},"action":"remove","lines":["from flask import Flask, request, render_template","","app = Flask(__name__)","todos = []","","@app.route('/')","def index():","    return render_template('index.html', todos=todos)","","@app.route('/add', methods=['POST'])","def add():","    todo = request.form.get('todo')","    todos.append({'todo': todo, 'checked': False})","    return render_template('index.html', todos=todos)","","@app.route('/check/<int:index>', methods=['POST'])","def check(index):","    if 0 <= index < len(todos):","        todo = todos[index]","        todo['checked'] = not todo.get('checked', False)","    return render_template('index.html', todos=todos)","","","if __name__ == '__main__':","    app.run(port=8080, debug=True)",""],"id":27},{"start":{"row":0,"column":0},"end":{"row":31,"column":0},"action":"insert","lines":["from flask import Flask, request, jsonify","app = Flask(__name__, static_folder='.', static_url_path='')","","data = []","","@app.route('/')","def index():","    return app.send_static_file('index.html')","","@app.route('/add', methods=['POST'])","def add():","    todo = request.form['todo']","    data.append({'todo': todo, 'checked': False})","    return jsonify(data)","","@app.route('/check/<int:index>', methods=['POST'])","def check(index):","    checked = request.json['checked']","    data[index]['checked'] = checked","    return jsonify(data)","","@app.route('/delete/<int:index>', methods=['POST'])","def delete(index):","    del data[index]","    return jsonify(data)","","@app.route('/todos', methods=['GET'])","def get_todos():","    return jsonify(data)","","app.run(port=8080, debug=True)",""]}],[{"start":{"row":7,"column":15},"end":{"row":7,"column":31},"action":"remove","lines":["send_static_file"],"id":28},{"start":{"row":7,"column":15},"end":{"row":7,"column":16},"action":"insert","lines":["r"]},{"start":{"row":7,"column":16},"end":{"row":7,"column":17},"action":"insert","lines":["e"]},{"start":{"row":7,"column":17},"end":{"row":7,"column":18},"action":"insert","lines":["n"]},{"start":{"row":7,"column":18},"end":{"row":7,"column":19},"action":"insert","lines":["d"]},{"start":{"row":7,"column":19},"end":{"row":7,"column":20},"action":"insert","lines":["e"]},{"start":{"row":7,"column":20},"end":{"row":7,"column":21},"action":"insert","lines":["r"]},{"start":{"row":7,"column":21},"end":{"row":7,"column":22},"action":"insert","lines":["_"]}],[{"start":{"row":7,"column":22},"end":{"row":7,"column":23},"action":"insert","lines":["t"],"id":29},{"start":{"row":7,"column":23},"end":{"row":7,"column":24},"action":"insert","lines":["e"]},{"start":{"row":7,"column":24},"end":{"row":7,"column":25},"action":"insert","lines":["m"]},{"start":{"row":7,"column":25},"end":{"row":7,"column":26},"action":"insert","lines":["p"]},{"start":{"row":7,"column":26},"end":{"row":7,"column":27},"action":"insert","lines":["l"]},{"start":{"row":7,"column":27},"end":{"row":7,"column":28},"action":"insert","lines":["a"]},{"start":{"row":7,"column":28},"end":{"row":7,"column":29},"action":"insert","lines":["t"]},{"start":{"row":7,"column":29},"end":{"row":7,"column":30},"action":"insert","lines":["e"]},{"start":{"row":7,"column":30},"end":{"row":7,"column":31},"action":"insert","lines":["s"]}],[{"start":{"row":7,"column":15},"end":{"row":7,"column":31},"action":"remove","lines":["render_templates"],"id":30},{"start":{"row":7,"column":15},"end":{"row":7,"column":31},"action":"insert","lines":["send_static_file"]}],[{"start":{"row":0,"column":0},"end":{"row":31,"column":0},"action":"remove","lines":["from flask import Flask, request, jsonify","app = Flask(__name__, static_folder='.', static_url_path='')","","data = []","","@app.route('/')","def index():","    return app.send_static_file('index.html')","","@app.route('/add', methods=['POST'])","def add():","    todo = request.form['todo']","    data.append({'todo': todo, 'checked': False})","    return jsonify(data)","","@app.route('/check/<int:index>', methods=['POST'])","def check(index):","    checked = request.json['checked']","    data[index]['checked'] = checked","    return jsonify(data)","","@app.route('/delete/<int:index>', methods=['POST'])","def delete(index):","    del data[index]","    return jsonify(data)","","@app.route('/todos', methods=['GET'])","def get_todos():","    return jsonify(data)","","app.run(port=8080, debug=True)",""],"id":31},{"start":{"row":0,"column":0},"end":{"row":33,"column":0},"action":"insert","lines":["from flask import Flask, request, jsonify","","app = Flask(__name__, static_folder='.', static_url_path='')","","data = []","","@app.route('/')","def index():","    return app.send_static_file('index.html')","","@app.route('/add', methods=['POST'])","def add():","    todo = request.form['todo']","    data.append({'todo': todo, 'checked': False})","    return jsonify(data)","","@app.route('/check/<int:index>', methods=['POST'])","def check(index):","    checked = request.json['checked']","    data[index]['checked'] = checked","    return jsonify(data)","","@app.route('/delete/<int:index>', methods=['POST'])","def delete(index):","    del data[index]","    return jsonify(data)","","@app.route('/todos', methods=['GET'])","def get_todos():","    return jsonify(data)","","if __name__ == '__main__':","    app.run(port=8080, debug=True)",""]}],[{"start":{"row":0,"column":0},"end":{"row":33,"column":0},"action":"remove","lines":["from flask import Flask, request, jsonify","","app = Flask(__name__, static_folder='.', static_url_path='')","","data = []","","@app.route('/')","def index():","    return app.send_static_file('index.html')","","@app.route('/add', methods=['POST'])","def add():","    todo = request.form['todo']","    data.append({'todo': todo, 'checked': False})","    return jsonify(data)","","@app.route('/check/<int:index>', methods=['POST'])","def check(index):","    checked = request.json['checked']","    data[index]['checked'] = checked","    return jsonify(data)","","@app.route('/delete/<int:index>', methods=['POST'])","def delete(index):","    del data[index]","    return jsonify(data)","","@app.route('/todos', methods=['GET'])","def get_todos():","    return jsonify(data)","","if __name__ == '__main__':","    app.run(port=8080, debug=True)",""],"id":32},{"start":{"row":0,"column":0},"end":{"row":33,"column":0},"action":"insert","lines":["from flask import Flask, request, render_template, jsonify","","app = Flask(__name__, static_folder='.', static_url_path='')","data = []","","","@app.route('/')","def index():","    return render_template('index.html', todos=data)","","","@app.route('/add', methods=['POST'])","def add():","    todo = request.form['todo']","    data.append({'todo': todo, 'checked': False})","    return jsonify(success=True)","","","@app.route('/check/<int:index>', methods=['POST'])","def check(index):","    checked = request.json['checked']","    data[index]['checked'] = checked","    return jsonify(success=True)","","","@app.route('/delete/<int:index>', methods=['POST'])","def delete(index):","    del data[index]","    return jsonify(success=True)","","","if __name__ == '__main__':","    app.run(port=8080, debug=True)",""]}],[{"start":{"row":11,"column":0},"end":{"row":16,"column":0},"action":"remove","lines":["@app.route('/add', methods=['POST'])","def add():","    todo = request.form['todo']","    data.append({'todo': todo, 'checked': False})","    return jsonify(success=True)",""],"id":33},{"start":{"row":11,"column":0},"end":{"row":15,"column":53},"action":"insert","lines":["@app.route('/add', methods=['POST'])","def add():","    todo = request.form.get('todo')","    todos.append({'todo': todo, 'checked': False})","    return render_template('index.html', todos=todos)"]}],[{"start":{"row":15,"column":47},"end":{"row":15,"column":52},"action":"remove","lines":["todos"],"id":34},{"start":{"row":15,"column":47},"end":{"row":15,"column":48},"action":"insert","lines":["d"]},{"start":{"row":15,"column":48},"end":{"row":15,"column":49},"action":"insert","lines":["a"]},{"start":{"row":15,"column":49},"end":{"row":15,"column":50},"action":"insert","lines":["t"]},{"start":{"row":15,"column":50},"end":{"row":15,"column":51},"action":"insert","lines":["a"]}],[{"start":{"row":14,"column":4},"end":{"row":14,"column":9},"action":"remove","lines":["todos"],"id":35},{"start":{"row":14,"column":4},"end":{"row":14,"column":5},"action":"insert","lines":["d"]},{"start":{"row":14,"column":5},"end":{"row":14,"column":6},"action":"insert","lines":["a"]},{"start":{"row":14,"column":6},"end":{"row":14,"column":7},"action":"insert","lines":["t"]},{"start":{"row":14,"column":7},"end":{"row":14,"column":8},"action":"insert","lines":["a"]}],[{"start":{"row":4,"column":0},"end":{"row":4,"column":12},"action":"insert","lines":["localStorage"],"id":36}],[{"start":{"row":4,"column":12},"end":{"row":4,"column":13},"action":"insert","lines":["　"],"id":37}],[{"start":{"row":4,"column":13},"end":{"row":4,"column":16},"action":"insert","lines":["=[]"],"id":38}],[{"start":{"row":4,"column":12},"end":{"row":4,"column":13},"action":"remove","lines":["　"],"id":39}],[{"start":{"row":4,"column":12},"end":{"row":4,"column":13},"action":"insert","lines":["　"],"id":40}],[{"start":{"row":4,"column":13},"end":{"row":4,"column":14},"action":"remove","lines":["="],"id":41},{"start":{"row":4,"column":12},"end":{"row":4,"column":13},"action":"remove","lines":["　"]}],[{"start":{"row":4,"column":12},"end":{"row":4,"column":13},"action":"insert","lines":[" "],"id":42},{"start":{"row":4,"column":13},"end":{"row":4,"column":14},"action":"insert","lines":["="]}],[{"start":{"row":4,"column":14},"end":{"row":4,"column":15},"action":"insert","lines":[" "],"id":43}],[{"start":{"row":4,"column":0},"end":{"row":4,"column":17},"action":"remove","lines":["localStorage = []"],"id":44},{"start":{"row":3,"column":9},"end":{"row":4,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":0,"column":0},"end":{"row":31,"column":0},"action":"remove","lines":["from flask import Flask, request, render_template, jsonify","","app = Flask(__name__, static_folder='.', static_url_path='')","data = []","","@app.route('/')","def index():","    return render_template('index.html', todos=data)","","","@app.route('/add', methods=['POST'])","def add():","    todo = request.form.get('todo')","    data.append({'todo': todo, 'checked': False})","    return render_template('index.html', todos=data)","","@app.route('/check/<int:index>', methods=['POST'])","def check(index):","    checked = request.json['checked']","    data[index]['checked'] = checked","    return jsonify(success=True)","","","@app.route('/delete/<int:index>', methods=['POST'])","def delete(index):","    del data[index]","    return jsonify(success=True)","","","if __name__ == '__main__':","    app.run(port=8080, debug=True)",""],"id":45},{"start":{"row":0,"column":0},"end":{"row":33,"column":0},"action":"insert","lines":["from flask import Flask, request, render_template, jsonify","","app = Flask(__name__, static_folder='.', static_url_path='')","data = []","","","@app.route('/')","def index():","    return render_template('index.html', todos=data)","","","@app.route('/add', methods=['POST'])","def add():","    todo = request.form.get('todo')","    data.append({'todo': todo, 'checked': False})","    return jsonify(success=True)","","","@app.route('/check/<int:index>', methods=['POST'])","def check(index):","    checked = request.json['checked']","    data[index]['checked'] = checked","    return jsonify(success=True)","","","@app.route('/delete/<int:index>', methods=['POST'])","def delete(index):","    del data[index]","    return jsonify(success=True)","","","if __name__ == '__main__':","    app.run(port=8080, debug=True)",""]}],[{"start":{"row":4,"column":0},"end":{"row":4,"column":19},"action":"insert","lines":["global localStorage"],"id":46}],[{"start":{"row":4,"column":0},"end":{"row":4,"column":19},"action":"remove","lines":["global localStorage"],"id":47}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":4,"column":0},"end":{"row":4,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1684475476926,"hash":"bf0f0b415a576be9578db0aeb3a68848a766d87e"}