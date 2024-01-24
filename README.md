[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/SGWUF1eE)
# Generic Real Estate Consulting Project

- Group Number: `Group 6`
- Group Member: 
    - [`Rui Li（lrl3@student.unimelb.edu.au) 1237956`]
    - [`Lingxiao Qu(lingxiaoq@student.unimelb.edu.au) 1266391`]
    - [`Jinzhuo Zheng(jinzhuoz@student.unimelb.edu.au) 1261345`]
    - [`Jianing Lu(lujl5@student.unimelb.edu.au) 1079029`]
    - [`Cheng Qian (cqq1@student.unimelb.edu.au) 1266297`]

**Research Goal:** This project aims to offer insightful rental location choices tailored for the middle-aged, elderly, and real estate agents. 

To run the pipeline, please first visit the `scripts` directory and download the data:
- `1 domain_scraping.py`: Python script for scraping domain data include features such as property name, price text etc.
- `4.1 shopping_scraping.py`: Python script for scraping shopping mall data with coordinates.
- `7.1 park_scraping`: Python script for scraping national park data with coordinates.

Then visit the `notebooks` directory and run all notebooks in the following order:  
- `2.1 pre_processing.ipynb`: The data scraped from the domain underwent feature extraction and feature engineering, and was subsequently stored in the `data/raw/domain.csv`.  
- `2.2 outlier_analysis.ipynb`: Conducts outlier analysis by plotting histogram, removes extreme values, and stores the refined data in `data/raw/domain_outliers_removed.csv`.  
- `3.1 shapefile_preprocessing.ipynb`: Preprocessing shapefiles for SA2 and postcode and saving them respectively in the `data/raw/SA2_shapefile` and `data/raw/postcode_shapefile` directories.  
- `3.2 sa2_postcode.ipynb`: Appends an SA2 column to the domain data through postcode matching, then saves the augmented dataset in `data/curated/domain.csv`.  
- `3.3 geoplot_rental_price.ipynb`: This notebook visualizes the geographical distribution of average rental prices for the year 2023 by grouping the data from the domain by SA2 and saving the grouped data in `data/curated/train/rental_price/rental_price_2023.csv`.
- `3.4 geoplot_income.ipynb`: Provides a geographical visualization of the average income distribution in 2019. The income data, grouped by SA2, is saved yearly in `data/curated/train/income_data`.  
- `3.5 geoplot_population.ipynb`: Illustrates the population density of various regions in 2021. The population data, grouped by SA2, is saved yearly in `data/curated/train/population_data`.
- `3.6 geoplot_crime_rate.ipynb`: Displays the crime rate in different regions for 2023. The crime rate data, grouped by SA2, is saved yearly in `data/curated/train/crime_data`.
- `4.2 Shopping_distance.ipynb`:  Utilizes the Openstreetservice API to calculate the straight-line distance from a property to the nearest shopping malls and then determines the driving distance to the three closest malls. The results are stored in `data/raw/shopping_distance`.
- `4.3 ananlysis_shopping_distance.ipynb`: Compile all the driving distances to shopping malls into a single CSV file, stored at `data/raw/merge_requirement/Driving_shop.csv`. Then, visualize the relationship between price and mall distance using scatter plot and boxplot.
- `5.1 School_distance.ipynb`: Calculates the straight-line distance from each property to the nearest school and stores the results in the `data/raw/merge_requirement/Direct_school.csv`.
- `5.2 analysis_school_distance.ipynb`: Analyze the relationship between school straight-line distance and price using the "Log Scatter Plot" and the "Boxplot whether the nearest school is within 4 km".
- `6.1 Train_distance.ipynb`: Calculates the straight-line distance from each property to the nearest train station and stores the results in the `data/raw/merge_requirement/Direct_train.csv`.
- `6.2 analysis_train_distance.ipynb`: Analyze the relationship between train straight-line distance and price using the "Log Scatter Plot" and the "Boxplot whether the nearest train is within 1 km".
- `7.2 Park_distance.ipynb`: Calculates the straight-line distance from each property to the nearest national park and stores the results in the `data/raw/merge_requirement/Direct_park.csv`.
- `7.3 analysis_park_distance.ipynb`: Analyze the relationship between park straight-line distance and price using the "Log Scatter Plot" and the "Boxplot whether the nearest park is within 2 km".
- `8.1 hospital_scraping.ipynb`: scraping all hospital coordinates in victorial and saved in `data/landing/all_hospitals_in_victoria.csv.`
- `8.2 Hospital_distance.ipynb`: Using orsm calculate the closest driving distance to hospital and all saved in folder `data/raw/hospital_distance/`.
- `8.3 analysis_hospital_distance.ipynb`: Compile all the driving distances to hospitals into a single CSV file, stored at `data/raw/merge_requirement/Driving_hospital.csv`. Then, visualize the relationship between price and hospital using scatter plot and boxplot.
- `9.0 merge_analysis.ipynb`: Merges all features and stores them in `data/curated/merged_data.csv`. It also creates heatmap , barchart and uses ANOVA to determine the correlation of these features with price.
- `9.1 rental_external_data.ipynb`: Stores the average rental prices of various regions over the past 20 years, grouped by year, in `data/raw/historial_rental_price_by_suburb.csv`.
- `9.2 suburb_convert_postcode.ipynb`: Converts suburbs to postcodes to ensure data consistency and stores the result in `data/raw/suburb_postcode.csv`.
- `9.3 arima_Model.ipynb`: Implements the ARIMA model to forecast rental prices in a time series manner and calculate the top 10 growth price in the future three years and saved in `data/curated/ARIMA_growth_rate.csv`.
- `10.1 feature_predictions.ipynb`: Predicts the features that influence rental prices for future 3 years and saved them in `data/curated/predict/`.
- `10.2 prepare_modeling_data.ipynb`: Put all the features into one file and save in `data/curated/predict/rental_price` to prepare for the model.
- `10.3 ml_models_prediction.ipynb`: using LR, KNN and random forest for prediction and analysis the results.
- `11.1 combine_results.ipynb`: combine the results of two models using mean and saved top 10 in `data/curated/combined_top10.csv`.
- `12.1 scoring.ipynb`: Using specific weight criterial mark every postcode and choose top 10 livable postcode.


For the visualisations, all plots are stored in the directory `plots`