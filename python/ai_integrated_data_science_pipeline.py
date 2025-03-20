import pandas as pd
import matplotlib.pyplot as plt 
from pymongo import MongoClient

# Example: Load data from AWS S3 (simulation)
print("Loading dataset...")
data = pd.DataFrame({
    'sales': [200, 220, 250, 270, 300],
    'profit': [50, 60, 70, 65, 80]
})

# Basic Data Analysis
print(data.describe())

# Visualization
plt.plot(data['sales'], data['profit'], marker='o')
plt.title('Sales vs Profit Analysis')
plt.xlabel('Sales')
plt.ylabel('Profit')
plt.show()

# MongoDB connection (simulation)
client = MongoClient('mongodb://localhost:27017/')
db = client['ai_pipeline']
collection = db['processed_data']
collection.insert_one({"summary": data.describe().to_dict()})
print("Data inserted into MongoDB.")
