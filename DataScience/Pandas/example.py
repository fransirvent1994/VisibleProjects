# First we import Pandas library. Pandas will be named as pd from now on
import pandas as pd 

# We make a list with the data we want to work with
users = {
    "Name": ["Juan", "María", "Carlos", "Ana", "Luis"],
    "Surname": ["Gómez", "López", "Rodríguez", "Pérez", "Martínez"],
    "Email": ["juan@example.com", "maria@example.com", "carlos@example.com", "ana@example.com", "luis@example.com"],
    "Phone": ["123-123-4567", "456-987-6543", "789-567-8901", "654-234-5678", "963-678-9012"],
    "Age": [12, 27, 22, 30, 16],
    "Address": ["13 Rue del Percebe", "La Vega", "Murcia", "Unknown", "Johto"]
}

# Var users_df refers to Data from users with pd.DataFrame
users_df = pd.DataFrame(users)

# Var above_age refers to value which points to users 18 or more years old
above_age = users_df[users_df["Age"] >= 18]

# Prints 18 or above years old users
print(above_age)

# A function to modify the phone numbers.
def modify_sintax(numbers):
    numbers_modified = numbers.replace("-", "")
    return f"({numbers_modified[0:3]}) {numbers_modified[3:6]}-{numbers_modified[6:]}"

users_df["Phone"] = users_df["Phone"].apply(modify_sintax)

print("***\n"*5)
print(users_df)

print("***\n"*5)

df_organized = users_df.sort_values(by='Age', ascending=False)
print(df_organized)
