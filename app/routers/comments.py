from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from app.database import get_session
from app.models import Comment
from app.schemas import CommentUpdate, CommentRead

router = APIRouter(prefix="/comments", tags=["Comments"])


def get_comment_or_404(comment_id: int, session: Session) -> Comment:
    comment = session.get(Comment, comment_id)
    if comment is None:
        raise HTTPException(status_code=404, detail="Комментарий не найден")
    return comment


@router.put("/{comment_id}", response_model=CommentRead)
def update_comment(
    comment_id: int, payload: CommentUpdate, session: Session = Depends(get_session)
):
    comment = get_comment_or_404(comment_id, session)
    comment.text = payload.text
    session.add(comment)
    session.commit()
    session.refresh(comment)
    return comment


@router.delete("/{comment_id}", status_code=204)
def delete_comment(comment_id: int, session: Session = Depends(get_session)):
    comment = get_comment_or_404(comment_id, session)
    session.delete(comment)
    session.commit()
    return None
