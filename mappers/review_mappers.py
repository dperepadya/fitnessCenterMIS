from db_models.review import Review as ReviewModel
from models.review import Review as Review


def review_to_reviewdb(review):
    if review is None:
        return None
    return ReviewModel(
            date=review.date,
            grade=review.grade,
            comment=review.comment,
            client_id=review.client_id,
            trainer_id=review.trainer_id
        )


def reviewdb_to_review(review):
    if review is None:
        return None
    return Review(
            date=review.date,
            grade=review.grade,
            comment=review.comment,
            client_id=review.client_id,
            trainer_id=review.trainer_id
        )
