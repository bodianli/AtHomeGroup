import os
import pandas as pd

Final_Data = pd.read_csv("..\Week_1_CollectData\Final_Data.csv",
                         encoding="UTF-8",
                         )

# https://data.world/niccolley/us-zipcode-to-county-state/workspace/file?filename=ZIP-COUNTY-FIPS_2010-03.csv
Zip_Convert = pd.read_csv("ZIP-COUNTY-FIPS_2010-03.csv",
                          encoding="UTF-8",
                          usecols=["ZIP", "STCOUNTYFP"]
                          )

# 1. Join Income Data
# https://covid19.census.gov/datasets/income-and-benefits-counties/data?geometry=-147.235%2C28.725%2C-13.729%2C51.806
Income_Data = pd.read_csv("Income_and_Benefits_-_Counties.csv",
                          encoding="UTF-8"
                          )
column_name_Income_Data = [
                           "FIPS_CODE",
                           "Total Households",
                           "Total Households *margin of error",
                           "Total Households with Income - less than $10,000",
                           "Total Households with Income - less than $10,000 *margin of error",
                           "Total Households with Income - $10,000 to $14,999",
                           "Total Households with Income - $10,000 to $14,999 *margin of error",
                           "Total Households with Income - $15,000 to $24,999",
                           "Total Households with Income - $15,000 to $24,999 *margin of error",
                           "Total Households with Income - $25,000 to $34,999",
                           "Total Households with Income - $25,000 to $34,999 *margin of error",
                           "Total Households with Income - $35,000 to $49,999",
                           "Total Households with Income - $35,000 to $49,999 *margin of error",
                           "Total Households with Income - $50,000 to $74,999",
                           "Total Households with Income - $50,000 to $74,999 *margin of error",
                           "Total Households with Income - $75,000 to $99,999",
                           "Total Households with Income - $75,000 to $99,999 *margin of error",
                           "Total Households - with Supplemental Security Income",
                           "Total Households - with Supplemental Security Income *margin of error",
                           "Total Households - with cash public assistance income",
                           "Total Households - with cash public assistance income *margin of error",
                           "Total Households - with Food Stamp/SNAP benefits in the past 12 months",
                           "Total Households - with Food Stamp/SNAP benefits in the past 12 months *margin of error",
                           "Percent of Households whose income in the past 12 months was less than $75,000",
                           "Total Households with Income - less than $75,000",
                           "Total Households with Income - less than $75,000 * margin of error",
                           "Households: Receiving Food Stamps/SNAP (%)",
                           "Households: Receiving Food Stamps/SNAP (%) *margin of error"]
data_income_clean = pd.DataFrame(data=Income_Data.iloc[:, 4:])
data_income_clean.columns = column_name_Income_Data
# Join income data with ZIP table
data_income_with_zip = pd.merge(Zip_Convert,
                                data_income_clean,
                                how="left",
                                left_on="STCOUNTYFP",
                                right_on="FIPS_CODE").groupby('ZIP').sum()

# 2. Join Race Data
# https://covid19.census.gov/datasets/race-and-ethnicity-county/data
Ethic_Data = pd.read_csv("Race_and_Ethnicity_-_County.csv",
                         encoding="UTF-8"
                         )

column_name_Ethic_Data = [
                          "FIPS_CODE",
                          "Total Population - White alone",
                          "Total Population - White alone *margin of error",
                          "Total Population - Black or African American alone",
                          "Total Population - Black or African American alone *margin of error",
                          "Total Population - American Indian and Alaska Native alone",
                          "Total Population - American Indian and Alaska Native alone *margin of error",
                          "Total Population - Asian alone",
                          "Total Population - Asian alone *margin of error",
                          "Total Population - Native Hawaiian and Other Pacific Islander alone",
                          "Total Population - Native Hawaiian and Other Pacific Islander alone *margin of error",
                          "Total Population - Some other race alone",
                          "Total Population - Some other race alone *margin of error",
                          "Total Population - Two or more races",
                          "Total Population - Two or more races *margin of error",
                          "Total Population - Not Hispanic or Latino",
                          "Total Population - Not Hispanic or Latino *margin of error",
                          "Total Population - Hispanic or Latino (of any race)",
                          "Total Population - Hispanic or Latino (of any race) *margin of error"]
