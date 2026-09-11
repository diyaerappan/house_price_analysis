import pandas as pd

# --------------------------------
# 1. Importing the dataset
# --------------------------------

df = pd.read_csv("house_data.csv")

print("HOUSE PRICE DATASET")
print("-------------------")
print(df)


# --------------------------------
# 2. Basic information
# --------------------------------

print("\nDATAFRAME INFORMATION")
print("---------------------")
df.info()


# --------------------------------
# 3. Shape of the dataset
# --------------------------------

print("\nDATASET SHAPE")
print("-------------")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])


# --------------------------------
# 4. Statistical summary
# --------------------------------

print("\nSTATISTICAL SUMMARY")
print("-------------------")
print(df.describe())


# --------------------------------
# 5. Check data types
# --------------------------------

print("\nDATA TYPES BEFORE CLEANING")
print("--------------------------")
print(df.dtypes)


# --------------------------------
# 6. Cleaning the Doors column
# --------------------------------

df["Doors"] = pd.to_numeric(
    df["Doors"],
    errors="coerce"
)


# --------------------------------
# 7. Converting Price to numeric
# --------------------------------

df["Price"] = pd.to_numeric(
    df["Price"],
    errors="coerce"
)


# --------------------------------
# 8. Converting categorical columns
# --------------------------------

df["Location"] = df["Location"].astype("category")

df["Furnishing"] = df["Furnishing"].astype("category")


# --------------------------------
# 9. Check data types after cleaning
# --------------------------------

print("\nDATA TYPES AFTER CLEANING")
print("-------------------------")
print(df.dtypes)


# --------------------------------
# 10. Count missing values
# --------------------------------

print("\nMISSING VALUES")
print("--------------")
print(df.isnull().sum())


# --------------------------------
# 11. Fill missing values
# --------------------------------

df["Bathrooms"] = df["Bathrooms"].fillna(
    df["Bathrooms"].median()
)

df["Doors"] = df["Doors"].fillna(
    df["Doors"].median()
)


# --------------------------------
# 12. Check missing values again
# --------------------------------

print("\nMISSING VALUES AFTER CLEANING")
print("-----------------------------")
print(df.isnull().sum())


# --------------------------------
# 13. Basic analysis
# --------------------------------

print("\nAVERAGE HOUSE PRICE")
print("------------------")
print(df["Price"].mean())


print("\nMOST EXPENSIVE HOUSE")
print("--------------------")
print(df.loc[df["Price"].idxmax()])


print("\nAVERAGE PRICE BY LOCATION")
print("-------------------------")
print(df.groupby("Location", observed=True)["Price"].mean())


print("\nAVERAGE PRICE BY FURNISHING")
print("----------------------------")
print(df.groupby("Furnishing", observed=True)["Price"].mean())


# --------------------------------
# 14. Save cleaned dataset
# --------------------------------

df.to_csv(
    "cleaned_house_data.csv",
    index=False
)

print("\nCleaned dataset saved successfully!")