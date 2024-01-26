import random
import string
from http import HTTPStatus


def generate_random_string():
    length = random.randint(1, 255)
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string


def content_generator(likes, comments, rating, relation_uuid):
    out = []
    likes_content = [
        {
            "relation_uuid": relation_uuid,
            "object_type": "like",
            "content": ""
        } for i in range(likes)
    ]

    comments_content = [
        {
            "relation_uuid": relation_uuid,
            "object_type": "comment",
            "content": generate_random_string()
        } for i in range(comments)
    ]

    ratting_content = [
        {
            "relation_uuid": relation_uuid,
            "object_type": "rating",
            "content": random.randint(0, 10)
        } for i in range(rating)
    ]

    out.extend(likes_content)
    out.extend(comments_content)
    out.extend(ratting_content)
    if len(ratting_content) > 0:
        avg_rating = sum(
            [rating["content"] for rating in ratting_content]
        ) / len(ratting_content)
    else:
        avg_rating = 0

    return (
        {
            'input_data': out,
            'relation_uuid': relation_uuid
        },
        {
            'likes': len(likes_content),
            'comments': comments,
            'avg_rating': avg_rating,
            'status': HTTPStatus.CREATED
        }
    )


test_metrics = [
    content_generator(
        likes=10,
        comments=0,
        rating=0,
        relation_uuid='e14b3ea9-b4db-4d73-a7d8-72815ac3eb61'
    ),

    content_generator(
        likes=0,
        comments=10,
        rating=0,
        relation_uuid='e14b3ea9-b4db-4d73-a7d8-72815ac3eb63'
    ),

    content_generator(
        likes=0,
        comments=0,
        rating=10,
        relation_uuid='e14b3ea9-b4db-4d73-a7d8-72815ac3eb64'
    ),
    content_generator(
        likes=15,
        comments=20,
        rating=10,
        relation_uuid='e14b3ea9-b4db-4d73-a7d8-72815ac3eb65'
    ),

]
