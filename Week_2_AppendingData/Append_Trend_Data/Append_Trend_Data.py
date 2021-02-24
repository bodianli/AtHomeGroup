# https://www2.census.gov/programs-surveys/popest/datasets/2010-2019/counties/totals/
# https://www2.census.gov/programs-surveys/popest/technical-documentation/file-layouts/2010-2019/nst-est2019-alldata.pdf
# The FIPS_CODE is composite by "state"+"region" ,
# 02:Alaska
# 013:Aleutians East Borough
# FIPS_CODE: 02013
import pandas as pd

Data_All = pd.read_csv(r"C:\Users\Bodian\Desktop\AtHomeGroup\Week_2_AppendingData\data_all.csv",
                       encoding="UTF-8")

Zip_Convert = pd.read_csv(r"C:\Users\Bodian\Desktop\AtHomeGroup\Week_2_AppendingData\ZIP-COUNTY-FIPS_2010-03.csv",
                          encoding="UTF-8",
                          usecols=["ZIP", "COUNTYNAME"]
                          )

Trend_data = pd.read_csv("co-est2019-alldata.csv")

Trend_data_with_zip = pd.merge(Zip_Convert, Trend_data,
                               how="left",
                               left_on="COUNTYNAME",
                               right_on="CTYNAME").groupby("ZIP").sum()

Trend_data_with_zip.to_csv("Trend_data_with_zip.csv", index=False)


AtHomeGroup_Demographic = pd.merge(Data_All,Trend_data_with_zip,how="left",
              left_on="ZipCode",
              right_on="ZIP")

AtHomeGroup_Demographic.to_csv("AtHomeGroup_Demographic.csv", index=False)

# data_all_trend = pd.merge(Data_All, Trend_data_with_zip, how="left", left_on="ZipCode", right_on="ZIP")
# data_all_trend.to_csv("data_all_trend.csv", index=False)

