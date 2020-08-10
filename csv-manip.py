import pandas as pd
import os

# TODO: Replace "MOCK_DATA.csv" with the actual filename once everyone sends me their email


path = "./sheets/"

#creates a pd.DataFrame object from a csv that has one column for name and one column for email
origin_df = pd.read_csv(os.path.join(path, "MOCK_DATA.csv")) 

#makes a dict of lists where every key is a person's name and every value is the person's email
name_to_email = origin_df.set_index('name').T.to_dict('list') 

day = 0
block = 0

for filename in os.listdir(path):
    if filename.endswith(".csv") and filename != "MOCK_DATA.csv":
        dest_df = pd.read_csv(os.path.join(path, filename))
        names_to_replace = dest_df['Email Address']

        day += 1
        block += 1
        block = block % 3
        new_col = []
        new_path_name = "Day{}Block{}.csv".format(day, block)

        del dest_df['Email Address']

        for entry in names_to_replace:
            new_col.append(name_to_email[entry][0])
        
        dest_df['Email Address'] = new_col
        dest_df.to_csv(os.path.join(path, new_path_name), index=False, header=True)
        continue
    else:
        continue
