import pandas as pd
import os

main = pd.DataFrame()

#os.remove("/Users/eottu002/Desktop/datafiles/.DS_Store") #this removes the hidden OS File 

Names = list(os.listdir('/Users/eottu002/Desktop/datafiles'))

Names.sort()

for file in Names:
    file_path = f'/Users/eottu002/Desktop/datafiles/{file}'
    print(file)
    df = pd.read_csv(file_path,sep='\t',skiprows=6)
    column_name = f"{file.strip('.jpg.iris')}"
    df = df.rename(columns={'opacity':column_name})
    main[column_name] = df[column_name]

main.to_csv('all_output.csv',index=None)

