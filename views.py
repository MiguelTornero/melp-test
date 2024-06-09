from flask import jsonify, request

from database import create_session
from models import Restaurant
from config import DEFAULT_QUERY_LIMIT

def get_all_restaurants(limit = DEFAULT_QUERY_LIMIT):
    with create_session() as session:
        query_results = session.query(Restaurant).limit(limit).all()

        return jsonify(query_results)

def get_restaurant_by_id(id: str):
    with create_session() as session:
        query_result = session.query(Restaurant).filter(Restaurant.id == id).first()
        if query_result == None:
            return jsonify({"error": "not found"}), 404
        return jsonify(query_result)
    
def update_restaurant_by_id(id: str):
    req_data = request.get_json(force=True)
    with create_session() as session:
        query_result = session.query(Restaurant).filter(Restaurant.id == id).update(req_data, synchronize_session="fetch")
        
        try: 
            session.commit()
        except Exception as e:
            return jsonify({"error": str(e)})
        
        status = 200
        if query_result == 0:
            status = 404
        
        return jsonify({"changed_rows": query_result}), status

def delete_restaurant_by_id(id: str):
    with create_session() as session:
        query_result = session.query(Restaurant).filter(Restaurant.id == id).delete(synchronize_session="fetch")
        try: 
            session.commit()
        except Exception as e:
            return jsonify({"error": str(e)})
        
        status = 200
        if query_result == 0:
            status = 404
        
        return jsonify({"deleted_rows": query_result}), status

def create_restaurant():
    req_data : dict = request.get_json(force=True)
    
    r = Restaurant()

    if "id" in req_data:
        r.id = str(req_data["id"])
    if "rating" in req_data:
        r.rating = int(req_data["rating"])
    if "name" in req_data:
        r.name = str(req_data["name"])
    if "site" in req_data:
        r.site = str(req_data["site"])
    if "email" in req_data:
        r.email = str(req_data["email"])
    if "phone" in req_data:
        r.phone = str(req_data["phone"])
    if "street" in req_data:
        r.street = str(req_data["street"])
    if "city" in req_data:
        r.city = str(req_data["city"])
    if "state" in req_data:
        r.state = str(req_data["state"])
    if "lat" in req_data:
        r.lat = float(req_data["lat"])
    if "lng" in req_data:
        r.lng = float(req_data["lng"])
    
    with create_session() as sesssion:
        sesssion.add(r)
        try:
            sesssion.commit()
        except Exception as e:
            return jsonify({"error": str(e)})
        
        return jsonify({"id": r.id})