from django.shortcuts import render
import pandas as pd
import numpy as np

def show_dataframe(request):
    a={'Column1': [1, 2, 3], 'Column2': [4, 5, 6]}
    df1 = pd.DataFrame(a)
    df2 = pd.DataFrame({'Column3': ["ggm", 8, 9,10,11], 'Column4': ["gg1", "gg2", 12,15,16]})
    
    context = {
        'df1': df1,
        'df2': df2,
    }
    
    return render(request, 'show_dataframe.html', context)
