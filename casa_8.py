import pandas as pd
bigmacfile = "./big-mac-full-index.csv"

#--------------The following is Method 4: Using interrows() method
df = pd.read_csv(bigmacfile)

print("Commencing Interrow Method")
for index, row in df.iterrows():
    dollar_gdp = row['dollar_price'] + row['GDP_bigmac']
    print(f"{row['name']} Sum of dollar price and GDP = ${dollar_gdp}")
print("\nInterrow Method Complete")

input()


#---------------The following is Method 6: Using apply() method---------------------

print("Commencing Apply method")
def dollar_gdp(row):
    dollar_gdp = row['dollar_price'] + row['GDP_bigmac']
    return f"{row['name']} Sum of dollar price and GDP = ${dollar_gdp}"
result = df.apply(dollar_gdp, axis=1)
for res in result:
    print(res)
print("\nApply Method Complete")



