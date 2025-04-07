from config import app, db
from models import User, Recipe

with app.app_context():
    # Drop all tables if they exist
    db.drop_all()
    
    # Create all tables
    db.create_all()
    
    # Verify tables were created
    print("Database initialized successfully")
    print("Tables created:", db.metadata.tables.keys())
