import flask
import requests
from flask import request, jsonify
from flask_cors import CORS
import database


app = flask.Flask(__name__)
CORS(app)
app.config["DEBUG"] = True

@app.route('/hello/<name>', methods=['GET'])
def hello(name):
	return jsonify({'message': 'Hello '+name, 'success': True})

@app.route('/hello/<name>/<times>', methods=['GET'])
def hello_times(name, times):
	return jsonify([name] * int(times))

@app.route('/caracola', methods=['GET'])
def caracola():
	return jsonify('Hola')

@app.route('/users',methods=['GET'])
def muestraUsuarios():
	arg = "SELECT * FROM employee"
	resul = database.function(arg)
	lista=[]
	for row in resul:
		lista.append({'id': int(row[0]),'name':row[1],'surname':row[2],'salary':row[3],'bday':row[4],'dni':row[5],'role':'employee'})
	arg = "SELECT * FROM client"
	resul1 = database.function(arg)
	for row in resul1:
		lista.append({'name': row[0],'id':int(row[1]),'employee_id':int(row[2]),'role':'client'})
	return jsonify(lista)

@app.route('/users/<id>',methods=['GET'])
def muestraUsuarioPorID(id):
	arg = ("SELECT * FROM employee WHERE id=" + id)
	resul = database.function(arg)
	lista = []
	for row in resul:
		lista.append({'id': int(row[0]),'name':row[1],'surname':row[2],'salary':row[3],'bday':row[4],'dni':row[5]})
	return jsonify(lista)

@app.route('/users',methods=['POST'])
def muestraUsuariosSeguro():
	name = request.form['first_name']
	surname = request.form['last_name']
	salary = request.form['salary']
	birthday = request.form['birthday']
	identification_number = request.form['identification_number']
	arg = ("INSERT INTO employee (first_name,last_name,salary,birthday,dni) VALUES ('" + name + "','" + surname + "','" + salary + "','" + birthday + "','" + identification_number + "')")
	database.function2(arg)
	return jsonify('done')

@app.route('/users',methods=['DELETE'])
def removeuser():
	id = request.form['id']
	arg = ("DELETE FROM employee WHERE id='" + id + "'")
	database.function2(arg)
	return jsonify('done')

@app.route('/users/<id>/<pay>',methods=['PATCH'])
def cambiarSalario(id,pay):
	arg = ("UPDATE employee SET salary='"+pay+"' WHERE id='"+id+"'")
	database.function2(arg)
	return jsonify('done')

@app.route('/ceu/<id>/<employee>',methods=['PATCH'])
def cambiarEmpleado(id,employee):
	arg = ("UPDATE client SET employee='"+employee+"' WHERE id='"+id+"'")
	database.function2(arg)
	return jsonify('done')

@app.route('/ic/<name>/<employee>/<apellido>/<dni>/<nacimiento>',methods=['PATCH'])
def insertarCliente(name,employee,apellido,dni,nacimiento):
	arg = ("INSERT INTO client (name, employee, surname, dni, birthday) VALUES ('"+name+"','" + employee + "','" + apellido + "','" + dni +"','" + nacimiento + "')")
	database.function2(arg)
	return jsonify('done')

@app.route('/ie/<name1>/<name2>/<pay>/<bd>/<dni>',methods=['PATCH'])
def insertarEmpleado(name1,name2,pay,bd,dni):
	arg = ("INSERT INTO employee (first_name,last_name,salario,birthday,dni) VALUES ('"+name1+"','" + name2 + "','" + pay + "','" + bd + "','" + dni + "')")
	database.function2(arg)
	return jsonify('done')

@app.route('/dc/<id>',methods=['PATCH'])
def borrarCliente(id):
	arg = ("DELETE FROM client WHERE id='"+id+"'")
	database.function2(arg)
	return jsonify('done')

@app.route('/de/<id>',methods=['PATCH'])
def borrarEmpleado(id):
	arg = ("DELETE FROM employee WHERE id='"+id+"'")
	database.function2(arg)
	return jsonify('done')



app.run()