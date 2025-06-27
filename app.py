from flask import Flask, render_template, request, redirect, url_for, flash
from forms.post_form import Signup, Login
app=Flask(__name__)
@app.route('/')
def home():
    return render_template('base.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = Signup()
    if request.method=='Post':
        if form.validate():
            flash('Signup is Successful')
            return redirect('templates/login.html')
    return render_template('signup.html', form=form)
if __name__ == "__main__":
    app.run(debug=True)