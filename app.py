from flask import Flask, render_template, request, jsonify

from chat import get_response

app = Flask(__name__)


@app.get("/")
def index_get():
    return render_template("base.html")

# @app.post("/predict")
@app.route('/predict', methods=['GET','POST'])
def predict():
    print('here')
    if request.method == 'POST':
        print('he')
        text = request.get_json().get("message")
        print('he2')
        # ToDo: check if text s valid
        response = get_response(text)
        print('he3')
        message = {"answer": response}
        print('he4')
        return jsonify(message)
    else:
        return jsonify({"answer": 'error'})


if __name__ == "__main__":
    app.run(debug=True)
