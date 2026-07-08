from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session, select

from app.database import get_session
from app.models import Article, Comment
from app.schemas import (
    ArticleCreate,
    ArticleUpdate,
    ArticleRead,
    ArticleReadWithComments,
    CommentCreate,
    CommentRead,
)

router = APIRouter(prefix="/articles", tags=["Articles"])


def get_article_or_404(article_id: int, session: Session) -> Article:
    article = session.get(Article, article_id)
    if article is None:
        raise HTTPException(status_code=404, detail="Статья не найдена")
    return article


@router.get("", response_model=List[ArticleRead])
def list_articles(
    blog_id: Optional[int] = Query(default=None, description="Фильтр по ID блога"),
    session: Session = Depends(get_session),
):
    
    query = select(Article)
    if blog_id is not None:
        query = query.where(Article.blog_id == blog_id)
    return session.exec(query).all()


@router.get("/{article_id}", response_model=ArticleReadWithComments)
def get_article(article_id: int, session: Session = Depends(get_session)):
    
    return get_article_or_404(article_id, session)


@router.post("", response_model=ArticleRead, status_code=201)
def create_article(payload: ArticleCreate, session: Session = Depends(get_session)):
    article = Article(**payload.model_dump())
    session.add(article)
    session.commit()
    session.refresh(article)
    return article


@router.put("/{article_id}", response_model=ArticleRead)
def update_article(
    article_id: int, payload: ArticleUpdate, session: Session = Depends(get_session)
):
    article = get_article_or_404(article_id, session)

    update_data = payload.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(article, field, value)


    from datetime import datetime
    article.updated_at = datetime.utcnow()

    session.add(article)
    session.commit()
    session.refresh(article)
    return article


@router.delete("/{article_id}", status_code=204)
def delete_article(article_id: int, session: Session = Depends(get_session)):
   
    article = get_article_or_404(article_id, session)
    session.delete(article)
    session.commit()
    return None


@router.get("/{article_id}/comments", response_model=List[CommentRead])
def list_comments(article_id: int, session: Session = Depends(get_session)):
    get_article_or_404(article_id, session)  # 404, если статьи нет
    query = select(Comment).where(Comment.article_id == article_id)
    return session.exec(query).all()


@router.post("/{article_id}/comments", response_model=CommentRead, status_code=201)
def add_comment(
    article_id: int, payload: CommentCreate, session: Session = Depends(get_session)
):
    
    get_article_or_404(article_id, session)

    comment = Comment(article_id=article_id, **payload.model_dump())
    session.add(comment)
    session.commit()
    session.refresh(comment)
    return comment
