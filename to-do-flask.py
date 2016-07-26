from flask import Flask, render_template, redirect, request

import pg

db = pg.DB(dbname='todo_db')

app = Flask('ToDoApp')

@app.route('/')
def form():
    query  = db.query('''
        select * from task
    ''')
    tasks = query.namedresult();
    # html = '<ul>'
    # for task in query.namedresult():
    #     html+= '<li>%s' %(task.task_description)
    # html +='</ul>'
    return render_template('edit_tasks.html', tasks = tasks)
    # return html

@app.route('/append_task', methods=['POST'])
def append_task():
    task_name = request.form['add_task']
    db.insert('task', task_description=task_name, completed=False)
    return redirect('/')

def complete_task(checked_keys):
    for checked_key in checked_keys:
        if checked_key == "complete":
            continue
        db.update('task', {'id': checked_key, 'completed': True})

def delete_task(checked_keys):
    for checked_key in checked_keys:
        if checked_key == "delete":
            continue
        db.delete('task', {'id': checked_key})

@app.route('/submit_form', methods=['POST'])
def submit_form():
    checked_keys = request.form.keys()
    if "complete" in checked_keys:
        complete_task(checked_keys)
    elif "delete" in checked_keys:
        delete_task(checked_keys)




    # if checked_keys :
    #     db.update('task', completed=True)




    # task_completed = request.form['completed']
    # print task_completed
    print checked_keys
    return redirect('/')



if __name__ == '__main__':
    app.debug = True
    app.run(debug=True)
