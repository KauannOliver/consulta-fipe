# FIPE Query System

This project was developed to automate the process of retrieving truck information via the FIPE Parallelum API. The system makes multiple requests to various URLs and saves the obtained data to an Excel file, facilitating data analysis and management.

In the company where I work, we handle a large volume of vehicles and their respective plates. To streamline the query process and gather relevant data for each vehicle, I developed a solution that includes:

- **Automated Plate Lookup**: Automated access to the Busca Placas website, reading vehicle plates from the company and saving responses to an Excel file.
- **Data Handling via Excel**: Using queries in Excel, I separated information like make, model, and year-fuel type for each vehicle.
- **URL Generation for the FIPE API**: Based on extracted data, I generated URLs to query the FIPE API and retrieve detailed information for each truck.

**KEY FEATURES**

1. **Automated Requests to the FIPE API**  
   The system automatically queries the FIPE API from a list of URLs generated based on vehicle details (make, model, year, and fuel type).

2. **Exponential Backoff with Retry Mechanism**  
   To avoid request rate limits, the system implements a retry mechanism with exponential backoff. When the rate limit is exceeded, the system waits before retrying.

3. **Excel Export**  
   Data obtained from the FIPE API is organized and exported to an Excel file, enabling easy analysis and storage of truck information.

**TECHNOLOGIES USED**

1. **Python**: Main language used for automation and data handling.
2. **Requests**: Used for making HTTP requests to the FIPE API.
3. **Pandas**: Library used for data manipulation and export to Excel.
4. **Excel**: Used to store and organize extracted vehicle information.

**CONCLUSION**

This project provides an efficient solution for querying large-scale vehicle data via the FIPE API, automating the data request and export process to Excel. With automatic retries and exponential backoff, the system ensures robust and reliable execution, even under high request loads.
