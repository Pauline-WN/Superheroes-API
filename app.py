from app.models import db, Hero, Power, HeroPower

hero1 = Hero(name="Kamala Khan", super_name="Ms. Marvel")
hero2 = Hero(name="Carol Danvers", super_name="Captain Marvel")
power1 = Power(name="flight", description="Allows flying at supersonic speed")

db.session.add_all([hero1, hero2, power1])
db.session.commit()
