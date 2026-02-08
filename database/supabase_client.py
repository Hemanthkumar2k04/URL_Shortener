from dotenv import load, get
from supabase import create_client, Client

load("../.env")


class SupabaseClient:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized:
            return

        supabase_url: str = get("SUPABASE_URL")
        supabase_anon_key: str = get("SUPABASE_ANON_KEY")

        self.client: Client = create_client(
            supabase_url=supabase_url, supabase_key=supabase_anon_key
        )
        self._initialized = True

    def get_client(self) -> Client:
        """Get the Supabase client instance"""
        return self.client


supabase_client = SupabaseClient().get_client()
