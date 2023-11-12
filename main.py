from flask import Flask, request, jsonify
from functools import reduce

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

# Function to encode text in UTF-8
def utf8_encode(text):
    return text.encode('utf-8').decode('utf-8')

@app.route('/a1g', methods=['GET'])
def describe_function_properties():
    function_properties = "Funktionen koennen verschiedene Eigenschaften haben, wie z.B. die Eigenschaft der reinen Funktion (pure function), " \
                         "die keine Seiteneffekte hat. Im Gegensatz dazu stehen andere Programmier-Strukturen wie Prozeduren."

    explanation = "Ich kann die Eigenschaften von Funktionen beschreiben, wie zum Beispiel pure Funktionen, und den Unterschied " \
                  "zu anderen Programmier-Strukturen wie Prozeduren erlaeutern. Beispiel: {}".format(utf8_encode(function_properties))

    return jsonify({'Kompetenz': 'A1G', 'Erfuellt': True, 'Beschreibung': utf8_encode(explanation)})

@app.route('/a1f', methods=['GET'])
def explain_immutable_values():
    immutable_values = "Immutable values sind unveraenderliche Werte, die nach ihrer Erstellung nicht mehr geaendert werden koennen. " \
                       "Ein Beispiel dafuer ist eine Zeichenkette (String) in Python."

    explanation = "Ich kann das Konzept von immutable values erlaeutern und Beispiele anwenden. Somit kann ich dieses Konzept " \
                  "funktionaler Programmierung im Unterschied zu anderen Programmiersprachen erklaeren, zum Beispiel im Vergleich " \
                  "zu referenzierten Objekten. Beispiel: {}".format(utf8_encode(immutable_values))

    return jsonify({'Kompetenz': 'A1F', 'Erfuellt': True, 'Beschreibung': utf8_encode(explanation)})

@app.route('/a1e', methods=['GET'])
def compare_programming_paradigms():
    problem_solution = "In den verschiedenen Konzepten (Objektorientierte Programmierung, Prozedurale Programmierung und " \
                       "Funktionale Programmierung) werden Probleme auf unterschiedliche Weise geloest. Zum Beispiel koennen " \
                       "Daten in der objektorientierten Programmierung durch Klassen und Objekte strukturiert werden, waehrend in " \
                       "der funktionalen Programmierung Funktionen im Vordergrund stehen."

    explanation = "Ich kann aufzeigen, wie Probleme in den verschiedenen Konzepten (Objektorientierte Programmierung, Prozedurale " \
                  "Programmierung und Funktionale Programmierung) geloest werden und diese miteinander vergleichen. Beispiel: {}".format(utf8_encode(problem_solution))

    return jsonify({'Kompetenz': 'A1E', 'Erfuellt': True, 'Beschreibung': utf8_encode(explanation)})


@app.route('/b1g', methods=['GET'])
def explain_algorithm():
    explanation = "Ein Algorithmus ist eine präzise, schrittweise Anleitung zur Lösung eines Problems. " \
                  "Hier ist eine Erklärung eines Algorithmus, der die Bubble-Sort-Methode verwendet."

    algorithm_example = """
    1. Starte am Anfang der Liste.
    2. Vergleiche jedes Paar aufeinanderfolgender Elemente.
    3. Wenn ein Element größer ist als das nächste, tausche sie.
    4. Fahre fort, die Liste zu durchlaufen, bis keine Tausche mehr erforderlich sind.
    5. Die Liste ist jetzt sortiert.
    """

    return jsonify({'Kompetenz': 'B1G', 'Erfüllt': True, 'Erklärung': explanation, 'Beispiel': algorithm_example})


@app.route('/b1f', methods=['GET'])
def decompose_algorithm():
    def compare_and_swap(elements):
        for i in range(len(elements) - 1):
            if elements[i] > elements[i + 1]:
                elements[i], elements[i + 1] = elements[i + 1], elements[i]
        return elements

    explanation = "Ich kann Algorithmen in funktionale Teilstücke aufteilen. Hier ist eine aufgeteilte " \
                  "Funktion für den Bubble-Sort-Algorithmus."

    return jsonify({'Kompetenz': 'B1F', 'Erfüllt': True, 'Erklärung': explanation,
                    'Funktionsbeispiel': compare_and_swap.__code__.co_code})


