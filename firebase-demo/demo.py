# Import necessary firebase libraries
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent
CRED_PATH = os.path.join(BASE_DIR, "firebase-demo\\firebase-credentials.json")

# Initialize connection to firebase
cred = credentials.Certificate(CRED_PATH)
app = firebase_admin.initialize_app(cred)
db = firestore.client()

doc_ref = db.collection("content").document("test1")

tweet = input("Enter your tweet: ")
doc_ref.set(
    {
        "body": tweet,
        "type": "tweet",
    }
)
