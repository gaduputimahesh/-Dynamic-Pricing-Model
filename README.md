# Dynamic Pricing Model for E-Commerce with Reinforcement Learning

## Project Overview
This project demonstrates the implementation of a **dynamic pricing model** using **Reinforcement Learning (RL)**, specifically **Q-learning**, to optimize pricing strategies for e-commerce platforms. By adjusting prices based on factors like customer demand, competitor pricing, and other market variables, the model aims to maximize revenue through continual learning.

The goal is to train a model that dynamically adjusts prices based on historical and environmental data, helping businesses optimize their pricing strategies for higher revenue.

## Key Features
- **Data Preprocessing:** Includes data cleaning, handling missing values, and feature scaling to prepare raw data for modeling.
- **Reinforcement Learning Model:** Uses **Q-learning** to determine the optimal price for each situation based on market conditions.
- **Evaluation:** Compares the performance of RL-based pricing strategies with fixed pricing methods by tracking the generated revenue.

## Dataset
The dataset used in this project simulates a ride-hailing scenario and contains the following features:
- `Number_of_Riders`: Number of riders requesting rides.
- `Number_of_Drivers`: Number of available drivers in the area.
- `Location_Category`: Location type (Urban, Suburban, Rural).
- `Customer_Loyalty_Status`: Customer loyalty category (Silver, Regular).
- `Number_of_Past_Rides`: Number of rides taken by the customer.
- `Average_Ratings`: Average rating of the customer.
- `Time_of_Booking`: Time of day when the booking was made (Morning, Afternoon, Evening, Night).
- `Vehicle_Type`: Type of vehicle requested (Economy, Premium).
- `Expected_Ride_Duration`: Estimated ride time (in minutes).
- `Historical_Cost_of_Ride`: Previous cost for the ride.

### Handling Missing Data:
- **Numerical Columns:** Filled with the mean of the respective columns.
- **Categorical Columns:** Filled with the mode (most frequent value).

## Installation Instructions

### Clone the Repository
Clone this repository to your local machine:
```bash
git clone https://github.com/gaduputimahesh/-Dynamic-Pricing-Model.git
cd Dynamic-Pricing-Model

