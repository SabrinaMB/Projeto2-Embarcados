from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

todos = {}

dispositivos = {}

class recebe(Resource):
	def get(self):
		global agua, cafe, digital, sdigital
		data = "D: 0"
		if (request.args.get("Agua")):
			agua = request.args.get("Agua")
			agua = int(agua)
		
		else:
			agua = 0

		if (request.args.get("Cafe")):
			cafe = request.args.get("Cafe")
			cafe = int(cafe)
		
		else:
			cafe = 0
		if (request.args.get("Digital")):
			digital = request.args.get("Digital")
			digital = int(digital)
		else:
			digital = 0

		if digital == 0:
			sdigital = "Botão não foi pressionado"
		else:
			sdigital = "Botão foi pressionado"
		
		# print(request.data)
		# print(request.time)
		# r='REceieve'
		# clientsocket.send(r.encode())
		if digital == 1: # tem cafe e agua:
			data = "D: 1"
		return data

	def post(self):
		return 1


api.add_resource(recebe, '/')
global ButtonPressed
ButtonPressed = 0;      



class cafe(Resource):
	def get(self):
		return "get"

	def post(self):
		return "post"


api.add_resource(cafe, '/cafe')

@app.route('/show')

def show():

   return '''
   	<html>
   		<body>
			<div class="container">
    			<form method="post" action="/cafe"> 
        			<input type="submit" value="Faz Café" >
    			</form>
 			</div>
         	<h1> Agua: {0} <h1>
   			<h1> Cafe: {1} <h1>
   			<h1>  {2} <h1>
    	</body>
	</html>
  
	
   '''.format(agua, cafe, sdigital)







# class show(Resource):
# 	def get(self):
# 		# return '''
# 		#    	<html>
# 		#    		<body>
# 		# 			<div class="container">
# 		#     			<form method="post"> 
# 		#         			<input type="submit" value="Faz Café" >
# 		#     			</form>
# 		#  			</div>
# 		#          	<h1> Agua: {0} <h1>
# 		#    			<h1> Cafe: {1} <h1>
# 		#    			<h1>  {2} <h1>
# 		#     	</body>
# 		# 	</html>
		  
			
# 		#    '''.format(agua, cafe, sdigital)
# 		return "<h1>oi<h1>"
# 	def post(self):
# 		return 1


# api.add_resource(show, '/show')
# @app.route('/python')

# def hello_python():
#    return 'Hello Python'
if __name__ == '__main__':
	app.run(host='0.0.0.0',debug=True)
	#app.run(debug=True)

