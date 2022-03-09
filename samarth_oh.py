


def handling_outliers_drop(data,column_name,iqr_multiplier=1.5):
    '''
    Function written by Samarth for handling outliers using just IQR method and drops the outliers. 
    data : Pass the entire pandas dataframe.
    column_name : Pass the column_name you want to handle
    iqr_mulitplier : This is the value used for multiplying IQR to remove the outliers. 
        default value : 1.5
    '''
    q3 = data[column_name].quantile(0.75)
    q1 = data[column_name].quantile(0.25)
    iqr = q3-q1
    uw = q3+iqr_multiplier*iqr
    lw = q1-iqr_multiplier*iqr
    temp = data[(data[column_name]>lw)&(data[column_name]<uw)]
    return temp



def handling_outliers_winsorization(data,column_name,iqr_multiplier=1.5):
    '''
    Function written by Samarth for handling outliers using just IQR method and caps to upper and lower whiskers. 
    data : Pass the entire pandas dataframe.
    column_name : Pass the column_name you want to handle
    iqr_mulitplier : This is the value used for multiplying IQR to remove the outliers. 
        default value : 1.5
    '''
    temp = data.copy()
    q3 = temp[column_name].quantile(0.75)
    q1 = temp[column_name].quantile(0.25)
    iqr = q3-q1
    uw = q3+iqr_multiplier*iqr
    lw = q1-iqr_multiplier*iqr
    temp.loc[temp[column_name]<lw,column_name] = lw
    temp.loc[temp[column_name]>uw,column_name] = uw
    return temp