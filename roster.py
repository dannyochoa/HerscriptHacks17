import pandas as pd


def get_roster(filepath):
    """Returns dictionary with format {<id1>:['<name1>',<crew#1>], <id2>:['<name2>',<crew#2>], ...}  
    roster_dict[35851][0] gets the name
    roster_dict[35851][1] gets the crew 
    """
    roster_df = pd.read_csv(filepath)
    roster_df.sort_values('crew', inplace=True)
    roster_df.reset_index(inplace=True)
    del roster_df['index']
    roster_dict = roster_df.set_index('id').T.to_dict('list')
    print(roster_dict)
    return roster_dict


if __name__ == "__main__":
    roster_dict2 = get_roster("Data/roster.csv")
