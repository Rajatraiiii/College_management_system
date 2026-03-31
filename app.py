from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>🎓 College Management System</h1>
    <h3>Modules:</h3>
    <ul>
        <li>Student Management</li>
        <li>Faculty Management</li>
        <li>Course Management</li>
        <li>Fees & Reports</li>
    </ul>
    <p>✅ Running successfully on Kubernetes</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
