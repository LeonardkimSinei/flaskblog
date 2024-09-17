from flask import Flask,render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY']='8c1739763c20a39e035a7c30fd00575d'

posts=[
  {'title':'First Blog',
   'content':'First Blog',
   'date_posted':'12/09/2024',
   'author':'Leo Kim'
   },
  
  
  {'title':'Second Blog',
   'content':'Second Blog content',
   'date_posted':'12/09/2024',
   'author':'Mum Cheru'},



  {'title':'Second Blog',
   'content':'Second Blog content',
   'date_posted':'12/09/2024',
   'author':'Mum Cheru'}]

@app.route("/")
@app.route("/home")
def home():
   return render_template('home.html',title= 'home page', posts=posts)

@app.route("/about")
def about():
   return render_template('about.html',title= 'about page')

@app.route("/register", methods=['GET','POST'])
def register():
   form = RegistrationForm()
   return render_template('register.html',title= 'register page', form=RegistrationForm)


@app.route("/login")
def login():
   form = LoginForm()
   return render_template('login.html',title= 'Login page', form =form)




if (__name__) == "__main__":
   app.run
