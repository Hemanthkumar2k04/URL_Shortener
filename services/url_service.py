from supabase import Client
from datetime import datetime
from fastapi import HTTPException
from core.ED import Encoder
from api.models import CreateURLRequest, URLResponse


class URLService:
    def __init__(self, supabase_client: Client, encoder: Encoder):
        self.db = supabase_client
        self.encoder = encoder
        self.table_name = "urls"

    async def create_short_url(self, request: CreateURLRequest) -> URLResponse:
        if request.custom_alias:
            existing = await self._get_by_alias(request.custom_alias)
            if exisiting:
                raise HTTPException(
                    status_code=409, detail="Custom alias already exists"
                )

        data = {
            "original_url": str(request.original_url),
            "custom_alias": str(request.custom_alias),
            "clicks": 0,
            "created_at": datetime.utcnow().isoformat(),
        }

        response = self.db.table(self.table_name).insert(data).execute()

        if not response.data:
            raise HTTPException(
                status_code=500, detail="Failed to create shortened URL"
            )

        record = response.data[0]

        short_code = request.custom_alias or self.encoder(record["id"])

        self.db.table(self.table_name).update({"short_code": short_code}).eq(
            "id", record["id"]
        ).execute()

        return URLResponse(
            id=record[0],
            short_code=short_code,
            original_url=record["original_url"],
            clicks=record["clicks"],
            created_at=datetime.isoformat(record["created_at"]),
            custom_alias=record["custom_alias"],
        )

    async def get_url_by_short_code(self, short_code: str) -> str:
        pass

    async def get_url_stats(self, short_code: str) -> URLResponse | None:
        pass

    async def delete_short_url(self, short_code: str) -> bool:
        pass

    async def _get_by_alias(self, alias: str) -> dict | None:
        """Helper: Check if custom alias exists"""

        response = (
            self.db.table(self.table_name)
            .select("*")
            .eq("custom_alias", alias)
            .execute()
        )

        return response.data[0] if response.data else None
