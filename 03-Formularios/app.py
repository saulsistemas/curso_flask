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
        if len(username) >= 4  and len(username)<=25 and len(password)>=2 and len(password)<=40:
            #return f'Nombre de usuario {username} y la contraseña {password}'
            success =f""" 
                Usuario y contraseña 
                usuario {username}
                password {password}
            """
            return render_template('auth/register.html',successHtml = success)
        else:
            error =""" 
                Nombre de usuario debe tener entre 4 y 25 caracteres y la 
                contraseña debe tener entre 2 a 40 caracteres.            
            """
            return render_template('auth/register.html',errorHtml = error)
            
        
    return render_template('auth/register.html')
    
if __name__ == '__main__':
    app.run(debug=True)