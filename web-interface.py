from flask import Flask, render_template, redirect, send_file

app = Flask(__name__)

med_headings = ['Name', 'Purpose', 'Brand', 'Price (₹)', 'Count', 'Prescription Needed']
bill_headings = ['Bill ID', 'Phone', 'Name', 'Medicines', 'Total', 'Payment Mode']

def get_med_details():
    meds = list()
    with open('med-hash.txt', 'r') as med_file:
        records = med_file.readlines()
        [meds.append(record.split('|')) for record in records]
    return meds

def get_bill_details():
    bills = list()
    with open('bill-hash.txt', 'r') as bill_file:
        records = bill_file.readlines()
        [bills.append(record.split('|')) for record in records]
    return bills

@app.route('/meds')
def meds():
    return render_template('index.html', title='Meds', med_status='active', headings=med_headings, data=get_med_details())

@app.route('/bills')
def bills():
    return render_template('index.html', title='Bills', bill_status='active', headings=bill_headings, data=get_bill_details())

@app.route('/css', methods=['GET'])
def bootstrap_css():
    filename = './assets/css/bootstrap.min.css'
    return send_file(filename)

@app.errorhandler(404)
def error_route(err):
    return redirect('/meds')

app.run('0.0.0.0', 3000)

