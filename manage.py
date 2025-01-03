from app import app, db  # Import both app and db from app.py
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

# Initialize Manager and Migrate
manager = Manager(app)
migrate = Migrate(app, db)

# Add migrate command to manager
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
