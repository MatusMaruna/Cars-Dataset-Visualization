import pandas as pd

class DataReader: 

    def getData(): 
        cars = pd.read_csv('data.csv')
        #Replace '?' in all columns with mean 
        a=cars[cars['normalized-losses']!='?']
        b=(a['normalized-losses'].astype(int)).mean()
        cars['normalized-losses']=cars['normalized-losses'].replace('?',b).astype(int)

        a=cars['num-of-doors'].map({'two':2,'four':4,'?':4})
        cars['num-of-doors']=a

        a=cars[cars['price']!='?']
        b=(a['price'].astype(int)).mean()
        cars['price']=cars['price'].replace('?',b).astype(int)

        a=cars[cars['horsepower']!='?']
        b=(a['horsepower'].astype(int)).mean()
        cars['horsepower']=cars['horsepower'].replace('?',b).astype(int)

        a=cars[cars['bore']!='?']
        b=(a['bore'].astype(float)).mean()
        cars['bore']=cars['bore'].replace('?',b).astype(float)

        a=cars[cars['stroke']!='?']
        b=(a['stroke'].astype(float)).mean()
        cars['stroke']=cars['stroke'].replace('?',b).astype(float)

        a=cars[cars['peak-rpm']!='?']
        b=(a['peak-rpm'].astype(float)).mean()
        cars['peak-rpm']=cars['peak-rpm'].replace('?',b).astype(float)
        cars = cars.reset_index()
        #Create normalized dataset between 0 and 5 for radar plot
        temp = cars.copy()
        a, b = 0, 5
        x, y = temp['horsepower'].min(), temp['horsepower'].max()
        temp['horsepower'] = (temp['horsepower'] - x) / (y - x) * (b - a) + a
        x, y = temp['curb-weight'].min(), temp['curb-weight'].max()
        temp['curb-weight'] = (temp['curb-weight'] - x) / (y - x) * (b - a) + a
        x, y = temp['price'].min(), temp['price'].max()
        temp['price'] = (temp['price'] - x) / (y - x) * (b - a) + a
        x, y = temp['engine-size'].min(), temp['engine-size'].max()
        temp['engine-size'] = (temp['engine-size'] - x) / (y - x) * (b - a) + a
        temp['mpg'] = cars[['city-mpg', 'highway-mpg']].mean(axis=1)
        x, y = temp['mpg'].min(), temp['mpg'].max()
        temp['mpg'] = (temp['mpg'] - x) / (y - x) * (b - a) + a
        

        return cars, temp 