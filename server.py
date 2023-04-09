from flask import Flask, render_template, redirect, request, session


app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key= "Secret"


# The "@" decorator associates this route with the function immediately following
@app.route('/')          
def dojo_survey():
    return render_template('index.html')

@app.route('/process', methods=['post'])          
def process():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/result')

@app.route('/result')          
def result():
    return render_template('result.html')


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
