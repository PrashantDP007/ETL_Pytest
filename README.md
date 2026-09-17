# Python Pytest ETL Testing Framework

## Project Overview

This is a small ETL testing framework built using Python and Pytest.

The framework validates:

- Source-to-target record counts
- Source-to-target data
- NULL values
- Duplicate records
- Transformation logic

## Technology

- Python
- Pytest
- SQLite
- SQL
- Pytest HTML Report

## Project Structure

etl_pytest_framework/

    config/
        config.ini

    db/
        source.db
        target.db

    utils/
        db_utils.py
        queries.py

    tests/
        test_patient_etl.py

    conftest.py
    setup_data.py
    pytest.ini
    requirements.txt

## Setup

Install dependencies:

pip install -r requirements.txt

Create databases:

python setup_data.py

Run tests:

pytest

Generate HTML report:

pytest --html=reports/report.html --self-contained-html