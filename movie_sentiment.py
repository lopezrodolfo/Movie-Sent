"""
Module: movie_sentiment

Program to analyze movie reviews and predict the sentiment of new reviews.

Author:
1) Rodolfo Lopez (rodolfolopez@sandiego.edu)
"""


def average_review(word, review_filename):
    """
    Computes the average rating of reviews that include the specified word.

    Parameters:
    word (type: string): The term to search for within the reviews.
    review_filename (type: string): The name of the file that contains the reviews.

    Returns:
    total / num_reviews (type: float): The average rating associated with the specified word, or 2.0 if the word is not found in any reviews.
    """

    with open(review_filename, "r", encoding="utf-8") as f:
        total = 0
        num_reviews = 0
        for line in f:
            words = line.lower().split()
            review = words[1:]
            if word.lower() in review:
                score = int(words[0])
                num_reviews += 1
                total += score

    if num_reviews == 0:
        return 2.0
    else:
        return total / num_reviews


def estimate_review_score(movie_review, review_filename):
    """
    Calculates the estimated score for a specified movie review.

    Parameters:
    movie_review (type: string): The review text to be evaluated.
    review_filename (type: string): The name of the file that contains prior reviews.

    Returns:
    acc / len(words)(type: float) The estimated score corresponding to the provided review.
    """

    words = movie_review.lower().split()

    total = 0.0
    for w in words:
        avg = average_review(w, review_filename)
        total += avg

    return total / len(words)


def estimate_user_review():
    """
    Asks user to enter a movie review, then the name of a file with existing
    movie reviews.
    It then calculates the estimated rating of the review they entered, along
    with a description of that rating (e.g. "neutral" or "slightly positive").
    """

    movie_review = input("Enter a movie review: ")
    review_filename = input("Enter the name of the file containing reviews: ")

    score = estimate_review_score(movie_review, review_filename)
    rounded_score = round(score)

    if rounded_score == 0:
        print(f"Estimated score: {score} (negative)")
    elif rounded_score == 1:
        print(f"Estimated score: {score} (somewhat negative)")
    elif rounded_score == 2:
        print(f"Estimated score: {score} (neutral)")
    elif rounded_score == 3:
        print(f"Estimated score: {score} (somewhat positive)")
    else:
        print(f"Estimated score: {score} (positive)")


# Do not modify anything after this point.
if __name__ == "__main__":
    estimate_user_review()