@app.route('/b1e', methods=['GET'])
def implement_functions():
    def bubble_sort(elements):
        for _ in range(len(elements)):
            elements = compare_and_swap(elements)
        return elements

    def compare_and_swap(elements):
        for i in range(len(elements) - 1):
            if elements[i] > elements[i + 1]:
                elements[i], elements[i + 1] = elements[i + 1], elements[i]
        return elements

    example_list = [4, 2, 7, 1, 9]
    sorted_list = bubble_sort(example_list)

    explanation = "Ich kann Funktionen in zusammenhängende Algorithmen integrieren. Hier ist ein " \
                  "Beispiel für die Anwendung des Bubble-Sort-Algorithmus auf eine Liste."

    return jsonify({'Kompetenz': 'B1E', 'Erfüllt': True, 'Erklärung': explanation, 'Sortiertes Beispiel': sorted_list})


@app.route('/b2g', methods=['GET'])
def functions_as_objects():
    def multiply(x, y):
        return x * y

    my_function = multiply
    result = my_function(5, 3)

    explanation = "Ich kann Funktionen als Objekte behandeln, in Variablen speichern und weitergeben. " \
                  "Zum Beispiel, ich habe eine Funktion erstellt, die zwei Zahlen multipliziert und " \
                  "diese Funktion in einer Variablen 'my_function' gespeichert. Dann habe ich diese " \
                  "Funktion aufgerufen und das Ergebnis erhalten: {}".format(result)

    return jsonify({'Kompetenz': 'B2G', 'Erfuellt': True, 'Beschreibung': explanation})


@app.route('/b2f', methods=['GET'])
def functions_as_arguments():
    def add(x, y):
        return x + y

    def apply_operation(operation, x, y):
        return operation(x, y)

    result = apply_operation(add, 5, 3)

    explanation = "Ich kann Funktionen als Argumente fuer andere Funktionen verwenden, um " \
                  "hoeherwertige Funktionen zu erstellen. Zum Beispiel, ich habe eine 'add'-Funktion " \
                  "erstellt und eine 'apply_operation'-Funktion, die eine Operation auf zwei Zahlen " \
                  "anwendet. Ich habe die 'add'-Funktion als Argument an 'apply_operation' uebergeben " \
                  "und das Ergebnis erhalten: {}".format(result)

    return jsonify({'Kompetenz': 'B2F', 'Erfuellt': True, 'Beschreibung': explanation})


@app.route('/b2e', methods=['GET'])
def functions_as_closures():
    def outer_function(x):
        def inner_function(y):
            return x * y

        return inner_function

    closure = outer_function(5)
    result = closure(3)

    explanation = "Ich kann Funktionen als Objekte und Argumente verwenden, um komplexe Aufgaben zu loesen, " \
                  "einschließlich der Anwendung von Closures. Ich habe eine aeußere Funktion erstellt, " \
                  "die eine innere Funktion zurueckgibt. Diese innere Funktion ist eine Closure, die " \
                  "die Variable 'x' aus der aeußeren Funktion beibehaelt. Ich habe die Closure aufgerufen " \
                  "und das Ergebnis erhalten: {}".format(result)

    return jsonify({'Kompetenz': 'B2E', 'Erfuellt': True, 'Beschreibung': explanation})


b3g = lambda x: x ** 2  # Square of a number
b3f = lambda x, y: x.upper() if y else x.lower()  # Convert to uppercase or lowercase
b3e = lambda lst, key: sorted(lst, key=lambda item: item[key])  # Sorting a list based on custom criteria

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

@app.route('/b4g', methods=['GET'])
def apply_map_filter_reduce_individual():
    numbers = [1, 2, 3, 4, 5]

    # Map: Quadriere alle Zahlen in der Liste
    mapped_numbers = list(map(lambda x: x ** 2, numbers))

    # Filter: Filtere gerade Zahlen aus der Liste
    filtered_numbers = list(filter(lambda x: x % 2 == 0, numbers))

    from functools import reduce
    # Reduce: Berechne die Summe der Zahlen in der Liste
    reduced_sum = reduce(lambda x, y: x + y, numbers)

    explanation = "Ich kann die Funktionen Map, Filter und Reduce einzeln auf Listen anwenden. " \
                  "Beispiel: Gegebene Liste [1, 2, 3, 4, 5],\n" \
                  "Map: Quadrierte Zahlen -> {}\n" \
                  "Filter: Filterte gerade Zahlen -> {}\n" \
                  "Reduce: Summe der Zahlen -> {}".format(mapped_numbers, filtered_numbers, reduced_sum)

    return jsonify({'Kompetenz': 'B4G', 'Erfuellt': True, 'Beschreibung': explanation})

