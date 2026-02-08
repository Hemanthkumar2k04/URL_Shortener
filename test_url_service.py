import asyncio
from dotenv import load, get
from database import supabase_client
from core import Encoder
from services.url_service import URLService
from api.models import CreateURLRequest

encoder = Encoder()

# Create URLService instance
url_service = URLService(supabase_client, encoder)


# Test the function with a random URL
async def test_create_short_url():
    try:
        # Create a test request with a random URL
        request = CreateURLRequest(
            original_url="https://www.example.com/very/long/path2/that/needs/shortening",
            custom_alias=None,  # Let the encoder generate a short code
        )

        print("Testing create_short_url with:")
        print(f"  Original URL: {request.original_url}")
        print(f"  Custom Alias: {request.custom_alias}")
        print()

        # Call the function
        response = await url_service.create_short_url(request)

        print("Success! Response:")
        print(f"  ID: {response.id}")
        print(f"  Short Code: {response.short_code}")
        print(f"  Original URL: {response.original_url}")
        print(f"  Created At: {response.created_at}")
        print(f"  Clicks: {response.clicks}")
        print(f"  Custom Alias: {response.custom_alias}")

        retrieve = await url_service.get_url_by_short_code(response.short_code)

        print("Success")
        print(retrieve)

    except Exception as e:
        print(f"Error occurred: {type(e).__name__}")
        print(f"Message: {str(e)}")


# Run the test
if __name__ == "__main__":
    asyncio.run(test_create_short_url())
