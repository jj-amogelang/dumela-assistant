from pymongo import MongoClient

# MongoDB setup
client = MongoClient('mongodb://localhost:27017/')  # Replace with your MongoDB URI
db = client['dumelahealth_db']
clinics_collection = db['clinics']

# Ensure the clinics collection has a geospatial index on the location field
clinics_collection.create_index([('location', '2dsphere')])

def get_nearby_clinics(lat, lng, max_distance=5000):
    clinics = list(clinics_collection.find({
        'location': {
            '$near': {
                '$geometry': {
                    'type': 'Point',
                    'coordinates': [lng, lat]
                },
                '$maxDistance': max_distance  # 5 km radius
            }
        }
    }, {'_id': 0, 'name': 1, 'address': 1, 'location.coordinates': 1, 'services': 1, 'hours': 1, 'directions': 1}))

    formatted_clinics = []
    for clinic in clinics:
        formatted_clinics.append({
            'name': clinic['name'],
            'address': clinic['address'],
            'lat': clinic['location']['coordinates'][1],
            'lng': clinic['location']['coordinates'][0],
            'services': clinic['services'],
            'hours': clinic['hours'],
            'directions': clinic['directions']
        })

    return formatted_clinics
