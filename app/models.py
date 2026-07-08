from datetime import datetime
from typing import Optional, List

from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy import Column, DateTime, func, ForeignKey


class Article(SQLModel, table=True):
    __tablename__ = "articles"

    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    content: str
    author_name: str
    blog_id: Optional[int] = Field(default=None, index=True)  

    created_at: datetime = Field(
        sa_column=Column(DateTime, server_default=func.now(), nullable=False)
    )
    updated_at: datetime = Field(
        sa_column=Column(
            DateTime, server_default=func.now(), onupdate=func.now(), nullable=False
        )
    )

    
    comments: List["Comment"] = Relationship(
        back_populates="article",
        sa_relationship_kwargs={"cascade": "all, delete-orphan"},
    )


class Comment(SQLModel, table=True):
    __tablename__ = "comments"

    id: Optional[int] = Field(default=None, primary_key=True)
    article_id: int = Field(
        sa_column=Column(ForeignKey("articles.id", ondelete="CASCADE"), nullable=False)
    )
    author_name: str
    text: str

    created_at: datetime = Field(
        sa_column=Column(DateTime, server_default=func.now(), nullable=False)
    )

    article: Optional[Article] = Relationship(back_populates="comments")
