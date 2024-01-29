from dotenv import load_dotenv
import os
from supabase import create_client, Client
import json

# Load environment variables from .env file
load_dotenv()

# Get Supabase URL and Key from environment variables
supabase_url = os.getenv("NEXT_PUBLIC_SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_SERVICE_ROLE_KEY")

# Create Supabase client
supabase: Client = create_client(supabase_url, supabase_key)


def fetch_data(api_key, app_name):
    # Query the api_keys table to get user_id
    user_data = supabase.table('apikeys').select('user_id').eq('key_id', api_key).execute()

    # Extract user_id
    user_id = user_data.data[0]['user_id'] if user_data.data else None

    if not user_id:
        return "User ID not found for the given API key."

    # Query the experiment_run table for data specific to this user
    experiment_data = supabase.table('experiment_run').select('*').eq('user_id', user_id).execute()

    if experiment_data.data:
        # Filter the results based on the app_name within general_data
        filtered_data = [
            entry for entry in experiment_data.data
            if any(
                len(item) >= 2 and item[0] == "Application name" and item[1] == app_name
                for item in entry.get('general_data', [])
            )
        ]

        return filtered_data if filtered_data else "No data found for the specified app."
    else:
        return "No data found for the user."


def get_run_ids(api_key, app_name):
    data = fetch_data(api_key, app_name)
    if isinstance(data, str):
        return data
    runs = [run['id'] for run in data]
    return runs


api_key = 'key_9dWvLH5RNrUi7kkruwBpZz'
app_name = "App1"

result = fetch_data(api_key, app_name)

# Check if result is a string (indicating an error) or a list (run ids)
if isinstance(result, str):
    print(result)
else:
    pretty_json_output = json.dumps(result, indent=4)
    print(pretty_json_output)
