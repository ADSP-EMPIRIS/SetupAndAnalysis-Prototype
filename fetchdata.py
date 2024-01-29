from dotenv import load_dotenv
import os
from supabase import create_client, Client

# Load environment variables from .env file
load_dotenv()

# Get Supabase URL and Key from environment variables
supabase_url = os.getenv("NEXT_PUBLIC_SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_SERVICE_ROLE_KEY")

supabase: Client = create_client(supabase_url, supabase_key)

# Provided API key for authentication
api_key = 'key_9dWvLH5RNrUi7kkruwBpZz'

# Query the api_keys table to get user_id
user_data = supabase.table('apikeys').select('user_id').eq('key_id', api_key).execute()

# Extract user_id
user_id = user_data.data[0]['user_id'] if user_data.data else None

if not user_id:
    print("User ID not found for the given API key.")
else:
    # Query the experiment_run table for this user's data
    experiment_data = supabase.table('experiment_run').select('*').eq('user_id', user_id).execute()

    print( experiment_data.data)
