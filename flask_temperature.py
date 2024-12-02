from flask import Flask

app = Flask(__name__)


def celsius_to_fahrenheit(celsius):
    """Convert celsius to fahrenheit."""
    return celsius * 9.0 / 5 + 32


@app.route('/')
def index():
    return '''<h1>Temperature Converter</h1>
    <p>To convert temperature, add /convert/number to the URL</p>
    <p>For example: /convert/100</p>'''


@app.route('/convert/<float:celsius>')
def convert(celsius):
    """Convert Celsius temperature given in URL to Fahrenheit."""
    fahrenheit = celsius_to_fahrenheit(celsius)
    return f'''<h1>Temperature Converter</h1>
    <p>{celsius}°C is {fahrenheit:.2f}°F</p>'''


if __name__ == '__main__':
    app.run()