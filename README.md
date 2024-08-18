# Forum Enhancement Project

In collaboration with (Marina Gómez Rey)[https://github.com/MarinaGRey], Sara Piñas and Ángela Durán.
Subject: Machine Learning Applications
Grade: 10/10

## Introduction
Welcome to the Forum Enhancement project! In the digital age, enhancing user interaction on forum platforms is crucial for boosting engagement and user satisfaction. This project aims to tackle the challenges of organizing and extracting meaningful insights from diverse forum data. By leveraging various data analysis techniques and incorporating emojis to express sentiments, this project enhances forum functionality and user experience.

## Objective
The primary objective of this project is to refine forum data using advanced analytical methods to improve user interaction and engagement. This involves:
- Using clustering, sentiment analysis, topic modeling, and recommendation systems to analyze and enrich forum data.
- Incorporating emojis to convey emotions and sentiments more effectively.
- Developing a pipeline to provide recommendations and insights based on user interactions.

## Repository Structure
The repository is organized as follows:

- **Data/**: Contains datasets and model files.
  - `best_kmeans_model_15.pkl`: Pre-trained KMeans clustering model.
  - `doc_topics.txt`: Topic distribution for documents.
  - `emojis_faces.csv`: Emoji face data.
  - `emojis_sentiment_new_scale.csv`: Emoji sentiment scale data.
  - `forum_final.csv`: Final processed forum dataset.

- `Notebook_final_project_ML.ipynb`: Jupyter Notebook containing the main machine learning code and analysis.
- `report_final.pdf`: Comprehensive project report detailing the methodology, results, and conclusions.
- `scrap_all.py`: Python script for web scraping to collect data.

## Tasks Overview
1. **Data Collection**:
   - Web scraping techniques were employed to gather forum data and related information.

2. **Text Preprocessing and Vectorization**:
   - Implemented preprocessing pipelines for text data.
   - Explored various vectorization strategies, including TF-IDF, GloVe, and LDA, with detailed rationale for each choice.
   - Applied dimensionality reduction techniques to enhance model performance.

3. **Machine Learning Model: Clustering**:
   - Applied clustering algorithms to segment forum data.
   - Determined the optimal number of clusters and interpreted the results.
   - Conducted sentiment analysis and topic modeling for emoji recommendation.
   - Mapped topics to emoji subsets to provide relevant recommendations.

4. **Dashboard**:
   - Developed a pipeline for recommending emojis based on sentiment analysis of new text inputs.
   - Created a user-friendly dashboard for visualizing recommendations and insights.

## Conclusion
This project demonstrates the effective use of clustering, sentiment analysis, topic modeling, and recommendation systems to enhance forum data management and user engagement. By integrating emojis and advanced analytics, we provide a more interactive and visually appealing forum experience.

For more details, please refer to the `report_final.pdf` and explore the Jupyter Notebook for in-depth analysis and code implementation.
