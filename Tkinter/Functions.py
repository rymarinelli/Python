import sqlite3
import pandas as pd

parameter_list = ['SCORE', 'Zip Codes', 'Seating', 'Year']
class Query():

    def __init__(self):
        self.value = -1

    def set_Data(self):
        df = pd.read_csv('C:\\Users\\rmarinelli4\\Downloads\\combined_test.csv')
        return df

    def set_Value(self, second):
        self.value = second
        return self.value


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
        if self.value == -1:
            print('No Action')
        elif self.value == 0:
            print('value is zero')
            df = self.group_By(parameter_list)
            df = df.groupby(['Year', "Zip Codes", 'Seating']).mean()
            print(df)
        elif self.value == 1:
            print('value is one')
            df = self.group_By_1(parameter_list)
            df = df.groupby(['Year', 'Seating']).mean()
            print(df)
        else:
            print('value is two')
            df = self.group_By_2(parameter_list)
            df = df.groupby(['Year', 'Zip Codes']).mean()
            print(df)

    def median(self):
        if self.value == -1:
            print('No Action')
        elif self.value == 0:
            print('value is zero')
            df = self.group_By(parameter_list)
            df = df.groupby(['Year', "Zip Codes", 'Seating']).median()
            print(df)
        elif self.value == 1:
            print('value is one')
            df = self.group_By_1(parameter_list)
            df = df.groupby(['Year', 'Seating']).median()
            print(df)
        else:
            print('value is two')
            df = self.group_By_2(parameter_list)
            df = df.groupby(['Year', 'Zip Codes']).median()
            print(df)


    def mode(self):
        if self.value == -1:
            print('No Action')
        elif self.value == 0:
            print('value is zero')
            df = self.group_By(parameter_list)
            df = df.groupby(['Year', "Zip Codes", 'Seating']).agg(lambda val:val.value_counts().index[0])
            print(df)
        elif self.value == 1:
            print('value is one')
            df = self.group_By_1(parameter_list)
            df = df.groupby(['Year', 'Seating']).agg(lambda val:val.value_counts().index[0])
            print(df)
        else:
            print('value is two')
            df = self.group_By_2(parameter_list)
            df = df.groupby(['Year', 'Zip Codes']).agg(lambda val:val.value_counts().index[0])
            print(df)
