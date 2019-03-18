#*****************************************************************#
# Chi-square independence test: p-value and Carmers V calculation
# Version 1
# Copyrights: SirnaTechSolutions
# Date: 17 March 2019
#*****************************************************************#

def chi2ind(df):
    import numpy as np
    from scipy import stats
    import pandas as pd
    import math
    
    dataframe = df.dropna() #Drop missing values from the data frame
    dataframeCatOnly = dataframe.select_dtypes(include =['object']) #Pick out only Categorical parts of the dataframe
    
    if(dataframeCatOnly.shape[1]<2): #If the dataframe does not have atleast two categorical variables
        print("The given dataframe does not have enough categorical variables")
        dataP = 0
        dataCramersV = 0
    else:
        #Calculate the chi square independence test p values and cramers V so we can assess independence
        catColumnsList = dataframeCatOnly.columns; #Extract the list of column names from the data frame
        dataP = pd.DataFrame(columns = catColumnsList, index = catColumnsList) #Create a blank dataframe for the p values
        dataP.fillna('x', inplace = True)
        dataCramersV = pd.DataFrame(columns = catColumnsList, index = catColumnsList) #Create a blank dataframe for Cramers V values
        dataCramersV.fillna('x', inplace = True)
        catColumnsList = amesHousingCatOnly.columns

        for i in range(len(catColumnsList)-1):

            for j in range(i+1,len(catColumnsList)):

                table = pd.crosstab(dataframeCatOnly[catColumnsList[i]], dataframeCatOnly[catColumnsList[j]], margins = True)
                tableSize = table.shape
                tableRowInd = table.index[list(range(tableSize[0]-1))]
                tableColInd = table.columns[list(range(tableSize[1]-1))]
                f_obs = table.loc[tableRowInd,tableColInd].values
                chiTest = stats.chi2_contingency(f_obs)[0:3]
                dataP.iloc[i][j] = chiTest[1]
                dataCramersV.iloc[i][j] = math.sqrt(chiTest[0]/(dataframeCatOnly.shape[0]*(min(tableSize)-1)))
    return dataP, dataCramersV #Return the data frame of p values and Cramers v
