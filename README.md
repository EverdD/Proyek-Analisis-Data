## Air Quality Index Dashboard :cloud:

This dashboard provides insights into air quality data, helping users visualize and understand trends in air quality over time. It utilizes data analysis techniques and visualization tools to present information in an accessible and informative manner.

### Features:
- **Best & Worst Air Quality Index (AQI):** Displays the top 5 stations with the best and worst AQI, allowing users to quickly identify areas of concern.
- **Average Climate Variables:** Shows the average temperature, pressure, dew point, and wind speed, providing an overview of the prevailing climate conditions.
- **Air Quality Index by Time:** Analyzes AQI trends over different time intervals (year, month, day, hour), helping users identify patterns and correlations.

### Technologies Used:
- **Python Libraries:** NumPy, Pandas, Matplotlib, Seaborn, Streamlit
- **Data Processing:** Data filtering, aggregation, and visualization techniques are employed to generate meaningful insights.
- **Streamlit:** A user-friendly framework for building interactive web applications with Python.

### How to Run:
1. **Environment Setup:**
   - Create a Conda environment with Python 3.11.
   - Activate the environment and install required libraries using pip.
   ```
   conda create --name main-ds python=3.11
   conda activate main-ds
   pip install numpy pandas scipy matplotlib seaborn jupyter streamlit
   ```

2. **Run Streamlit App:**
   - Execute the Streamlit app using the command:
   ```
   streamlit run dashboard.py
   ```

### Data Sources:
- Air Quality Index (AQI) data is sourced from https://drive.google.com/file/d/1RhU3gJlkteaAQfyn9XOVAz7a5o1-etgr/view?usp=share_link.
- Climate variables data is obtained from Air Quality Index (AQI) data

### Contribution Guidelines:
- Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

### Contributors:
- Firman Nurcahyo

### License:
- This project is licensed under the [Dicoding Academy]. Feel free to use and modify the code as per the terms of the license.

### Contact Information:
- For any inquiries or feedback, please contact [firman,cahyo.369@gmail.com].

Let's keep our air clean and healthy! :seedling:
