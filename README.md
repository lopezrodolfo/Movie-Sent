# Movie Sentiment Analyzer

This program analyzes movie reviews and predicts the sentiment of new reviews.

## Author

Rodolfo Lopez

## Date

Fall 2019

## Features

- Calculates average rating for reviews containing specific words
- Estimates sentiment score for new movie reviews
- Provides a user interface to enter and analyze reviews

## Usage

1. Run the program:

   ```
   python movie_sentiment.py
   ```

2. When prompted, enter a movie review.

3. Enter the name of the file containing existing reviews (e.g. "all_reviews.txt").

4. The program will output an estimated sentiment score and description.

## How it works

- `average_review` function calculates the average rating for reviews containing a given word.
- `estimate_review_score` uses this to estimate an overall score for a new review.
- Scores are mapped to sentiment descriptions (e.g. "neutral", "somewhat positive").

## File format

The review file should contain one review per line in the format:

`<score> <review text>`

Where `<score>` is an integer from 0-4.
