from pymongo import MongoClient, errors

# MongoDB setup
try:
    client = MongoClient('mongodb://localhost:27017/')  # Replace with your MongoDB URI
    db = client['dumelahealth_db']
    clinics_collection = db['clinics']
    print("Connected to MongoDB successfully.")
except errors.ConnectionError as e:
    print(f"Error connecting to MongoDB: {e}")
    exit(1)

# Sample clinic data for Johannesburg, Pretoria, and Thembisa areas
clinics = [
    # Johannesburg Clinics
    {
        'name': 'Johannesburg Clinic One',
        'address': '123 Main St, Section A, Johannesburg',
        'location': {
            'type': 'Point',
            'coordinates': [28.0473, -26.2041]  # Longitude, Latitude
        },
        'services': 'General Practice, Pediatrics',
        'hours': 'Mon-Fri 9am-5pm',
        'directions': 'https://www.google.com/maps'
    },
    {
        'name': 'Johannesburg Clinic Two',
        'address': '456 Elm St, Section B, Johannesburg',
        'location': {
            'type': 'Point',
            'coordinates': [28.0573, -26.2141]  # Longitude, Latitude
        },
        'services': 'Dermatology, Cardiology',
        'hours': 'Mon-Fri 8am-6pm',
        'directions': 'https://www.google.com/maps'
    },
    # Add more Johannesburg clinics here...
    {
        'name': 'Johannesburg Clinic Three',
        'address': '789 Oak St, Section C, Johannesburg',
        'location': {
            'type': 'Point',
            'coordinates': [28.0673, -26.2241]  # Longitude, Latitude
        },
        'services': 'Orthopedics, Neurology',
        'hours': 'Mon-Fri 9am-5pm',
        'directions': 'https://www.google.com/maps'
    },
    {
        'name': 'Johannesburg Clinic Four',
        'address': '101 Pine St, Section D, Johannesburg',
        'location': {
            'type': 'Point',
            'coordinates': [28.0773, -26.2341]  # Longitude, Latitude
        },
        'services': 'Ophthalmology, ENT',
        'hours': 'Mon-Fri 9am-5pm',
        'directions': 'https://www.google.com/maps'
    },
    {
        'name': 'Johannesburg Clinic Five',
        'address': '202 Birch St, Section E, Johannesburg',
        'location': {
            'type': 'Point',
            'coordinates': [28.0873, -26.2441]  # Longitude, Latitude
        },
        'services': 'Gynecology, Urology',
        'hours': 'Mon-Fri 9am-5pm',
        'directions': 'https://www.google.com/maps'
    },
    {
        'name': 'Johannesburg Clinic Six',
        'address': '303 Cedar St, Section F, Johannesburg',
        'location': {
            'type': 'Point',
            'coordinates': [28.0973, -26.2541]  # Longitude, Latitude
        },
        'services': 'General Practice, Pediatrics',
        'hours': 'Mon-Fri 9am-5pm',
        'directions': 'https://www.google.com/maps'
    },
    {
        'name': 'Johannesburg Clinic Seven',
        'address': '404 Maple St, Section G, Johannesburg',
        'location': {
            'type': 'Point',
            'coordinates': [28.1073, -26.2641]  # Longitude, Latitude
        },
        'services': 'Dermatology, Cardiology',
        'hours': 'Mon-Fri 8am-6pm',
        'directions': 'https://www.google.com/maps'
    },
    {
        'name': 'Johannesburg Clinic Eight',
        'address': '505 Walnut St, Section H, Johannesburg',
        'location': {
            'type': 'Point',
            'coordinates': [28.1173, -26.2741]  # Longitude, Latitude
        },
        'services': 'Orthopedics, Neurology',
        'hours': 'Mon-Fri 9am-5pm',
        'directions': 'https://www.google.com/maps'
    },
    {
        'name': 'Johannesburg Clinic Nine',
        'address': '606 Chestnut St, Section I, Johannesburg',
        'location': {
            'type': 'Point',
            'coordinates': [28.1273, -26.2841]  # Longitude, Latitude
        },
        'services': 'Ophthalmology, ENT',
        'hours': 'Mon-Fri 9am-5pm',
        'directions': 'https://www.google.com/maps'
    },
    {
        'name': 'Johannesburg Clinic Ten',
        'address': '707 Ash St, Section J, Johannesburg',
        'location': {
            'type': 'Point',
            'coordinates': [28.1373, -26.2941]  # Longitude, Latitude
        },
        'services': 'Gynecology, Urology',
        'hours': 'Mon-Fri 9am-5pm',
        'directions': 'https://www.google.com/maps'
    },
    
    # Pretoria Clinics
    {
        'name': 'Pretoria Clinic One',
        'address': '123 Main St, Section A, Pretoria',
        'location': {
            'type': 'Point',
            'coordinates': [28.2293, -25.7479]  # Longitude, Latitude
        },
        'services': 'General Practice, Pediatrics',
        'hours': 'Mon-Fri 9am-5pm',
        'directions': 'https://www.google.com/maps'
    },
    {
        'name': 'Pretoria Clinic Two',
        'address': '456 Elm St, Section B, Pretoria',
        'location': {
            'type': 'Point',
            'coordinates': [28.2393, -25.7579]  # Longitude, Latitude
        },
        'services': 'Dermatology, Cardiology',
        'hours': 'Mon-Fri 8am-6pm',
        'directions': 'https://www.google.com/maps'
    },
    # Add more Pretoria clinics here...
    {
        'name': 'Pretoria Clinic Three',
        'address': '789 Oak St, Section C, Pretoria',
        'location': {
            'type': 'Point',
            'coordinates': [28.2493, -25.7679]  # Longitude, Latitude
        },
        'services': 'Orthopedics, Neurology',
        'hours': 'Mon-Fri 9am-5pm',
        'directions': 'https://www.google.com/maps'
    },
    {
        'name': 'Pretoria Clinic Four',
        'address': '101 Pine St, Section D, Pretoria',
        'location': {
            'type': 'Point',
            'coordinates': [28.2593, -25.7779]  # Longitude, Latitude
        },
        'services': 'Ophthalmology, ENT',
        'hours': 'Mon-Fri 9am-5pm',
        'directions': 'https://www.google.com/maps'
    },
    {
        'name': 'Pretoria Clinic Five',
        'address': '202 Birch St, Section E, Pretoria',
        'location': {
            'type': 'Point',
            'coordinates': [28.2693, -25.7879]  # Longitude, Latitude
        },
        'services': 'Gynecology, Urology',
        'hours': 'Mon-Fri 9am-5pm',
        'directions': 'https://www.google.com/maps'
    },
    {
        'name': 'Pretoria Clinic Six',
        'address': '303 Cedar St, Section F, Pretoria',
        'location': {
            'type': 'Point',
            'coordinates': [28.2793, -25.7979]  # Longitude, Latitude
        },
        'services': 'General Practice, Pediatrics',
        'hours': 'Mon-Fri 9am-5pm',
        'directions': 'https://www.google.com/maps'
    },
    {
        'name': 'Pretoria Clinic Seven',
        'address': '404 Maple St, Section G, Pretoria',
        'location': {
            'type': 'Point',
            'coordinates': [28.2893, -25.8079]  # Longitude, Latitude
        },
        'services': 'Dermatology, Cardiology',
        'hours': 'Mon-Fri 8am-6pm',
        'directions': 'https://www.google.com/maps'
    },
    {
        'name': 'Pretoria Clinic Eight',
        'address': '505 Walnut St, Section H, Pretoria',
        'location': {
            'type': 'Point',
            'coordinates': [28.2993, -25.8179]  # Longitude, Latitude
        },
        'services': 'Orthopedics, Neurology',
        'hours': 'Mon-Fri 9am-5pm',
        'directions': 'https://www.google.com/maps'
    },
    {
        'name': 'Pretoria Clinic Nine',
        'address': '606 Chestnut St, Section I, Pretoria',
        'location': {
            'type': 'Point',
            'coordinates': [28.3093, -25.8279]  # Longitude, Latitude
        },
        'services': 'Ophthalmology, ENT',
        'hours': 'Mon-Fri 9am-5pm',
        'directions': 'https://www.google.com/maps'
    },
    {
        'name': 'Pretoria Clinic Ten',
        'address': '707 Ash St, Section J, Pretoria',
        'location': {
            'type': 'Point',
            'coordinates': [28.3193, -25.8379]  # Longitude, Latitude
        },
        'services': 'Gynecology, Urology',
        'hours': 'Mon-Fri 9am-5pm',
        'directions': 'https://www.google.com/maps'
    },
    
    # Thembisa Clinics
    {
        'name': 'Thembisa Clinic One',
        'address': '123 Main St, Section A, Thembisa',
        'location': {
            'type': 'Point',
            'coordinates': [28.2105, -26.0004]  # Longitude, Latitude
        },
        'services': 'General Practice, Pediatrics',
        'hours': 'Mon-Fri 9am-5pm',
        'directions': 'https://www.google.com/maps'
    },
    {
        'name': 'Thembisa Clinic Two',
        'address': '456 Elm St, Section B, Thembisa',
        'location': {
            'type': 'Point',
            'coordinates': [28.2155, -26.0054]  # Longitude, Latitude
        },
        'services': 'Dermatology, Cardiology',
        'hours': 'Mon-Fri 8am-6pm',
        'directions': 'https://www.google.com/maps'
    },
    # Add more Thembisa clinics here...
    {
        'name': 'Thembisa Clinic Three',
        'address': '789 Pine St, Section C, Thembisa',
        'location': {
            'type': 'Point',
            'coordinates': [28.2205, -26.0104]  # Longitude, Latitude
        },
        'services': 'Gynecology, Urology',
        'hours': 'Mon-Fri 9am-5pm',
        'directions': 'https://www.google.com/maps'
    },
    {
        'name': 'Thembisa Clinic Four',
        'address': '101 Maple St, Section D, Thembisa',
        'location': {
            'type': 'Point',
            'coordinates': [28.2255, -26.0154]  # Longitude, Latitude
        },
        'services': 'Ophthalmology, ENT',
        'hours': 'Mon-Fri 9am-5pm',
        'directions': 'https://www.google.com/maps'
    },
    {
        'name': 'Thembisa Clinic Five',
        'address': '202 Birch St, Section E, Thembisa',
        'location': {
            'type': 'Point',
            'coordinates': [28.2305, -26.0204]  # Longitude, Latitude
        },
        'services': 'Orthopedics, Neurology',
        'hours': 'Mon-Fri 9am-5pm',
        'directions': 'https://www.google.com/maps'
    },
    {
        'name': 'Thembisa Clinic Six',
        'address': '303 Cedar St, Section F, Thembisa',
        'location': {
            'type': 'Point',
            'coordinates': [28.2355, -26.0254]  # Longitude, Latitude
        },
        'services': 'General Practice, Pediatrics',
        'hours': 'Mon-Fri 9am-5pm',
        'directions': 'https://www.google.com/maps'
    },
    {
        'name': 'Thembisa Clinic Seven',
        'address': '404 Maple St, Section G, Thembisa',
        'location': {
            'type': 'Point',
            'coordinates': [28.2405, -26.0304]  # Longitude, Latitude
        },
        'services': 'Dermatology, Cardiology',
        'hours': 'Mon-Fri 8am-6pm',
        'directions': 'https://www.google.com/maps'
    },
    {
        'name': 'Thembisa Clinic Eight',
        'address': '505 Walnut St, Section H, Thembisa',
        'location': {
            'type': 'Point',
            'coordinates': [28.2455, -26.0354]  # Longitude, Latitude
        },
        'services': 'Orthopedics, Neurology',
        'hours': 'Mon-Fri 9am-5pm',
        'directions': 'https://www.google.com/maps'
    },
    {
        'name': 'Thembisa Clinic Nine',
        'address': '606 Chestnut St, Section I, Thembisa',
        'location': {
            'type': 'Point',
            'coordinates': [28.2505, -26.0404]  # Longitude, Latitude
        },
        'services': 'Ophthalmology, ENT',
        'hours': 'Mon-Fri 9am-5pm',
        'directions': 'https://www.google.com/maps'
    },
    {
        'name': 'Thembisa Clinic Ten',
        'address': '707 Ash St, Section J, Thembisa',
        'location': {
            'type': 'Point',
            'coordinates': [28.2555, -26.0454]  # Longitude, Latitude
        },
        'services': 'Gynecology, Urology',
        'hours': 'Mon-Fri 9am-5pm',
        'directions': 'https://www.google.com/maps'
    }
]

# Insert clinic data into the collection
try:
    result = clinics_collection.insert_many(clinics)
    print(f"Inserted {len(result.inserted_ids)} clinics into the database.")
except errors.BulkWriteError as e:
    print(f"Error inserting data: {e.details}")

# Create a geospatial index on the location field
try:
    clinics_collection.create_index([('location', '2dsphere')])
    print("Geospatial index created on the location field.")
except errors.OperationFailure as e:
    print(f"Error creating geospatial index: {e}")