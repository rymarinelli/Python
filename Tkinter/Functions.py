import sqlite3
import pandas as pd
import os
from pathlib import Path

parameter_list = ['SCORE', 'Zip Codes', 'Seating', 'Year']
downloads = str(os.path.join(Path.home(), "Downloads"))

class Query():

    def __init__(self):
        self.value = -1
        self.second_value = -1

    def set_Data(self):
        downloads = str(os.path.join(Path.home(), "Downloads"))
        file_path = downloads + "\combined_test.csv"
        df = pd.read_csv(file_path)
        return df

    def set_Value(self, second):
        self.value = second
        return self.value

    def set_Second_Value(self, second_value):
        self.second_value = second_value
        return self.second_value


    def group_By(self, parameter_list):
        df = self.set_Data()
        df = df[parameter_list]
        self.set_Value(0)
        return (df)


    def group_By_1(self,parameter_list):
        df = self.set_Data()
        parameter_list = [parameter_list[i] for i in (0, 2, 3)]
        print(parameter_list)
        df = df[parameter_list]
        self.set_Value(1)
        return(df)

    def group_By_2(self,parameter_list):
        parameter_list = [parameter_list[i] for i in (0, 1, 3)]
        print(parameter_list)
        df = self.set_Data()
        df = df[parameter_list]
        self.set_Value(2)
        return(df)

#    def mean(self):
#        print('Testing if value was changed')
#        print(self.test)
#        if self.test == -1:
#            print("No action selected")
#            print('Testing if value was changed')
#            print(self.test)
#        elif self.test == 0:
#            print(Query.group_By(self,parameter_list).mean())
#            self.test = -1
#        elif self.test == 1:
#            print(Query.group_By_1(self, parameter_list).mean())
#            self.test = -1
#        else:
#            print(Query.group_By_2(self, parameter_list).mean())
#            self.test = -1
    def mean(self):
        file_path = (downloads + "\query_result.csv")
        self.set_Second_Value(0)
        if self.value == -1:
            print('No Action')
        elif self.value == 0:
            print('value is zero')
            df = self.group_By(parameter_list)
            df = df.groupby(['Year', "Zip Codes", 'Seating']).mean()
            df_1 = pd.DataFrame(df)
            df_1.to_csv(file_path)
            print(df)
            return df
        elif self.value == 1:
            print('value is one')
            df = self.group_By_1(parameter_list)
            df = df.groupby(['Year', 'Seating']).mean()
            df_1 = pd.DataFrame(df)
            df_1.to_csv(file_path)
            print(df)
            return df
        else:
            print('value is two')
            df = self.group_By_2(parameter_list)
            df = df.groupby(['Year', 'Zip Codes']).mean()
            df_1 = pd.DataFrame(df)
            df_1.to_csv(file_path)
            print(df)
            return df

    def median(self):
        file_path = (downloads + "\query_result.csv")
        self.set_Second_Value(1)
        if self.value == -1:
            print('No Action')
        elif self.value == 0:
            print('value is zero')
            df = self.group_By(parameter_list)
            df = df.groupby(['Year', "Zip Codes", 'Seating']).median()
            df_1 = pd.DataFrame(df)
            df_1.to_csv(file_path)
            print(df)
            return(df)
        elif self.value == 1:
            print('value is one')
            df = self.group_By_1(parameter_list)
            df = df.groupby(['Year', 'Seating']).median()
            df_1 = pd.DataFrame(df)
            df_1.to_csv(file_path)
            print(df)
            return df
        else:
            print('value is two')
            df = self.group_By_2(parameter_list)
            df = df.groupby(['Year', 'Zip Codes']).median()
            df_1 = pd.DataFrame(df)
            df_1.to_csv(file_path)
            print(df)
            return df


    def mode(self):
        file_path = (downloads + "\query_result.csv")
        self.set_Second_Value(2)
        if self.value == -1:
            print('No Action')
        elif self.value == 0:
            print('value is zero')
            df = self.group_By(parameter_list)
            df = df.groupby(['Year', "Zip Codes", 'Seating']).agg(lambda val:val.value_counts().index[0])
            df_1 = pd.DataFrame(df)
            df_1.to_csv(file_path)
            print(df)
            return df
        elif self.value == 1:
            print('value is one')
            df = self.group_By_1(parameter_list)
            df = df.groupby(['Year', 'Seating']).agg(lambda val:val.value_counts().index[0])
            df_1 = pd.DataFrame(df)
            df_1.to_csv(file_path)
            print(df)
            return df
        else:
            print('value is two')
            df = self.group_By_2(parameter_list)
            df = df.groupby(['Year', 'Zip Codes']).agg(lambda val:val.value_counts().index[0])
            df_1 = pd.DataFrame(df)
            df_1.to_csv(file_path)
            print(df)
            return df

    def query_print(self):
        if self.second_value == -1:
            return None
        elif self.second_value == 0:
            self.set_Second_Value(-1)
            return self.mean()
        elif self.second_value == 1:
            self.set_Second_Value(-1)
            return self.median()
        else:
            self.set_Second_Value(-1)
            return self.mode()