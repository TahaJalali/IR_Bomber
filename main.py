#Khar
from flask import Flask

app = Flask(__name__)

@app.route("/InsertDB")
def hello_world():
    # Create a simple button in cernter of the page in html
    return """<!DOCTYPE html>
<html lang='en'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Insert Api DB</title>
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        button {
            padding: 10px 20px;
            font-size: 16px;
        }
    </style>
</head>
<body>
    <button onclick='alert("DB Insterted Sucsessfuly!")'>Insert DB</button>
</body>
</html>"""
app.run()

def Main():
    # Code to handle the main logic of the program
    pass

def DB_Connection():
    # Code to establish a connection to the sqlite database
    pass

def Api_List_Info():
    # Code to read the API list from a sqlite database
    pass
