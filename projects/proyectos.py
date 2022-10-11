from flask import Flask, render_template, request, url_for, flash, redirect

app = Flask(__name__)

# Menu Inicio
@app.route('/')
def index():
    return render_template('index.html')

#Pag relacionada al proyecto uno
@app.route('/project_one', methods=['GET', 'POST'])
def project_one():

    resultados = []
    conjunto1 = request.args.get('conjunto1')
    conjunto2 = request.args.get('conjunto2')
    
    if conjunto1 is not None or conjunto2 is not None:
        resultados.append(conjunto1)
        resultados.append(conjunto2)
            
    if request.method == 'POST':
        conjunto1 = request.form['conjunto1']
        conjunto2 = request.form['conjunto2']
                
        return redirect(url_for('project_one',conjunto1=conjunto1,conjunto2=conjunto2))
    
    return render_template('project_one.html',resultados=resultados)

#Pag relacionada al proyecto dos
@app.route('/project_two')
def project_two():
    return render_template('project_two.html')
