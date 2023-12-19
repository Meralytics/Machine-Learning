## Overview

This project aims to classify news articles as either reliable or unreliable using a machine learning model. The code utilizes the scikit-learn library for building a Decision Tree Classifier and NLTK for natural language processing tasks.

## Data Loading and Preprocessing

The project starts by loading a dataset (train.csv) using the Pandas library.
Descriptive statistics and information about the dataset are displayed, including summary statistics and column details.
Null values in the dataset are handled by filling them with empty strings.
Text Preprocessing

The NLTK library is used for text preprocessing, including removing non-alphabetic characters, converting to lowercase, and stemming.
The processed text data is then split into features (x) and labels (y).

## Model Training

The dataset is split into training and testing sets using the train_test_split function from scikit-learn.
The text data is transformed into numerical features using TF-IDF vectorization.
A Decision Tree Classifier is trained on the training data.

## Model Evaluation

The trained model is used to make predictions on the test set.
The accuracy of the model on the test set is calculated.

## Model Persistence

The TF-IDF vectorizer and the trained Decision Tree model are saved using the joblib library.

## Inference

A function, fake_news, is defined to take a news article as input, preprocess it, and use the trained model to predict its reliability.
An example news article is provided, and the result is printed as either "reliable" or "unreliable."

## Usage

Ensure you have the required libraries installed (pandas, nltk, scikit-learn).
Run the provided code in a Jupyter environment or as a Python script.
Use the fake_news function to classify the reliability of news articles.

## Files

train.csv: The dataset containing news articles and their labels.
vector.joblib: Saved TF-IDF vectorizer.
model.joblib: Saved Decision Tree Classifier model.
