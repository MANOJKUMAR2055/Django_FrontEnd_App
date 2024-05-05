from django.shortcuts import render
import pandas as pd

def index(request):
    headers = None
    preview_data = None
    if request.method == 'POST':
        excel_file = request.FILES.get('excel-file')
        if excel_file:
            if excel_file.name.endswith('.xlsx') or excel_file.name.endswith('.xls'):
                df = pd.read_excel(excel_file)
                headers = df.columns.tolist()
                preview_data = df.values.tolist()
            else:
                error_message = "Invalid file format. Please upload a .xlsx or .xls file."
                return render(request, 'index.html', {'error_message': error_message})
        else:
            error_message = "No file selected. Please choose a file to upload."
            return render(request, 'index.html', {'error_message': error_message})
    return render(request, 'index.html', {'preview_data': preview_data, 'headers': headers})
