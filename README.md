# Fake Data Generator

This project generates synthetic user and purchase data using the `Faker` library.  
The goal is to simulate a simple data pipeline: data generation → CSV output → SQLite storage.  
It demonstrates Python scripting, reproducible data generation, and basic ETL structure useful in data engineering.

## Project Overview

This project is a compact example of a data engineering workflow built using Python.
It demonstrates how synthetic datasets can be generated, structured, and prepared
for downstream analytics or machine-learning work.

The pipeline is simple but follows real-world DE patterns:

1. Generate synthetic users and purchase events using Faker  
2. Store the data in structured CSV files  
3. Load the data into a SQLite database  
4. Make the dataset available for analysis (via notebook or SQL)

The project focuses on:
- reproducible data generation (seeded randomness)
- clean and modular Python code
- clear repository structure following DE best practices
- lightweight ETL-style processing
- preparing data for BI, SQL queries, or ML prototyping

It is designed as a portfolio-friendly example that shows understanding of
data pipelines, file-based storage, and relational databases.

## Business Use Case

A gaming company wants to analyze user behaviour and spending patterns.
However, real production data cannot be shared due to privacy and compliance
constraints (e.g., GDPR).

To support development and testing, the analytics and data engineering teams
need a reproducible synthetic dataset that mimics real user activity.

This project provides:
- synthetic user profiles  
- purchase events with realistic structure  
- reproducible datasets for testing ETL pipelines  
- a small SQLite database for practicing queries  
- a safe, privacy-compliant alternative to production data

The generated data can be used for:
- ETL prototyping  
- BI dashboard development  
- SQL training  
- onboarding new team members  
- demonstrating DE skills in a portfolio

## Project Structure

```
project/
├── data/                # Generated CSV files
├── output/              # SQLite database
├── src/                 # Source code
│   └── generate_data.py
├── README.md
└── requirements.txt
```

## Features

- Synthetic user profiles (UUID, name, age, country)
- Synthetic purchase events (UUID, user reference, item, amount, timestamp)
- Deterministic output (seeded randomness)
- Export to:
  - CSV files (`data/`)
  - SQLite database (`output/database.db`)
- Clean, modular Python script (`src/generate_data.py`)

## Installation

Install required dependencies:
pip install -r requirements.txt

If `pip` is not recognized, use:
python -m pip install -r requirements.txt

## Usage

Run the generator:

After running the script, you will find:

- `users.csv` and `purchases.csv` in the `data/` folder
- `database.db` in the `output/` folder

## Example Output

### Sample user record:
{
"user_id": "d9a4d0b2-1a9f-4e70-8d60-98e91e4b5e32",
"name": "John Doe",
"age": 32,
"country": "Germany"
}

### Sample purchase record:
{
"purchase_id": "7bb89c87-66ac-4471-9a41-0f042819c58d",
"user_id": "<"d9a4d0b2-1a9f-4e70-8d60-98e91e4b5e32"",
"item": "Gold Pack",
"amount": 49.99,
"timestamp": "2025-01-14 12:43:21"
}

## Analysis Notebook

An example exploratory analysis is available in `analysis.ipynb`.

It demonstrates how the generated data can be:
- loaded from CSV files,
- joined into an analytical dataset,
- used to compute key metrics,
- visualized using matplotlib.

This step illustrates how downstream teams (analytics/BI) can consume
the data produced by the pipeline.

## Tech Stack

- Python 3.14
- Faker
- Pandas
- SQLite3

## License

MIT License

## Created By
Michał Kaczmarek