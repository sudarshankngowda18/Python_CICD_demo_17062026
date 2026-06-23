from flask import Flask, request, jsonify
from math_operations import add

app = Flask(__name__)

@app.route("/add", methods=["GET", "POST"])
def add_numbers():
        data = request.get_json()
        a = data["a"]
        b = data["b"]
        result = add(a,b)
        return jsonify({
            "results": result
            })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    

#%%
# curl -X POST http://127.0.0.1:5000/add ^
# -H "Content-Type: application/json" ^
# -d "{\"a\":10,\"b\":5}"
#%%