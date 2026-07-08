from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel, ConfigDict



class ArticleCreate(BaseModel):
    title: str
    content: str
    author_name: str
    blog_id: Optional[int] = None


class ArticleUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    author_name: Optional[str] = None
    blog_id: Optional[int] = None


class ArticleRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    content: str
    author_name: str
    blog_id: Optional[int]
    created_at: datetime
    updated_at: datetime


class ArticleReadWithComments(ArticleRead):
    comments: List["CommentRead"] = []



class CommentCreate(BaseModel):
    author_name: str
    text: str


class CommentUpdate(BaseModel):
    text: str


class CommentRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    article_id: int
    author_name: str
    text: str
    created_at: datetime


ArticleReadWithComments.model_rebuild()
