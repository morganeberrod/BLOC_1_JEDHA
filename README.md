# Project Plan your trip with Kayak

## Project 🚧
The marketing team needs help on a new project. After doing some user research, the team discovered that 70% of their users who are planning a trip would like to have more information about the destination they are going to.

In addition, user research shows that people tend to be defiant about the information they are reading if they don't know the brand which produced the content.

Therefore, Kayak Marketing Team would like to create an application that will recommend where people should plan their next holidays. The application should be based on real data about:

- Weather
- Hotels in the area

The application should then be able to recommend the best destinations and hotels based on the above variables at any given time.

## Goals 🎯
As the project has just started, your team doesn't have any data that can be used to create this application. Therefore, your job will be to:

- Scrape data from destinations
- Get weather data from each destination
- Get hotels' info about each destination
- Store all the information above in a data lake
- Extract, transform and load cleaned data from your datalake to a data warehouse

## Data

There are 3 files in the results folder:
- city_forecast_weather.csv : get the weather from an API (https://openweathermap.org/appid)
- hotels.json : result of scraping Booking website (www.booking.com)
- hotels_information.csv : pandas dataframe transformed in csv after cleaning 

## Authors

**Morgane BERROD** - [MorganeBD](https://github.com/morganeberrod)
