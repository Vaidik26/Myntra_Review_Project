## 🛍️ Myntra Product Scraper & Analyzer

A Python-based project that scrapes reviews from Myntra, stores the data in MongoDB, and provides insightful analysis to understand customer feedback better.

## 📝 Project Goal

The primary objective of this project is to automate the process of extracting customer reviews from Myntra's website and analyzing the data to identify trends, sentiments, and potential areas for improvement.

## 📂 Data Details

The project extracts the following details for each product review:

Reviewer Name: Name of the customer.
Review Rating: Numerical rating given by the customer.
Review Text: Detailed feedback from the customer.
Review Date: Date when the review was posted.
Product Details: Title, price, and other specifications of the product.

## 🛠️ Installation and Setup

# 1. Clone the Repository:

bash
git clone https://github.com/Vaidik26/Myntra_Review_Project.git  
cd Myntra_Review_Project  

# 2. Set up a Virtual Environment:

bash
python -m venv env  
source env/bin/activate  # On Windows: env\Scripts\activate  

# 3. Install Dependencies:

bash
pip install -r requirements.txt  

# 4. Set up MongoDB:

Ensure MongoDB is installed and running on your local machine or server.
Configure the connection details in the code.

## 5. Run the Scraper:

Use the provided scripts to extract and analyze reviews:

bash
python app.py  

## 🚀 Usage

# Scrape Reviews:

Use Selenium to extract data from the Myntra website dynamically.

# Store Data:

All extracted reviews are saved in a MongoDB database for efficient retrieval and storage.

# Analyze Reviews:

Use the Jupyter notebook (myntra.ipynb) or generate_analysis.py for analysis and visualizations.

## 📁 Project Structure

Myntra_Review_Project/  
│  
├── env/                     # Virtual environment directory (ignored in .gitignore)  
├── src/  
│   ├── pages/               # Selenium-based page objects for scraping  
│   ├── static/              # Static files for analysis  
│   ├── templates/           # HTML templates (if applicable)  
│   ├── exception.py         # Custom exception handling module  
│   ├── app.py               # Main script to run the scraper  
│   └── generate_analysis.py # Script for analyzing the scraped data  
├── data.csv                 # Sample dataset exported from MongoDB  
├── README.md                # Project documentation  
├── requirements.txt         # List of dependencies  
├── setup.py                 # Package setup file (if necessary for distribution)  
└── myntra.ipynb             # Notebook for exploratory data analysis  

## 🔍 Analysis Features

Sentiment analysis of reviews.

Visualization of review trends (e.g., ratings over time).

Key insights from product feedback.

## 📜 License

This project is licensed under the MIT License.

## 👥 Contact

For any questions or suggestions, feel free to reach out:

Email: vaidiky90@gmail.com

Stored high-volume review data in MongoDB, ensuring efficient data management and scalability.
Conducted data analysis using Python and pandas to identify customer sentiment trends and generate actionable insights.
Visualized insights through Jupyter notebooks, enabling improved understanding of customer feedback and review patterns.
Designed modular and reusable code architecture, enhancing maintainability and scalability for future extensions.
GitHub Repository: Myntra Review Project
