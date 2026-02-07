from pydantic import BaseModel, HttpUrl, Field
from datetime import datetime
from typing import Optional


class CreateURLRequest(BaseModel):
    original_url: HttpUrl = Field(..., description="The original URL to shorten")
    custom_alias: Optional[str] = Field(
        None, min_length=3, max_length=20, description="Optional custom short code"
    )

    class Config:
        json_schema_extra = {
            "example": {
                "original_url": "https://somerandomurl.com",
                "custom_alias": "gh-repo",
            }
        }


class URLResponse(BaseModel):
    id: int
    short_code: str = Field(..., description="The unique short code")
    original_url: str
    custom_alias: Optional[str]
    created_at: datetime
    clicks: int = Field(default=0, description="Number of times the URL was accessed")

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "short_code": "abc123",
                "original_code": "https://github.com/example/very-long-url",
                "custom_alias": "gh-repo",
                "created_at": datetime.now(),
                "clicks": 4,
            }
        }


class URLRedirectResponse(BaseModel):
    original_url: str
    short_code: str
