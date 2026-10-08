from pymongo import MongoClient
uri = "mongodb+srv://vivekrawatt17_db_user:Admin123@cluster0.aqiwfru.mongodb.net/?appName=Cluster0"
client = MongoClient(uri, serverSelectionTimeoutMS=30000)

client.admin.command("ping")

print("MongoDB connection successful!")