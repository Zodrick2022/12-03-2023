from flask import Flask, render_template

app = Flask(__name__)

#creamos ruta principal(pagina prioncipal)
@app.route('/')
def home(): #retornar texto
    return render_template('home.html') #con render_template podemos retornar una pagina html
#creomos ruta about
@app.route('/about')
def about(): #retornar texto
    return render_template('about.html') #con render_template podemos retornar una pagina html
#comprobamos si estamos en el archivo principal
if __name__ == '__main__': 
    app.run(debug=True) #cada vez que se haga un cambio en el codigo se reinicia el servidor