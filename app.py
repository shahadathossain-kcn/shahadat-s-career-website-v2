from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS=[
{
    'id' : 1,
    'title' : 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 10,00,000',
    
}, 
{
        'id' : 2,
        'title' : 'Sowftware Engineer',
        'location': 'Delhi, India',
        'salary': 'Rs. 15,00,000',

},
{
    'id' : 3,
    'title' : 'Backend Developer',
    'location': 'Kolkata, India',
    'salary': 'Rs. 25,00,000',

},
{
    'id' : 4,
    'title' : 'Frontend Developer',
    'location': 'Florida, USA',
    'salary': '$120,000',

}
    
    ]
@app.route("/")
def hello_world():
    return render_template('home.html', jobs=JOBS, company_name='Onko Da')

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
