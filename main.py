from flask import Flask, request, jsonify


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello %s!' % name

def create_function(message):
    def inner_function():
        return message
    return inner_function

b2g = create_function("Ich kann Funktionen als Objekte behandeln und diese in Variablen speichern und weitergeben.")
b2f = create_function("Ich kann Funktionen als Argumente für andere Funktionen verwenden und dadurch höherwertige Funktionen erstellen.")
b2e = create_function("Ich kann Funktionen als Objekte und Argumente verwenden, um komplexe Aufgaben (Anwenden von Closures).")

# Routen, die die Funktionen auswerten
@app.route('/b2g')
def b2g_endpoint():
    return jsonify({'message': b2g()})

@app.route('/b2f')
def b2f_endpoint():
    return jsonify({'message': b2f()})

@app.route('/b2e')
def b2e_endpoint():
    return jsonify({'message': b2e()})

b3g = lambda x: x ** 2  # Square of a number
b3f = lambda x, y: x.upper() if y else x.lower()  # Convert to uppercase or lowercase
b3e = lambda lst, key: sorted(lst, key=lambda item: item[key])  # Sorting a list based on custom criteria

# Routes for B3G, B3F, and B3E
@app.route('/b3g/<int:num>')
def b3g_endpoint(num):
    result = b3g(num)
    return jsonify({'message': f'Lambda expression: Squaring {num} results in {result}'})

@app.route('/b3f/<string:text>/<int:uppercase>')
def b3f_endpoint(text, uppercase):
    result = b3f(text, bool(uppercase))
    action = 'in uppercase' if uppercase else 'in lowercase'
    return jsonify({'message': f'Lambda expression: Convert "{text}" to {action}: {result}'})

@app.route('/b3e/<string:items>/<string:key>')
def b3e_endpoint(items, key):
    items_list = items.split(',')
    result = b3e(items_list, key)
    return jsonify({'message': f'Lambda expression: Sort list {items_list} by key "{key}": {result}'})


if __name__ == '__main__':
    app.run()