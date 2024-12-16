# print("Hello world !!")
from flask import Flask, render_template,jsonify

app = Flask(__name__)

JOBS=[
    {
    'id':1,
    'title':'Data Analyst',
    'location':'Bengaluru, India',
    'salary':'Rs. 10,00,000'
    },
    {
        'id':2,
        'title':'Data Scientist',
        'location':'Delhi, India',
        'salary':'Rs. 8,00,000'
    },
    {
        'id':3,
        'title':'Software Engineer',
        'location':'Gurugram, India',
        'salary':'Rs. 11,00,000'
    },
    {
        'id':4,
        'title':'Backend Developer',
        'location':'Bengaluru, India',
        'salary':'Rs. 7,00,000'
        },
    ]
# print(__name__)
@app.route("/")
def hello_world():
    # return "<p>Hello, World!</p>"
    return render_template("home.html",jobs=JOBS)

@app.route("/api/jobs")     #api is added so that we can differentiate in html or non html pages
def list_jobs():
    return jsonify(JOBS)
        
if __name__ == "__main__" :
  app.run(host='0.0.0.0' , debug=True)

  
