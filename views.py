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