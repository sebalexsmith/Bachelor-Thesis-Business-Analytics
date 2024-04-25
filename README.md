# Bachelor-Thesis-Business-Analytics
The GitHub repository for our bachelor thesis in business analytics.

Group members:
- Lars Nore Moene-Omholt
- Mats Esperum Nielsen
- Olav Andreas Lystrup
- Patrick André Eckbo Vikøren
- Sebastian Alexander Smith

In this repository you will find three folders: Code, Data, and Functions. In addition, our final bachelor thesis as a portable document format (.pdf) file.

Code (Jupyter notebook (6)):
- CleanHousingData.ipynb: Notebook responible for cleaning the raw housing data and merging with macroeconomic data (MacroData.csv and PolicyRate.csv) and coordinate information (PostalCodesWithCoordinates.csv).
- DecisionTreeRegression.ipynb: Notebook responsible for the creation of various decision tree regressors and displaying their results.
- DecriptiveAnalysis.ipynb: Notebook responsible for performing the descriptive analysis.
- LinearRegression.ipynb: Notebook responsible for the creation of singular and multiple regression models and displaying their results.
- RandomForestRegression.ipynb: Notebook responsible for the creation of various random forest regressors and displaying their results.
- VisualizeMacroeconomicData.ipynb: Notebook responsible for visualizing the macroeconomic data collected.

Data (Comma-Separated Values (4), Microsoft Excel Spreadsheet (1)):
- MacroData.csv: Contains macroeconomic factors (CPI, Change CPI, HPI Norway, HPI Trondheim, and Borrowing rate) from January 2021 to Febuary 2024.
- PolicyRate.csv: Contains the daily policy rate from the 4th of January 2021 to the 14th of March 2024.
- PostalCodesWithCoordinates.csv: Contains postal codes in the Trondheim area with their respective latitudes and longitudes.
- TrondheimHousingData.xlsx: Contains the raw, uncleaned housing data acquired from "Heimdal Eiendomsmegling".
- TrondheimHousingDataCleaned.csv: Contains the cleaned housing data merged with the macroeconomic data (MacroData.csv and PolicyRate.csv) and coordinates corresponding to postal codes (PostalCodesWithCoordinates.csv).

Functions (Python (1)):
- Helpers.py: Contains a function (classify_broker(broker: str) -> str) to help in label encoding for the dataset (TrondheimHousingDataCleaned.csv).