from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random as rand

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    cafes = Cafe.query.all()
    return render_template("index.html", cafes=cafes)
    

@app.route("/random", methods=['GET'])
def random():
    cafes = db.session.query(Cafe).all()
    random_cafe = rand.choice(cafes)
    return jsonify(cafe=random_cafe.to_dict())


@app.route("/all", methods=['GET'])
def all():
    cafes = db.session.query(Cafe).all()
    return jsonify(cafe=[e.to_dict() for e in cafes])


@app.route("/search", methods=['GET'])
def search():
    if 'loc' in request.args:
        query_location = request.args.get("loc").capitalize()
        cafes = Cafe.query.filter_by(location=query_location).all()
        if cafes:
            data = [cafe.to_dict() for cafe in cafes]
            return jsonify(cafe=data)
        else:
            return {"Error": {
                "Not Found": "Sorry, we don't have that cafe at that location."
            }}, 404
    else:
        return {"Error": {
            "No field": "No location field provided. Please specify the location."
        }}, 403


def make_bool(val: int) -> bool:
    return bool(int(val))

@app.route('/add', methods=['POST'])
def  post_new_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        has_sockets=make_bool(request.form.get("sockets")),
        has_toilet=make_bool(request.form.get("toilet")),
        has_wifi=make_bool(request.form.get("wifi")),
        can_take_calls=make_bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    ) 
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."}), 200


@app.route("/update-price/<int:cafe_id>", methods=['PATCH'])
def update(cafe_id):
    new_price = request.args.get('new_price')
    cafe = Cafe.query.get(cafe_id)
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."}), 200
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404


@app.route("/report-closed/<cafe_id>", methods=['DELETE'])
def delete(cafe_id):
    api_key = request.args.get('api-key')
    if api_key == 'thepasswordisamongus':
        cafe = Cafe.query.get(cafe_id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": f"Successfully deleted cafe {cafe_id} from the database."}), 200        
        else:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 403
    else:
            return jsonify(error={"Not Found": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 404

if __name__ == '__main__':
    app.run(debug=True)
