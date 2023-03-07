from flask import Flask, render_template

app = Flask(__name__)
#You are assigning the main app to name process here. If you print app or __name__, it will display as __main__.

@app.route('/')

def hello_world():
  return render_template('home.html')

#If instead of using the flask quickstart guide to run the program, you can also run code by equating the __name__ variable to the __main__ variable.
print(__name__)
if __name__ == '__main__':
  print('I am inside the if now.')
  #use 0.0.0.0 to run on the local server
  app.run(host='0.0.0.0', debug=True)