@app.route('/b4f', methods=['GET'])
def apply_map_filter_reduce_combined():
    data = [1, 2, 3, 4, 5]

    # Kombination von Map, Filter und Reduce: Berechne die Summe der Quadrate der geraden Zahlen
    result = reduce(lambda x, y: x + y, map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, data)))

    explanation = "Ich kann Map, Filter und Reduce kombiniert verwenden, um Daten zu verarbeiten und " \
                  "zu manipulieren, die komplexere Transformationen erfordern. " \
                  "Beispiel: Gegebene Daten [1, 2, 3, 4, 5],\n" \
                  "Kombination von Map, Filter und Reduce: Summe der Quadrate der geraden Zahlen -> {}".format(result)

    return jsonify({'Kompetenz': 'B4F', 'Erfuellt': True, 'Beschreibung': explanation})

@app.route('/b4e', methods=['GET'])
def apply_map_filter_reduce_complex():
    data = [
        {'name': 'Alice', 'score': 90},
        {'name': 'Bob', 'score': 85},
        {'name': 'Charlie', 'score': 95},
    ]

    # Kombination von Map, Filter und Reduce: Berechne den Durchschnitt der Punktzahlen
    total_score = reduce(lambda x, y: x + y, map(lambda d: d['score'], data))
    average_score = total_score / len(data)

    explanation = "Ich kann Map, Filter und Reduce verwenden, um komplexe Datenverarbeitungsaufgaben " \
                  "zu loesen, wie die Aggregation von Daten oder die Transformation von Datenstrukturen. " \
                  "Beispiel: Gegebene Daten mit Namen und Punktzahlen,\n" \
                  "Kombination von Map, Filter und Reduce: Durchschnitt der Punktzahlen -> {}".format(average_score)

    return jsonify({'Kompetenz': 'B4E', 'Erfuellt': True, 'Beschreibung': explanation})

@app.route('/c1g', methods=['GET'])
def list_refactoring_techniques():
    refactoring_techniques = [
        "Extrahieren von Methoden",
        "Umbenennen von Variablen und Funktionen",
        "Aufteilen von großen Funktionen in kleinere",
        "Entfernen von Redundanzen",
        "Anwenden von Design Patterns"
    ]

    explanation = "Refactoring-Techniken verbessern die Lesbarkeit und Verständlichkeit des Codes. Hier sind einige Beispiele:"

    return jsonify({'Kompetenz': 'C1G', 'Erfüllt': True, 'Erklärung': explanation, 'Refactoring-Techniken': refactoring_techniques})

@app.route('/c1f', methods=['GET'])
def apply_refactoring_techniques():
    original_code = """
    def calculate_area(radius):
        return 3.14 * radius * radius
    """

    refactored_code = """
    def calculate_circle_area(radius):
        return math.pi * radius ** 2
    """

    explanation = "Ich kann mit Refactoring-Techniken einen Code lesbarer und verständlicher machen. " \
                  "Hier ist ein Beispiel, bei dem eine Funktion zur Berechnung der Fläche eines Kreises refaktoriert wird."

    return jsonify({'Kompetenz': 'C1F', 'Erfüllt': True, 'Erklärung': explanation,
                    'Original Code': original_code, 'Refaktorierter Code': refactored_code})

@app.route('/c1e', methods=['GET'])
def assess_refactoring_impact():
    original_function = """
    def add_numbers(a, b):
        return a + b
    """

    refactored_function = """
    def add_numbers(a, b):
        return a + b + 1
    """

    impact_assessment = "Die Auswirkungen des Refactorings auf das Verhalten des Codes müssen sorgfältig " \
                        "beurteilt werden. Hier ist ein Beispiel, bei dem eine unerwünschte Änderung eingeführt wurde."

    return jsonify({'Kompetenz': 'C1E', 'Erfüllt': True, 'Auswirkungsbeurteilung': impact_assessment,
                    'Original Funktion': original_function, 'Refaktorierte Funktion': refactored_function})


if __name__ == '__main__':
    app.run()