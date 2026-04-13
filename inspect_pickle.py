import pickle

with open("combined_df.pkl", "rb") as f:
    data = pickle.load(f)

print(type(data))
print(data.keys() if isinstance(data, dict) else data)