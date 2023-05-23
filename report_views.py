import pandas as pd
from django.http import HttpResponse

def download_report(request):
    data = request.session.get('data')  # Retrieve the data from the session

    # Create a pandas DataFrame using the retrieved data
    df = pd.DataFrame(data)

    # Convert DataFrame to Excel
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='openpyxl')
    df.to_excel(writer, index=False, sheet_name='Sheet1')
    writer.save()
    output.seek(0)

    # Create the HttpResponse object with the appropriate headers
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=myreport.xlsx'
    response.write(output.getvalue())

    return response
