# **FIPE Query System**

This project automates the retrieval of truck data via the FIPE Parallelum API, streamlining vehicle information management. By making automated API requests and organizing the results in Excel, it ensures efficient handling of large-scale vehicle data for analysis and storage.

---

## **KEY FEATURES**

### 1. **Automated Requests to the FIPE API**
   - Queries the FIPE API using a list of dynamically generated URLs based on vehicle details, including make, model, year, and fuel type.
   - Retrieves detailed information for each truck with minimal manual intervention.

### 2. **Exponential Backoff with Retry Mechanism**
   - Implements a retry mechanism with exponential backoff to handle rate limits and ensure successful data retrieval.
   - Automatically waits and retries when the API rate limit is exceeded, ensuring smooth operation.

### 3. **Excel Export**
   - Organizes the data obtained from the FIPE API into a structured Excel file.
   - Facilitates further analysis, reporting, and storage.

---

## **ADDITIONAL FEATURES IN THE WORKFLOW**

### 1. **Automated Plate Lookup**
   - Uses the *Busca Placas* website to fetch vehicle data based on license plates provided by the company.
   - Saves responses to an Excel file for further processing.

### 2. **Data Handling via Excel**
   - Extracts vehicle details such as make, model, year, and fuel type from the plate lookup data.
   - Generates FIPE API query URLs based on the extracted information.

---

## **TECHNOLOGIES USED**

### 1. **Python**
   - Core programming language for automating API requests and data handling.

### 2. **Requests**
   - Handles HTTP requests to interact with the FIPE API.

### 3. **Pandas**
   - Processes and manipulates data before exporting it to Excel.

### 4. **Excel**
   - Serves as the primary format for organizing and storing retrieved vehicle data.

---

## **HOW IT WORKS**

1. **Plate Data Collection**
   - The system accesses the *Busca Placas* website, automating plate lookups and saving the responses in an Excel file.

2. **URL Generation**
   - Extracted data such as make, model, year, and fuel type is used to generate URLs for querying the FIPE API.

3. **Data Retrieval**
   - The system sends requests to the FIPE API, retrieves truck data, and implements retries with exponential backoff if rate limits are encountered.

4. **Excel Export**
   - Retrieved data is structured and exported to an Excel file, enabling easy analysis and record-keeping.

---

## **CONCLUSION**

The **FIPE Query System** is a robust tool for managing large-scale vehicle data. By automating plate lookups, FIPE API requests, and data exports, it eliminates manual work, reduces errors, and ensures efficient handling of detailed truck information. Its retry mechanism with exponential backoff ensures reliability under high workloads, making it an indispensable tool for companies managing vehicle fleets.
