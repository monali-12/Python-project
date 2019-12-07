from flask import Flask, jsonify, request #import objects from the Flask model
app = Flask(__name__) #define app using Flask

languages = [{'id': 1,'firstname' : 'pranali','lastname':'khade','contactno':8669736581,'emailid':'khadepranali24@gmail.com'}, {'id': 2,'firstname' : 'mona','lastname':'bade','contactno':9960737762,'emailid':'bademonali11@gmail.com'}, {'id': 3,'firstname' : 'pooja','lastname':'shelake','contactno':7865467899,'emailid':'poojashelake1557@gmail.com'}]


@app.route('/', methods=['GET'])
def test():
	return jsonify({'message' : 'It works!'})


@app.route('/lang', methods=['GET'])
def returnAll():
	return jsonify({'languages' : languages})


@app.route('/lang/<string:id>', methods=['GET'])
def returnOne(id):
	langs = [language for language in languages if language['id'] == int(id)]
	return jsonify({'language' : langs[0]})


@app.route('/lang', methods=['POST'])
def addOne():
	print(request.json)
	language = {'id': request.json['id'],  'firstname' : request.json['firstname'],'lastname' : request.json['lastname'],'contactno' : request.json['contactno']}

	languages.append(language)
	return jsonify({'msg': ' new contact has been added.!'})


@app.route('/lang/<string:id>', methods=['PUT'])
def editOne(id):
	langs = [language for language in languages if language['id'] == int(id)]
	langs[0]['firstname'] = request.json['firstname']
	langs[0]['lastname']=request.json['lastname']
	langs[0]['contactno']=request.json['contactno']
	return jsonify({'language' : langs[0]})





@app.route('/lang/<string:id>', methods=['DELETE'])
def removeOne(id):
	lang = [language for language in languages if language['id'] == int(id)]
	languages.remove(lang[0])
	return jsonify({'languages' : languages})

if __name__ == '__main__':
	app.run(debug=True, port=6060) #run app on port 8080 in debug mode
