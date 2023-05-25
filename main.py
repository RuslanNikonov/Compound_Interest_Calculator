from flask import Flask, render_template, request

#Создание сайта
app = Flask(__name__)

#Создание главнойй страницы
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['post', 'get'])
def form():
    if request.method == 'POST':
        Vsy_summa = (int)(request.form.get('name1'))
        cent = (int)(request.form.get('name2'))
        Vremy = (int)(request.form.get('name3'))
        itog = Vsy_summa * (pow((1 + cent/100), Vremy))

        return render_template('index.html',a = itog)


if __name__ == '__main__':
    app.run(debug=True)
