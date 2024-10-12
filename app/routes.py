from flask import jsonify, request
from app.models import db, Hero, Power, HeroPower

@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    hero_list = [{"id": hero.id, "name": hero.name, "super_name": hero.super_name} for hero in heroes]
    return jsonify(hero_list), 200

@app.route('/heroes/<int:id>', methods=['GET'])
def get_hero_by_id(id):
    hero = Hero.query.get(id)
    if hero:
        hero_powers = [{"power": hp.power.to_dict(), "strength": hp.strength} for hp in hero.hero_powers]
        hero_data = {
            "id": hero.id,
            "name": hero.name,
            "super_name": hero.super_name,
            "hero_powers": hero_powers
        }
        return jsonify(hero_data), 200
    else:
        return jsonify({"error": "Hero not found"}), 404