data_ethic_clean = pd.DataFrame(data=Ethic_Data.iloc[:, 4:])
data_ethic_clean.columns = column_name_Ethic_Data
# Join ethic data with ZIP table
data_ethic_with_zip = pd.merge(Zip_Convert,
                               data_ethic_clean,
                               how="left",
                               left_on="STCOUNTYFP",
                               right_on="FIPS_CODE").groupby('ZIP').sum()



# 3. Join ACS Data
LaborForce_Data = pd.read_csv("ACS_Labor_Force_Participation_by_Age_-_County.csv",
                              encoding="UTF-8")
column_name_Labor_Data = [
                          "FIPS_CODE",
                          "Area of Land (Square Meters)",
                          "Area of Water (Square Meters)",
                          "Name",
                          "State",
                          "Total population age 16 and over",
                          "Total population age 16 and over - Margin of Error",
                          "Population age 16 to 19 years",
                          "Population age 16 to 19 years - Margin of Error",
                          "Population age 16 to 19 years who worked in the past 12 months",
                          "Population age 16 to 19 years who worked in the past 12 months - Margin of Error",
                          "Population age 16 to 19 years who worked in the past 12 months, full-time, year-round",
                          "Population age 16 to 19 years who worked in the past 12 months, full-time, year-round - Margin of Error",
                          "Population age 16 to 19 years who worked in the past 12 months, less than full-time, year-round",
                          "Population age 16 to 19 years who worked in the past 12 months, less than full-time, year-round - Margin of Error",
                          "Population age 16 to 19 years who did not work in the past 12 months",
                          "Population age 16 to 19 years who did not work in the past 12 months - Margin of Error",
                          "Population age 20 to 24 years",
                          "Population age 20 to 24 years - Margin of Error",
                          "Population age 20 to 24 years who worked in the past 12 months",
                          "Population age 20 to 24 years who worked in the past 12 months - Margin of Error",
                          "Population age 20 to 24 years who worked in the past 12 months, full-time, year-round",
                          "Population age 20 to 24 years who worked in the past 12 months, full-time, year-round - Margin of Error",
                          "Population age 20 to 24 years who worked in the past 12 months, less than full-time, year-round",
                          "Population age 20 to 24 years who worked in the past 12 months, less than full-time, year-round - Margin of Error",
                          "Population age 20 to 24 years who did not work in the past 12 months",
                          "Population age 20 to 24 years who did not work in the past 12 months - Margin of Error",
                          "Population age 25 to 44 years",
                          "Population age 25 to 44 years - Margin of Error",
                          "Population age 25 to 44 years who worked in the past 12 months",
                          "Population age 25 to 44 years who worked in the past 12 months - Margin of Error",
                          "Population age 25 to 44 years who worked in the past 12 months, full-time, year-round",
                          "Population age 25 to 44 years who worked in the past 12 months, full-time, year-round - Margin of Error",
                          "Population age 25 to 44 years who worked in the past 12 months, less than full-time, year-round",
                          "Population age 25 to 44 years who worked in the past 12 months, less than full-time, year-round - Margin of Error",
                          "Population age 25 to 44 years who did not work in the past 12 months",
                          "Population age 25 to 44 years who did not work in the past 12 months - Margin of Error",
                          "Population age 45 to 54 years",
                          "Population age 45 to 54 years - Margin of Error",
                          "Population age 45 to 54 years who worked in the past 12 months",
                          "Population age 45 to 54 years who worked in the past 12 months - Margin of Error",
                          "Population age 45 to 54 years who worked in the past 12 months, full-time, year-round",
                          "Population age 45 to 54 years who worked in the past 12 months, full-time, year-round - Margin of Error",
                          "Population age 45 to 54 years who worked in the past 12 months, less than full-time, year-round",
                          "Population age 45 to 54 years who worked in the past 12 months, less than full-time, year-round - Margin of Error",
                          "Population age 45 to 54 years who did not work in the past 12 months",
                          "Population age 45 to 54 years who did not work in the past 12 months - Margin of Error",
                          "Population age 55 to 64 years",
                          "Population age 55 to 64 years - Margin of Error",
                          "Population age 55 to 64 years who worked in the past 12 months",
                          "Population age 55 to 64 years who worked in the past 12 months - Margin of Error",
                          "Population age 55 to 64 years who worked in the past 12 months, full-time, year-round",
                          "Population age 55 to 64 years who worked in the past 12 months, full-time, year-round - Margin of Error",
                          "Population age 55 to 64 years who worked in the past 12 months, less than full-time, year-round",
                          "Population age 55 to 64 years who worked in the past 12 months, less than full-time, year-round - Margin of Error",
                          "Population age 55 to 64 years who did not work in the past 12 months",
                          "Population age 55 to 64 years who did not work in the past 12 months - Margin of Error",
                          "Population age 65 to 69 years",
                          "Population age 65 to 69 years - Margin of Error",
                          "Population age 65 to 69 years who worked in the past 12 months",
                          "Population age 65 to 69 years who worked in the past 12 months - Margin of Error",
                          "Population age 65 to 69 years who worked in the past 12 months, full-time, year-round",
                          "Population age 65 to 69 years who worked in the past 12 months, full-time, year-round - Margin of Error",
                          "Population age 65 to 69 years who worked in the past 12 months, less than full-time, year-round",
                          "Population age 65 to 69 years who worked in the past 12 months, less than full-time, year-round - Margin of Error",
                          "Population age 65 to 69 years who did not work in the past 12 months",
                          "Population age 65 to 69 years who did not work in the past 12 months - Margin of Error",
                          "Population age 70 years and over",
                          "Population age 70 years and over - Margin of Error",
                          "Population age 70 years and over who worked in the past 12 months",
                          "Population age 70 years and over who worked in the past 12 months - Margin of Error",
                          "Population age 70 years and over who worked in the past 12 months, full-time, year-round",
                          "Population age 70 years and over who worked in the past 12 months, full-time, year-round - Margin of Error",
                          "Population age 70 years and over who worked in the past 12 months, less than full-time, year-round",
                          "Population age 70 years and over who worked in the past 12 months, less than full-time, year-round - Margin of Error",
                          "Population age 70 years and over who did not work in the past 12 months",
                          "Population age 70 years and over who did not work in the past 12 months - Margin of Error",
                          "Percent of population age 16 to 19 years who worked in the past 12 months",
                          "Percent of population age 16 to 19 years who worked in the past 12 months - Margin of Error",
                          "Percent of population age 20 to 24 years who worked in the past 12 months",
                          "Percent of population age 20 to 24 years who worked in the past 12 months - Margin of Error",
                          "Percent of population age 25 to 44 years who worked in the past 12 months",
                          "Percent of population age 25 to 44 years who worked in the past 12 months - Margin of Error",
                          "Percent of population age 45 to 54 years who worked in the past 12 months",
                          "Percent of population age 45 to 54 years who worked in the past 12 months - Margin of Error",
                          "Percent of population age 55 to 64 years who worked in the past 12 months",
                          "Percent of population age 55 to 64 years who worked in the past 12 months - Margin of Error",
                          "Percent of population age 65 to 69 years who worked in the past 12 months",
                          "Percent of population age 65 to 69 years who worked in the past 12 months - Margin of Error",
                          "Percent of population age 70 years and over who worked in the past 12 months",
                          "Percent of population age 70 years and over who worked in the past 12 months - Margin of Error",
                          "Shape Area",
                          "Shape Length",
                          "Population age 65 years and over",
                          "Population age 65 years and over - Margin of Error",
                          "Population age 65 years and over who worked in the past 12 months",
                          "Population age 65 years and over who worked in the past 12 months - Margin of Error",
                          "Percent of population age 65 years and over who worked in the past 12 months",
                          "Percent of population age 65 years and over who worked in the past 12 months - Margin of Error"]
data_labor_clean = pd.DataFrame(data=LaborForce_Data.iloc[:, 2:])
data_labor_clean.columns = column_name_Labor_Data

data_labor_with_zip = pd.merge(Zip_Convert,
                               data_labor_clean,
                               how="left",
                               left_on="STCOUNTYFP",
                               right_on="FIPS_CODE").groupby("ZIP").sum()

# Check Referential Integrity
# data_labor_with_zip.to_csv("data_labor_with_zip.csv")
# data_ethic_with_zip.to_csv("data_ethic_with_zip.csv")
# data_income_with_zip.to_csv("data_income_with_zip.csv")

# Final Step
# Join All table
data_all_i = pd.merge(Final_Data, data_income_with_zip, how="left", left_on="ZipCode", right_on="ZIP")
data_all_ir = pd.merge(data_all_i, data_ethic_with_zip, how="left", left_on="ZipCode", right_on="ZIP")
data_all_irl = pd.merge(data_all_ir, data_labor_with_zip, how="left", left_on="ZipCode", right_on="ZIP")
data_all_irl.to_csv("data_all.csv", index=False)


