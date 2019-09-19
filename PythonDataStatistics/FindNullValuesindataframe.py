amesHousingOrig.head()
amesHousingOrig.tail()
amesHousingOrig.describe()
amesHousingOrig.info()

#Find missing values and print for every column
amesHousingMissing = amesHousingOrig[amesHousingOrig.columns[amesHousingOrig.isnull().any()]].isnull().sum()#Print missing value count for missing value columns
amesHousingMissing.to_csv("AmesHousing_missing_data.csv", header = False)


#Apply threshold
amesHousingColRemoved = amesHousingOrig.dropna(thresh = len(amesHousingOrig)-400, axis = 1) #Remove columns having atleast 1000 missing values

#So the way the threshold works is total length minus threshold
