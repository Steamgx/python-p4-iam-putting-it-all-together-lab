from config import app, db
import os

# Get absolute path to server directory
server_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(server_dir, 'app.db')

# Update configuration
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'

with app.app_context():
    # Create all tables
    db.create_all()
    
    # Verify creation
    print(f"Database should be at: {db_path}")
    print(f"File exists: {os.path.exists(db_path)}")
