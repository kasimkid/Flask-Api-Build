from flask import Flask, request, jsonify
from models import db, Character, Dimension, Register, Favorite


app = Flask(__name__)


@app.route("/people")
def get_character():
    characters = Character.query.all()
    characters = list(map(lambda character: character.serialize(), characters))

    return jsonify({
        "status":"success",
        "data": characters
    }), 200

@app.route("/people/<int:people_id>")
def get_character_id(character_id):
    character = Character.query.get(character_id)

    if character is not None:
        return jsonify({
            "status": "succcess",
            "data": "character"
        }), 200
    else:
           return jsonify({
            "msg": "Character not found",
            "status": "Error"
        }), 404



@app.route("/dimension")
def get_dimension():
    dimensions = Dimension.query.all()
    dimensions = list(map(lambda dimension: dimension.serialize(), dimensions))

    return jsonify({
        "status":" success",
        "data": dimensions
    }), 200


@app.route("/dimension/<int:dimension_id>")
def get_dimension_id(dimension_id):
    dimension = Dimension.query.get(dimension_id)

    if dimension is not None:
        return jsonify({
            "status": "succcess",
            "data": "Error"
        }), 200

    else:
        return jsonify({
            "msg": "Location not found",
            "status": "Error"
        }), 404
    
@app.route("/register")
def get_register():
    registers = Register.query.all()
    registers = list(map(lambda registers: registers.serialize(), registers))

    return({
        "status": "success",
        "data": registers
    }), 200


@app.route("/register/favorites/<int:register_id>")
def get_register_favorite(register_id):
    favorites = Favorite.query.filter_by(registerID = register_id).all()

    return jsonify({
        "status": "success",
        "data": favorites
    }), 200


@app.route("/favorites/dimension/<int:dimension_id>", methods= ["POST"])
def generate_favorites_dimension(dimension_id):
    dimension_fav = Dimension.query.filter_by(dimension_id)
    data = request.get_json()


    db.session.add(dimension_fav)
    db.session.commit()


    return jsonify({
        "msg": "Dimension Agree",
        "status": "success"
    }), 200


@app.route("/favorite/people/<int:character_id>", methods=["POST"])
def generate_favorites_character(character_id):
    character_fav = Character.query.filter_by(character_id)
    data = request.get_json()

    db.session.add(character_fav)
    db.session.commit()

    return jsonify({
        "mgs": "Character added to Favorites",
        "status":"success"
    }), 200


@app.route("/favorite/people/<int:dimension_id>", methods=["DELETE"])
def delete_favorites_dimension(dimension_id):
    dimension_fav = Dimension.query.get(dimension_id)
    if dimension_fav is not None:
        db.session.delete(dimension_id)
        db.session.commit()
        return jsonify({
            "msg": "Dimension it`s delete from favorite",
            "status": "success"
        }), 200
    else:
        return jsonify({
            "msg": "Dimension not found in favorite",
            "status": "error"
        }), 404

@app.route("/favorite/people/<int:character_id>", methods=["DELETE"])
def delete_favorites_character(character_id):
    character_fav = Character.query.filter_by(character_id)
    if character_fav is not None:
        db.session.deleted(character_id)
        db.session.commit()
        return jsonify({
            "msg": "Character it`s delete from favorite",
            "status": "success"
        }), 200
    else:
        return jsonify({
            "msg": "Character not found in favorite",
            "status": "error"
        }), 404




    