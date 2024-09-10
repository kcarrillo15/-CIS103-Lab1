# --------------------------------------------------------
# Lab 1: Getting Started with Python
# CIS 103: Introduction to Programming
# Instructor: [Your Name]
# Student Name: [Your Name]
# Date: [Today's Date]
# Description:
# This script prints a personalized greeting message
# and demonstrates the use of variables and basic data types.
# --------------------------------------------------------
# Get the user's name (string) and age (integer)
name = input("Enter your name: ")
age = int(input("Enter your age: "))
# Calculate the year the user was born
current_year = 2024
birth_year = current_year - age
# Print a personalized greeting message
print(f"Hello, {name}! You were born in {birth_year}.")