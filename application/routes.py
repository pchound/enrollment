from application import app
from flask import render_template, request, json, Response

courseData = [
    {"courseID": "1111", "title": "PHP 101", "description": "Intro to PHP", "credits": 3, "term": "Fall, Spring"},
    {"courseID": "2222", "title": "Java 1", "description": "Intro to Java Programming", "credits": 4, "term": "Spring"},
    {"courseID": "3333", "title": "Adv PHP 201", "description": "Advanced PHP Programming", "credits": 3, "term": "Fall"},
    {"courseID": "4444", "title": "Angular 1", "description": "Intro to Angular", "credits": 3, "term": "Fall, Spring"},
    {"courseID": "5555", "title": "Java 2", "description": "Advanced Java Programming", "credits": 4, "term": "Fall"}
]

print(courseData[0]["title"])

@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html", index=True)

@app.route("/login")
def login():
    return render_template("login.html", login=True)

@app.route("/courses/")
@app.route("/courses/<term>")
def courses(term="Spring 2019"):
    return render_template("courses.html", courseData=courseData, courses=True, term=term)

@app.route("/register")
def register():
    return render_template("register.html", register=True)

@app.route("/enrollment", methods=["GET", "POST"])
def enrollment():
    id = request.form.get('courseID')
    title = request.form.get('title')
    term = request.form.get('term')
    return render_template("enrollment.html", enrollment=True, data={"id": id, "title": title, "term": term})

@app.route("/api/")
@app.route("/api/<idx>")
def api(idx=None):
    if idx is None:
        jdata = courseData
    else:
        jdata = courseData[int(idx)]
    return app.response_class(
        response=json.dumps(jdata),
        status=200,
        mimetype="application/json"
    )

class User(db.Document):
    user_id     =       db.IntField(unique=True)
    first_name  =       db.StringField(max_length=50)
    last_name   =       db.StringField(max_length=50)
    email       =       db.StringField(max_length=30)
    password    =       db.StringField(max_length=30)

@app.route("/user")
def user():
    User(user_id=1, first_name="Joseph", last_name="Garner" email="joedude1994@gmail.com", passwords="abc1234")
    User(user_id=1, first_name="PC", last_name="Hound" email="chaonerdguy@gmail.com", passwords="yourface")
    
    users = User.objects.all()
    return render_template("user.html", users=users)