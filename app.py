from flask import Flask,request,render_template
app=flask(__name__)
@app.route('/')
def index():
    return render_template('register.html')
@app.route("/register.html",method=['POST'])
def register():
    name=form.request('name').value
    year=form.request('year').value
    return render_template('successful.html')
if __name__==__main__:
    run(host='0.0.0.0',port=5000,debug=True)