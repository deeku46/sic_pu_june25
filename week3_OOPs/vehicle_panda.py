import pandas as pd

def read_excel_file():
    file_path = "C:/Users/Dx/Downloads/archive/car data.csv"
    df = pd.read_csv(file_path)
    print(df.count())
    print(df.head())
    print(df.tail())

def read_excel_file1():
    file_path = "C:/Users/Dx/Downloads/archive/car data.csv"
    df = pd.read_csv(file_path)
    for index, row in df.iterrows():
        print(row[0],' ',row[1])

def read_excel_file2():
    file_path = "C:/Users/Dx/Downloads/archive/car data.csv"
    df = pd.read_csv(file_path)
    for row in df.iterrows():
       print(row[1][0], row[1][1])


#read_excel_file()
#read_excel_file1()
read_excel_file2()