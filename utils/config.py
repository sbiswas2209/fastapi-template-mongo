import dotenv
import os
dotenv.load_dotenv();
mongo_uri=os.getenv("MONGO_URI")
jwt_secret=os.getenv("JWT_SECRET")

