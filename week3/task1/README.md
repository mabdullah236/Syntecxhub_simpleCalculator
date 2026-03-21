```markdown
# CSV to Excel Converter & Data Cleaner

A robust Python CLI tool designed to automate the process of converting CSV files into formatted Excel workbooks. This tool
includes built-in data cleaning logic and column mapping specifically for industry dataset processing.

# Features
- **Automated Conversion:** Converts large CSV files to `.xlsx` format seamlessly.
- **Smart Data Cleaning:** - Automatically fills missing (NaN) values.
    - Replaces empty text with `"N/A"`.
    - Replaces missing numbers with `0`.
- **Column Mapping:** Automatically renames `Industry_code_ANZSIC06` to a simpler `Code` header.
- **Date Standardization:** Attempts to parse and fix `Survey-date` columns automatically.
- **Logging & Error Handling:** Provides real-time feedback and detailed error reports during the conversion process.
---

# Prerequisites
Make sure you have Python installed, then install the required dependencies:
```bash
pip install pandas openpyxl
```
---

# How to Use
Run the script from your terminal by providing the input CSV path and the desired output Excel path:
```bash
python script_name.py --input "data.csv" --output "cleaned_data.xlsx"
```

# Arguments:
| Argument | Description | Required |
| :--- | :--- | :--- |
| `--input` | Path to the source CSV file. | Yes |
| `--output` | Path where the Excel file will be saved. | Yes |
---

# Logic Flow
1. **Load:** Reads CSV with `low_memory=False` to handle mixed data types.
2. **Clean:** Iterates through columns to handle null values based on data type (Object vs Numeric).
3. **Transform:** Renames specific industry columns and standardizes date formats.
4. **Export:** Saves the final cleaned dataframe to an Excel file without the index.
---

# Error Handling
- **File Access:** Validates if the input file exists and is readable.
- **Date Parsing:** Uses `errors="coerce"` to ensure the script doesn't crash on invalid date formats.
- **System Exit:** Gracefully stops execution if the input file cannot be loaded, preventing further errors.
