from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = {}  # Dictionary to store tasks

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    task_name = request.form['task_name']
    task_description = request.form['task_description']
    task_priority = request.form['task_priority']
    
    tasks[task_name] = {
        'description': task_description,
        'priority': task_priority,
        'status': 'not_started',  # Default status
        'progress': 0  # Default progress
    }
    return redirect(url_for('index'))

@app.route('/update_task/<task_name>', methods=['POST'])
def update_task(task_name):
    if task_name in tasks:
        task_status = request.form['task_status']
        task_progress = request.form['task_progress']
        
        tasks[task_name]['status'] = task_status
        tasks[task_name]['progress'] = task_progress
    return redirect(url_for('index'))

@app.route('/delete_task/<task_name>', methods=['POST'])
def delete_task(task_name):
    if task_name in tasks:
        del tasks[task_name]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
