"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")



# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def get_all_members():

    members = jackson_family.get_all_members()
   

    return jsonify(members), 200

@app.route('/member' , methods= ['POST'])
def add_member():
    try:
        first_name=request.json.get("first_name")
        age=request.json.get("age")
        lucky_numbers=request.json.get("lucky_numbers")
        id=request.json.get("id")

    
        new_member={
            "first_name":first_name,
            "age":age,
            "id":jackson_family._generateId(),
            "lucky_numbers":lucky_numbers,
            "last_name":"Jackson"
        }

        jackson_family.add_member(new_member)

        return jsonify({"message":"Member added succesfully"}),200
    
    except Exception as e:
        return jsonify({"error": str(e)}),404

    
   

@app.route('/member/<int:member_id>' , methods= ['DELETE'])
def delete_family_member(member_id):
    eliminar_familiar= jackson_family.delete_member(member_id)
    if eliminar_familiar:
        return jsonify({'done': 'True'}), 200
    else:
        return jsonify({'alert': 'family member not found'}), 404
    

                  
@app.route('/member/<int:member_id>', methods=['PUT'])
def update_family_member(member_id):
    new_member = request.json
    updated_member= jackson_family.update_member(member_id, new_member)
    if not updated_member:
        return jsonify({'msg': 'Family family member not found'}), 400
    
    return jsonify ({'done': 'Family member updated sucessfully'})

# this only runs if `$ python src/app.py` is executed

@app.route('/member/<int:member_id>', methods=['GET'])
def get_member(member_id):
    one_member= jackson_family.get_member(member_id)
    if not one_member:
        return jsonify({'msg':'Family member not found'}), 400
    
    return jsonify(one_member) , 200





if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
