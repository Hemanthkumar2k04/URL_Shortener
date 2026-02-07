from dotenv import load, get
from supabase import create_client, Client

load("../.env")
supabase_url: str = get("SUPABASE_URL")
supabase_anon_key: str = get("SUPABASE_ANON_KEY")

supabase_client: Client = create_client(
    supabase_url=supabase_url, supabase_key=supabase_anon_key
)
