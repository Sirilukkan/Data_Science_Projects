
# AWS SageMaker Classification Deployment

## Overview

This projects contains two distinct machine learning projects focused on deploying classification models using AWS SageMaker. The projects are designed to address real-world problems in visa approval prediction and hotel reservation cancellation prediction. Both projects leverage AWS SageMaker for efficient model deployment and pipeline management.

## Projects

### 1. Visa Approval Prediction

#### Problem Statement
The United States faces a significant challenge in efficiently processing visa applications due to the increasing volume of applicants each year. EasyVisa, hired by the Office of Foreign Labor Certification (OFLC), aims to develop a machine learning solution to assist in shortlisting candidates with a higher chance of visa approval.

#### Dataset Description
The dataset includes various attributes related to the employee and employer:
- **case_id:** ID of each visa application
- **continent:** Continent information of the employee
- **education_of_employee:** Employee's education details
- **has_job_experience:** Whether the employee has job experience (Y/N)
- **requires_job_training:** Whether the employee requires job training (Y/N)
- **no_of_employees:** Number of employees in the employer's company
- **yr_of_estab:** Year the employer's company was established
- **region_of_employment:** Intended region of employment in the US
- **prevailing_wage:** Average wage for similar positions in the employment area
- **unit_of_wage:** Unit of the prevailing wage (Hourly, Weekly, Monthly, Yearly)
- **full_time_position:** Whether the position is full-time (Y/N)
- **case_status:** Flag indicating if the visa was certified or denied

### 2. Hotel Reservation Cancellation Prediction

#### Problem Statement
The INN Hotels Group is experiencing a high number of booking cancellations, impacting their revenue and resource management. The goal is to develop a machine learning model to predict cancellations and help formulate effective cancellation policies to increase profitability.

#### Dataset Description
The dataset includes various attributes related to hotel bookings:
- **Booking_ID:** Unique identifier of each booking
- **no_of_adults:** Number of adults
- **no_of_children:** Number of children
- **no_of_weekend_nights:** Number of weekend nights booked
- **no_of_week_nights:** Number of week nights booked
- **type_of_meal_plan:** Type of meal plan selected (Not Selected, Meal Plan 1, Meal Plan 2, Meal Plan 3)
- **required_car_parking_space:** Whether a car parking space is required (0 - No, 1 - Yes)
- **room_type_reserved:** Type of room reserved (encoded)
- **lead_time:** Number of days between booking and arrival
- **arrival_year:** Year of arrival date
- **arrival_month:** Month of arrival date
- **arrival_date:** Date of the month
- **market_segment_type:** Market segment designation
- **repeated_guest:** Whether the customer is a repeated guest (0 - No, 1 - Yes)
- **no_of_previous_cancellations:** Number of previous bookings canceled by the customer
- **no_of_previous_bookings_not_canceled:** Number of previous bookings not canceled by the customer
- **avg_price_per_room:** Average price per day of the reservation (in euros)
- **no_of_special_requests:** Total number of special requests made by the customer
- **booking_status:** Flag indicating if the booking was canceled

## Getting Started

### Prerequisites
- AWS Account
- AWS SageMaker; Launching Studio to use jupyter notebook
- Python 3.x
- Jupyter Notebook

## Acknowledgements

These projects were completed as part of the Boostcamp program called "Data Science with AWS" from Great Learning. I would like to extend my gratitude to the instructors and peers who provided valuable insights and support throughout the program. Special thanks to the team at Great Learning for designing a comprehensive curriculum that enabled me to develop and deploy these machine-learning models using AWS SageMaker. 
