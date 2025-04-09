import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from scanner.zap_scanner import scan_target
from flask import Flask, render_template
from scanner.zap_scanner import scan_target
from scanner.parser import parse_alerts

app = Flask(__name__)

@app.route("/")
def home():
    alerts = parse_alerts(scan_target("http://testphp.vulnweb.com"))
    return render_template("dashboard.html", alerts=alerts)

if __name__ == "__main__":
    app.run(debug=True)
