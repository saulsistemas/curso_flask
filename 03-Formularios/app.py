from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('base.html')

@app.route('/auth/register/', methods=['GET','POST'])
def registrar():
    
    if request.method == 'POST':
        print(request.form)
        username = request.form['username']
        password = request.form['password']
        return f'Nombre de usuario {username} y la contraseña {password}'
    
    return render_template('auth/register.html')
    
if __name__ == '__main__':
    app.run(debug=True)