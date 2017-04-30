import pandas as pd
import csv


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
    return roster_dict


def write_to(id, name, crew, filepath):
    """Write directly to csv file without overwriting with new file.
    Takes in arguments of type str: 
                write_to("<id_str>", "<name_str>", <crew_int>, "<filepath_str>")
    example:    write_to("21452", "Daniel Ochoa", 1, "Data/roster.csv")
    """
    with open(filepath, 'a', newline='') as csvfile:
        # csvfile.write([id,name,crew])
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow([id, name, crew])


if __name__ == "__main__":
    roster_dict2 = get_roster("Data/roster.csv")
    # write_to("21452", "Daniel Ochoa", 1, "Data/roster.csv")
