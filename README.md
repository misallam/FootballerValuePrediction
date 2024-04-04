# FIFA Project README

## Overview

This project explores and analyzes a dataset of FIFA players, providing insights into player statistics, values, clubs, and other attributes. It includes data preprocessing, exploratory data analysis (EDA), and visualization components to uncover interesting patterns and insights about football players featured in the FIFA video game series.

## Installation & Packages

Before you can run the analysis, ensure you have Python installed on your system. Then, install the following packages using pip:

```bash
pip install numpy pandas matplotlib seaborn statsmodels
```

## Dataset

The dataset used in this project is titled `fifa_dataset.csv`. It contains various attributes of football players, including their value, international reputation, skill moves, and club information.

## Key Components

1. **DataFrame Exploration**: Initial exploration of the dataset to understand its structure and content.
2. **Preprocessing**: Steps to clean and prepare the data for analysis. This includes filling null values for several key attributes.
3. **Exploratory Data Analysis (EDA)**: In-depth analysis and visualization of the dataset to uncover insights. A complete presentation of the EDA part is available at: [EDA Presentation](https://www.canva.com/design/DAFvTZHJLBs/f8GkzJZnQegSZi9pes2GuA/edit?utm_content=DAFvTZHJLBs&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton).

## Usage

The notebook is structured to be run from top to bottom. Each cell in the notebook either contains markdown text explaining the step of the analysis or code that performs the analysis and visualization. Simply execute each cell in sequence to reproduce the analysis.

1. **Install the required packages** if you haven't already.
2. **Load and explore the dataset** to become familiar with the data you'll be working with.
3. **Follow the preprocessing steps** to prepare your data for analysis.
4. **Proceed through the EDA** to uncover insights about the FIFA dataset.

## Visualizations

The project includes a variety of visualizations to explore the dataset's characteristics, such as:

- Distribution of player values
- International reputation vs. player value
- Skill moves distribution among players
- Club representation in the dataset

# Advanced Statistics & Normalization
![Value Skwed Distribution](https://github.com/misallam/FootballerValuePrediction/blob/main/Value%20Normal%20Distribution.png) ![Value Normal Distribution](https://github.com/misallam/FootballerValuePrediction/blob/main/Value%20Skwed%20Distribution.png)

The previous visualizations are generated using `matplotlib` and `seaborn` libraries.
