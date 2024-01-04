import pandas as pd

text = "Hello world!" # UTF-8 encoded string

# Convert to list of integer code points 
code_points = [ord(char) for char in text]

# Create a Pandas DataFrame
df = pd.DataFrame(code_points, columns=['code_point'])

print(df)
