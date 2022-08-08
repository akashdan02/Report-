from django.shortcuts import render
from .models import*
import pandas as pd


def home(request):
    item=Client.objects.all().values()
    clientname=pd.DataFrame(item)
    mydict={
        clientname.to_excel()
    }
    pd.ExcelWriter('outputfilename.xlsx')
    clientname.to_excel(item, index=False, sheet_name='TableName1')
    return render(request,'clientname.xlsx', context = mydict)

    file_name = 'clientname.xlsx'
#
    item.to_excel(file_name)
