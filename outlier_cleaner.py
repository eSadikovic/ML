#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    z=zip(predictions, ages, net_worths)
    
    d=[]
    
    for i in z:
        d.append((i[0]-i[2])*(i[0]-i[2]))
        
    for j in range(len(z)):
        l=list(z[j])
        l.append(d[j])
        z[j]=l
        
    sorted_by_4=sorted(z, key=lambda tup: tup[3])    
    
    del sorted_by_4[-10:]
    
    for i in sorted_by_4:
        i.pop(0)
        i=list(i)
    
    cleaned_data=sorted_by_4
    
   

    ### your code goes here
    
    

    
    return cleaned_data
