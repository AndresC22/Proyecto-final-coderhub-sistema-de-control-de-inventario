from flask import Flask, render_template, request, redirect, url_for, jsonify, session, flash
from controller.controllerEquipo import *
import os
from werkzeug.utils import secure_filename 

# Se declara el nombre del programa para iniciar
app = Flask(__name__)
application = app

app.secret_key = "esta_es_clave_secreta_super_segura" 

# ruta de registro de usuario
@app.route('/register', methods=['GET', 'POST'])
def register():
    if 'id_usuario' in session:
        return redirect(url_for('inicio'))

    if request.method == 'POST':
        # Se usa .get() y .strip() para evitar errores y limpiar espacios en blanco
        nombre = request.form.get('nombre', '').strip()
        clave = request.form.get('clave', '').strip()
        
        # Se validad que se completen todos los campos para ser registrado
        if not nombre or not clave:
            flash('Por favor, llena todos los campos para registrarte.')
            return render_template('loginregistro/register.html')
        
        # Se validad que la contraseña no sea menor de 5 caracteres
        if len(clave) < 5:
            flash('La clave no puede tener menos de 5 caracteres.')
            return render_template('loginregistro/register.html')
        
        resultado = registrarUsuario(nombre, clave)
        
        # Se evita que existan dos usuarios con el mismo nombre
        if resultado == "existe":
            flash('El nombre de usuario ya está en uso. Pruebe con otro nombre.')
        elif resultado == 1:
            flash('Registro exitoso. Ahora puedes iniciar sesión.')
            return redirect(url_for('login'))
        else:
            flash('Ocurrió un error al registrar el usuario.')

    return render_template('loginregistro/register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'id_usuario' in session:
        return redirect(url_for('inicio'))

    if request.method == 'POST':
        nombre = request.form.get('nombre', '').strip()
        clave = request.form.get('clave', '').strip()
        
        # Se validad que se completen todos los campos para iniciar sesion
        if not nombre or not clave:
            flash('Por favor, ingresa tu usuario y clave.')
            return render_template('loginregistro/login.html')
        
        usuario_bd = verificarUsuario(nombre, clave)
        # Se valida que el usuario y la clave exita dentro de la base datos
        if usuario_bd:
            session['id_usuario'] = usuario_bd['id']
            session['nombre_usuario'] = usuario_bd['nombre']
            return redirect(url_for('inicio'))
        else:
            flash('Usuario o clave incorrectos.')

    return render_template('loginregistro/login.html')

# ruta de cerrar sesion del usuario
@app.route('/logout')
def logout():
    session.clear() 
    flash('Se ha cerrado la sesión correctamente.')
    return redirect(url_for('login'))

# ruta al ingresar al main
@app.route('/', methods=['GET','POST'])
def inicio():
    # sera dirigido al login en caso exista una sesion de algun usuario
    if 'id_usuario' not in session:
        return redirect(url_for('login'))

    mensaje = session.pop('msg', '')
    tipo_msg = session.pop('tipo', '')
    
    # Se obtiene el id de la sesion del usuario
    id_usuario_actual = session.get('id_usuario')
    
    # Se envia el id del usuario a la funcion para que aparezca solamente los registro realizados por el
    equipos_del_usuario = listaEquipos(id_usuario_actual)
    
    return render_template('inicio/main.html', miData=equipos_del_usuario, msg=mensaje, tipo=tipo_msg)

#ruta de registro de equipo
@app.route('/registrar-equipo', methods=['GET','POST'])
def addEquipo():
    if 'id_usuario' not in session: return redirect(url_for('login'))
    return render_template('acciones/add.html')


@app.route('/equipo', methods=['POST'])
def formAddEquipo():
    if 'id_usuario' not in session: return redirect(url_for('login'))

    if request.method == 'POST':
        marca               = request.form['marca']
        modelo              = request.form['modelo']
        clase               = request.form['clase']
        area                = request.form['area']
        observacion         = request.form['observacion']
        revisado            = request.form['revisado']
        
        id_usuario = session.get('id_usuario')
        
        if(request.files['foto'] !=''):
            file     = request.files['foto'] 
            nuevoNombreFile = recibeFoto(file) 
            
            resultData = registrarEquipo(id_usuario, marca, modelo, clase, area, observacion, revisado, nuevoNombreFile)
            
            if(resultData == 1):
                session['msg'] = 'El Registro fue un éxito'
                session['tipo'] = 1
                return redirect(url_for('inicio'))
            else:
                session['msg'] = 'Error al registrar'
                session['tipo'] = 1
                return redirect(url_for('inicio'))
            
# ruta actualizar registro
@app.route('/form-update-equipo/<string:id>', methods=['GET','POST'])
def formViewUpdate(id):
    if 'id_usuario' not in session: return redirect(url_for('login'))
    
    if request.method == 'GET':
        resultData = updateEquipo(id)
        if resultData:
            return render_template('acciones/update.html',  dataInfo = resultData)
        else:
            return redirect(url_for('inicio'))
    else:
        return redirect(url_for('inicio'))     
         
# ruta de visualizacion del equipo y su informacion
@app.route('/ver-detalles-del-equipo/<int:idEquipo>', methods=['GET', 'POST'])
def viewDetalleEquipo(idEquipo):
    if 'id_usuario' not in session: return redirect(url_for('login'))
    
    if request.method == 'GET':
        resultData = detallesdelEquipo(idEquipo)
        if resultData:
            return render_template('acciones/view.html', infoEquipo = resultData, msg='Detalles del Equipo', tipo=1)
        else:
            return render_template('inicio/main.html', msg='No existe el Equipo', tipo=1)
    return redirect(url_for('inicio'))
    
@app.route('/actualizar-equipo/<string:idEquipo>', methods=['POST'])
def formActualizarEquipo(idEquipo):
    if 'id_usuario' not in session: return redirect(url_for('login'))
    
    if request.method == 'POST':
        marca           = request.form['marca']
        modelo          = request.form['modelo']
        clase           = request.form['clase']
        area            = request.form['area']
        observacion     = request.form['observacion']
        revisado        = request.form['revisado']
        
        foto_equipo = None
        if 'foto' in request.files and request.files['foto'].filename != '':
            file = request.files['foto']
            foto_equipo = recibeFoto(file)

        resultData = recibeActualizarEquipo(
            marca, modelo, clase, area, observacion, revisado, foto_equipo, idEquipo
        )
        
        if(resultData == 1):
            session['msg'] = 'Datos del equipo actualizados'
            session['tipo'] = 1
        else:
            session['msg'] = 'No se pudo actualizar'
            session['tipo'] = 1
        return redirect(url_for('inicio'))

# ruta para eliminar equipo
@app.route('/borrar-equipo', methods=['GET', 'POST'])
def formViewBorrarEquipo():
    if 'id_usuario' not in session: return jsonify([0]) 
    
    if request.method == 'POST':
        idEquipo         = request.form['id']
        nombreFoto      = request.form['nombreFoto']
        resultData      = eliminarEquipo(idEquipo, nombreFoto)

        if resultData == 1:
            return jsonify([1])
        else: 
            return jsonify([0])


def eliminarEquipo(idEquipo='', nombreFoto=''):
    conexion = connectionBD() 
    cur = conexion.cursor() 
    
    cur.execute('DELETE FROM equipos WHERE id=?', (idEquipo,))
    conexion.commit()
    resultado_eliminar = cur.rowcount 
    
    cur.close()
    conexion.close()
    # Se elimina la foto almacenada en la carpeta al borrar el registro
    if nombreFoto:
        basepath = os.path.dirname(__file__) 
        url_File = os.path.join(basepath, 'static/assets/fotos_equipos', nombreFoto)
        # se verifica que exista la foto en la carpeta y borrarlo
        if os.path.exists(url_File):
            os.remove(url_File) 

    return resultado_eliminar

#se agrega una copia de la foto en la carpeta para almacenarla
def recibeFoto(file):
    basepath = os.path.dirname (__file__)
    filename = secure_filename(file.filename) #Se captura la extencion que pertenece la foto
    extension           = os.path.splitext(filename)[1]
    nuevoNombreFile     = stringAleatorio() + extension
        
    upload_path = os.path.join (basepath, 'static/assets/fotos_equipos', nuevoNombreFile) 
    file.save(upload_path)

    return nuevoNombreFile

# Redireccionando cuando la página no existe
@app.errorhandler(404)
def not_found(error):
    return redirect(url_for('inicio'))
    
    
if __name__ == "__main__":
    app.run(debug=True)