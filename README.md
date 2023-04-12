# Movie-Recommendation-System
This is a simple movie recommendation system that suggests movies to users based on their preferences. The system is built using Python and utilizes the bag-of-words algorithm and cosine similarity model for machine learning.

### Note: This repo doesn't contain dataset and model file Because we cannot upload more than 25 MB data on GitHub so kindly download the dataset from the Dataset section below and model file from the below link
Model Link: https://drive.google.com/file/d/1CEcORiagbVc9H8ymDJUl2BCC03TFrhN3/view?usp=share_link

![alt text](https://github.com/iamrahul-9/Movie-Recommendation-System/blob/main/MRS%201.png)
![alt text](https://github.com/iamrahul-9/Movie-Recommendation-System/blob/main/MRS%202.png)
![alt text](https://github.com/iamrahul-9/Movie-Recommendation-System/blob/main/MRS%203.png)

## How it Works
The recommendation system uses content-based filtering, collaborative filtering, and hybrid filtering techniques to generate recommendations. The bag-of-words algorithm is used to represent movie plots as a vector of words, and the cosine similarity model is used to measure the similarity between movie plots.

## Dataset
The dataset used for this project is the IMDb dataset, which I took from kaggle.com.
Dataset Link: https://www.kaggle.com/datasets/akshaypawar7/millions-of-movies

## Setup
To run the recommendation system, you'll need Python 3.x and the following Python libraries:

1. streamlit
2. pickle

Just run the following code in terminal

```pip install streamlit, pickle```

## Usage
To use the recommendation system, simply run the ```streamlit run main.py``` in cmd. The system will prompt the user to input any movie name, and then generate a list of top 5 similar movies.

## Conclusion
This movie recommendation system is a simple example of how machine learning can be used to personalize user experiences. It can be improved and scaled for larger datasets, and can be applied to other industries such as e-commerce and music streaming
