# -----------------------------------------------------------------------------
# SQL QUERY DEFINITIONS FOR ETL VALIDATION
# -----------------------------------------------------------------------------
# This file was created to keep all SQL statements in one central place instead
# of writing raw queries directly inside test files or application logic.
#
# Why this file exists:
# 1. Reusability: the same validation queries can be used by multiple tests.
# 2. Maintainability: SQL logic is stored in one place, making updates easier.
# 3. Readability: tests remain clean and focused on assertions instead of SQL.
# 4. Consistency: every ETL validation uses the same query logic and naming.
#
# This file is used in ETL testing to compare data between a source system and a
# target system. The queries here help validate:
# - whether row counts match
# - whether records are missing
# - whether null values appear in keys
# - whether duplicates exist
# - whether data mismatches exist after transformation
# - whether calculated values like totals are correct
#
# SQL syntax used in this file and what it means:
# - SELECT: chooses the columns or expressions to return.
# - COUNT(*): counts the number of rows in a result set.
# - FROM: specifies the table to read from.
# - JOIN: combines rows from two tables based on a matching condition.
# - LEFT JOIN: keeps all rows from the left table and matches rows from the right
#   table where available. If no match exists, it returns NULLs for right-side
#   columns.
# - ON: defines the matching condition in a JOIN.
# - WHERE: filters rows before or after the join, based on conditions like
#   equality, inequality, or NULL checks.
# - IS NULL: checks whether a column has no value.
# - GROUP BY: groups rows with the same values in one or more columns.
# - HAVING: filters grouped data after aggregation, similar to WHERE but for
#   aggregated results.
# - AS: renames a column or expression in the output.
# - <>: means "not equal to" in SQL.
#
# Example:
# SELECT COUNT(*) FROM patient
# This returns the total number of rows in the patient table.
#
# Example:
# LEFT JOIN patient t ON s.patient_id = t.patient_id
# This compares source and target records by patient_id and keeps all source rows,
# even if there is no matching target row.
#
# Example:
# GROUP BY patient_id HAVING COUNT(*) > 1
# This finds duplicate patient IDs by grouping identical IDs and keeping only those
# with more than one row.
# -----------------------------------------------------------------------------

# -------------------------
# SOURCE QUERIES
# -------------------------

SOURCE_PATIENT_COUNT = """
SELECT COUNT(*)
FROM patient
"""


# -------------------------
# TARGET QUERIES
# -------------------------

TARGET_PATIENT_COUNT = """
SELECT COUNT(*)
FROM patient
"""


# -------------------------
# MISSING RECORDS
# -------------------------

MISSING_PATIENTS = """
SELECT s.patient_id
FROM patient s
LEFT JOIN patient t
    ON s.patient_id = t.patient_id
WHERE t.patient_id IS NULL
"""


# -------------------------
# NULL VALIDATION
# -------------------------

TARGET_NULL_PATIENTS = """
SELECT *
FROM patient
WHERE patient_id IS NULL
"""


# -------------------------
# DUPLICATE VALIDATION
# -------------------------

TARGET_DUPLICATE_PATIENTS = """
SELECT patient_id, COUNT(*)
FROM patient
GROUP BY patient_id
HAVING COUNT(*) > 1
"""


# -------------------------
# DATA MISMATCH
# -------------------------

PATIENT_DATA_MISMATCH = """
SELECT
    s.patient_id,
    s.name AS source_name,
    t.name AS target_name,
    s.city AS source_city,
    t.city AS target_city
FROM source_patient s
JOIN target_patient t
    ON s.patient_id = t.patient_id
WHERE s.name <> t.name
   OR s.city <> t.city
"""


# -------------------------
# TRANSFORMATION VALIDATION
# -------------------------

CLAIM_AMOUNT_MISMATCH = """
SELECT
    claim_id,
    quantity,
    unit_price,
    total_amount
FROM claims
WHERE total_amount <> quantity * unit_price
"""

####
SOURCE_PATIENTS = """
SELECT patient_id, name, city
FROM patient
ORDER BY patient_id
"""

TARGET_PATIENTS = """
SELECT patient_id, name, city
FROM patient
ORDER BY patient_id
"""

# Fetch Patient IDs from the source.

SOURCE_PATIENT_IDS = """
SELECT patient_id
FROM patient
ORDER BY patient_id
"""

# Fetch Patient IDs from the target.
TARGET_PATIENT_IDS = """
SELECT patient_id
FROM patient
ORDER BY patient_id
"""