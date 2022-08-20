from typing import Optional

import pydantic


class Blog(pydantic.BaseModel):
    title: str
    description: str
    published_at: Optional[bool]
