import pandas as pd 

data='ALLEUJAH AMEN GREAT GOD our LORD AND SAVIOR JESUS CHRIST REIGNS FOREVER AMEN'.split()
df=pd.DataFrame(data)

data={
    'name':'Matthew,Mark,Luke,John,Mary,David,Jonah'.split(','),
    'position':'tax collector,evangelist,historian,evangelist,charity worker,king of Israel,prophet'.split(','),
    'mentioned_in':'Matthew and Luke,Mark and Acts,Luke and Acts,John and Revelation,John,1 and 2 Kings,Jonah'.split(','),
}
df=pd.DataFrame(data)
print(df)