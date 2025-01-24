from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/update-score", methods=["POST"])
def update_score():
    try:
        data = request.json
        # هنا يمكن معالجة البيانات
        return jsonify({"message": "تم تحديث البيانات بنجاح!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
