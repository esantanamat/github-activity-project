# GitHub Activity Tracker

A simple command-line tool to track a GitHub user's activity over the past week. This project uses the GitHub API to fetch the user's recent activity, including commits and repository creations, and displays the data in the terminal.

## Features

- Track commits and created repositories for the past week.
- Display activity with proper grammar handling (singular/plural).
- Command-line interface for easy usage.

## Requirements

- Python 3.x

## Installation

1. Clone the repository or download the code to your local machine.
2. Ensure Python 3.x is installed on your system.
3. No additional dependencies are required, as it uses built-in Python modules (`urllib`, `json`, `datetime`).

## Usage

Run the following command to fetch a GitHub user's activity for the current week:

```bash
python githubactivity.py get-activity <username>
