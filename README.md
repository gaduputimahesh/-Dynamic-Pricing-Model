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

# Usage:
Data Preprocessing: Prepares the data by cleaning and scaling.
![Screenshot (179)](https://github.com/user-attachments/assets/b5013afb-cba8-4f70-9980-36f58fc83100)
![Screenshot (181)](https://github.com/user-attachments/assets/59d46229-9c3d-43ec-b3bb-62d5dd40f722)
![Screenshot (182)](https://github.com/user-attachments/assets/f4d8083f-5c40-4fca-934a-991766e0fef0)
![Screenshot (183)](https://github.com/user-attachments/assets/b07129e7-f3bb-421f-b0e0-3a4bf1d4e2b1)




# Model Training:  
Implements the Q-learning algorithm to adjust prices dynamically.
# Evaluation:
Compares the performance of RL-based pricing strategies with traditional pricing models.
Total Revenue: 75817.50
![download](https://github.com/user-attachments/assets/df89b75a-08d9-427e-bc1f-5e4ee5e64440)

The model shows improvement over time as it learns from the data, with total revenue increasing as the pricing strategy becomes more optimized. 
# output: 
Episode 0, Total Revenue: $63,388
Episode 100, Total Revenue: $70,617



# Conclusion:
The project successfully uses reinforcement learning to implement a dynamic pricing model that maximizes revenue over time. The approach is highly effective in competitive e-commerce markets and can be adapted to various industries with similar pricing needs

