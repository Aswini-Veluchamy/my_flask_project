from flask import Blueprint, render_template, request

main_bp = Blueprint('main', __name__)

@main_bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Process form data here
        field1 = request.form['field1']
        field2 = request.form['field2']
        field3 = request.form['field3']
        field4 = request.form['field4']
        field5 = request.form['field5']
        field6 = request.form['field6']
        field7 = request.form['field7']
        field8 = request.form['field8']
        field9 = request.form['field9']
        field10 = request.form['field10']
        field11 = request.form['field11']
        field12 = request.form['field12']
        print(f"field1: {field1}, field2: {field2}, field3: {field3}",
              f"field4: {field4}, field5: {field5}, field6: {field6}",
              f"field7: {field7}, field8: {field8}, field9: {field9}",
              f"field10: {field10}, field11: {field11}, field12: {field12}")

    return render_template('index.html')
