from flask import Flask, request, jsonify
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# Create the Jackson family
jackson_family = FamilyStructure("Jackson")

@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def get_all_members():
    return jsonify(jackson_family.get_all_members()), 200

@app.route('/member/<int:member_id>', methods=['GET'])
def get_member(member_id):
    member = jackson_family.get_member(member_id)
    if member:
        return jsonify(member), 200
    return jsonify({"error": "Miembro no encontrado"}), 404

@app.route('/member', methods=['POST'])
def create_member():
    data = request.get_json()
    if not data or "first_name" not in data or "age" not in data or "lucky_numbers" not in data:
        return jsonify({"error": "Datos incompletos"}), 400

    new_member = {
        "id": data.get("id"),
        "first_name": data["first_name"],
        "last_name": data.get("last_name", jackson_family.last_name),
        "age": data["age"],
        "lucky_numbers": data["lucky_numbers"]
    }

    member = jackson_family.add_member(new_member)
    return jsonify(member), 200

@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    success = jackson_family.delete_member(member_id)
    if success:
        return jsonify({"done": True}), 200
    return jsonify({"error": "Miembro no encontrado"}), 404

if __name__ == '__main__':
    import os
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
