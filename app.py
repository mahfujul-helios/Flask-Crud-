from apps import create_app,db
from apps.config import config_dict
import os
 
DEBUG = (os.getenv('DEBUG', 'False') == 'True')

# The configuration
get_config_mode = 'Debug' if DEBUG else 'Production'
app_config = config_dict[get_config_mode.capitalize()]

app = create_app(app_config)

if __name__ == "__main__":
 app.run(debug=True)
