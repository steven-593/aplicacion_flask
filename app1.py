from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('forms.html')

@app.route("/submit", methods=['POST'])
def submit():
    if request.method == 'POST':
        # Obtener los datos del formulario
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        dob = request.form.get('dob')
        gender = request.form.get('gender')
        email = request.form.get('email')
        address = request.form.get('address')
        university = request.form.get('university')
        phone = request.form.get('phone')

        # Mostrar los datos recibidos
        return f"""
            <h1>Datos Registrados</h1>
            <p>Nombre: {first_name}</p>
            <p>Apellido: {last_name}</p>
            <p>Fecha de Nacimiento: {dob}</p>
            <p>Género: {gender}</p>
            <p>Correo Electrónico: {email}</p>
            <p>Dirección: {address}</p>
            <p>Universidad: {university}</p>
            <p>Número de Teléfono: {phone}</p>
        """
    return "<p>Método no permitido</p>"

if __name__ == "__main__":
    app.run(debug=True)
