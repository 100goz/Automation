from flask import Flask, jsonify, request

app = Flask(__name__)


# ==========================================
# Mock Robot Data
# ==========================================

robot = {
    "robot_id": "RB001",
    "connection": "online",
    "status": "cleaning",
    "battery": 85
}


# ==========================================
# GET
# Robot 상태 조회
# ==========================================

@app.route("/api/robots/<robot_id>/status", methods=["GET"])
def get_robot_status(robot_id):

    if robot_id != robot["robot_id"]:
        return jsonify({
            "message": "Robot not found"
        }), 404

    return jsonify(robot), 200


# ==========================================
# POST
# Robot Wi-Fi 상태 변경
# ==========================================

@app.route("/api/robots/<robot_id>/network", methods=["POST"])
def change_network(robot_id):

    if robot_id != robot["robot_id"]:
        return jsonify({
            "message": "Robot not found"
        }), 404

    data = request.get_json()

    if not data or "connection" not in data:
        return jsonify({
            "message": "connection is required"
        }), 400

    connection = data["connection"]

    if connection not in ["online", "offline"]:
        return jsonify({
            "message": "Invalid connection status"
        }), 400

    robot["connection"] = connection

    return jsonify({
        "robot_id": robot["robot_id"],
        "connection": robot["connection"]
    }), 200


# ==========================================
# Server Start
# ==========================================

if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False
    )
    
    
     