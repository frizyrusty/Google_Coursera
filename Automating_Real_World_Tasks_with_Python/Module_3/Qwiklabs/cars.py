#!/usr/bin/env python3

# cars.py file

import json
import locale
import sys
import reports
import emails
import os


def load_data(filename):
    """Loads the contents of filename as a JSON file."""
    with open(filename) as json_file:
        data = json.load(json_file)
    return data


def format_car(car):
    """Given a car dictionary, returns a nicely formatted name."""
    return "{} {} ({})".format(car["car_make"], car["car_model"], car["car_year"])


def process_data(data):
    """Analyzes the data, looking for maximums.

    Returns a list of lines that summarize the information.
    """
    max_revenue = {"revenue": 0}
    max_sales = 0
    most_sales_model = ""
    popular_years = {}

    for item in data:
        # Calculate the revenue generated by this model (price * total_sales)
        item_price = locale.atof(item["price"].strip("$"))
        item_revenue = item["total_sales"] * item_price

        if item_revenue > max_revenue["revenue"]:
            max_revenue = {
                "car": item["car"],
                "revenue": item_revenue,
            }

        # Handle max sales
        if item["total_sales"] > max_sales:
            max_sales = item["total_sales"]
            most_sales_model = item["car"]["car_model"]

        # Handle most popular car_year
        car_year = item["car"]["car_year"]
        if car_year in popular_years:
            popular_years[car_year] += item["total_sales"]
        else:
            popular_years[car_year] = item["total_sales"]

    most_popular_year = max(popular_years, key=popular_years.get)

    summary = [
        "The {} generated the most revenue: ${}".format(
            format_car(max_revenue["car"]), max_revenue["revenue"]),
        "The {} has the most sales: {}".format(most_sales_model, max_sales),
        "The most popular year was {} with {} sales.".format(
            most_popular_year, popular_years[most_popular_year]),
    ]

    return summary


def cars_dict_to_table(car_data):
    """Turns the data in car_data into a list of lists."""
    table_data = [["ID", "Car", "Price", "Total Sales"]]
    for item in car_data:
        table_data.append([item["id"], format_car(item["car"]), item["price"], item["total_sales"]])
    return table_data


def main(argv):
    """Process the JSON data and generate a full report out of it."""
    data = load_data("car_sales.json")
    summary = process_data(data)
    print("\n".join(summary))

    # Generate the PDF report
    report_title = "Sales summary for last month"
    additional_info = "<br/>".join(summary)
    table_data = cars_dict_to_table(data)
    reports.generate("/tmp/cars.pdf", report_title, additional_info, table_data)

    # Send the PDF report as an email attachment
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = "Sales summary for last month"
    body = "\n".join(summary)
    attachment_path = "/tmp/cars.pdf"
    message = emails.generate(sender, receiver, subject, body, attachment_path)
    emails.send(message)


if __name__ == "__main__":
    main(sys.argv)
