from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/misDatos', methods=['GET'])
def misDatos():

	if request.method == 'GET':

		return {

			'carnet' : "201700365",
			'nombre': "Saúl Enrique Pérez Pérez"
		}


@app.route("/")
def index():

	return "<h1>CORTO 3 -IPC1</h1>"		

if __name__ == "__main__":
	app.run(threaded=True, port=5000,debug=True)			
		