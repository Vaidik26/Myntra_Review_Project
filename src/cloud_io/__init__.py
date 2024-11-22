import pandas as pd
from database_connect import mongo_operation as mongo
import os, sys
from urllib.parse import quote_plus
from src.constants import MONGO_DATABASE_NAME, MONGODB_URL_KEY
from src.exception import CustomException


class MongoIO:
    mongo_ins = None

    def __init__(self):
        if MongoIO.mongo_ins is None:
            # Encode username and password for safety
            username = "Vaidik"
            password = "Vaidik@2002"
            cluster_url = "cluster0.k9n1v.mongodb.net"

            # Use quote_plus to safely encode credentials
            encoded_username = quote_plus(username)
            encoded_password = quote_plus(password)

            # Construct the MongoDB connection URL
            mongo_db_url = f"mongodb+srv://{encoded_username}:{encoded_password}@{cluster_url}/?retryWrites=true&w=majority&appName=Cluster0"

            # Validate if the MongoDB URL exists
            if not mongo_db_url:
                raise Exception(f"Environment key: {MONGODB_URL_KEY} is not set.")

            # Initialize MongoDB connection
            MongoIO.mongo_ins = mongo(
                client_url=mongo_db_url, database_name=MONGO_DATABASE_NAME
            )
        self.mongo_ins = MongoIO.mongo_ins

    def store_reviews(self, product_name: str, reviews: pd.DataFrame):
        """
        Stores reviews in the MongoDB collection.

        Args:
            product_name (str): Name of the product.
            reviews (pd.DataFrame): Reviews data as a pandas DataFrame.
        """
        try:
            # Create a collection name based on the product name
            collection_name = product_name.replace(" ", "_").lower()

            # Insert the reviews into the collection
            self.mongo_ins.bulk_insert(reviews, collection_name)

            print(
                f"Reviews for '{product_name}' stored successfully in the '{collection_name}' collection."
            )
        except Exception as e:
            raise CustomException(e, sys)

    def get_reviews(self, product_name: str):
        """
        Retrieves reviews from the MongoDB collection.

        Args:
            product_name (str): Name of the product to retrieve reviews for.

        Returns:
            Data from the MongoDB collection as a list of dictionaries.
        """
        try:
            # Create a collection name based on the product name
            collection_name = product_name.replace(" ", "_").lower()

            # Retrieve data from the collection
            data = self.mongo_ins.find(collection_name=collection_name)

            print(
                f"Successfully retrieved reviews for '{product_name}' from the '{collection_name}' collection."
            )
            return data
        except Exception as e:
            raise CustomException(e, sys)
