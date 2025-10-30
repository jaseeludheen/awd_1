from django.shortcuts import render


from .utils import get_all_custom_models, check_csv_errors
from django.conf import settings
from uploads.models import Upload
from django.contrib import messages
from django.shortcuts import redirect
from django.core.management import call_command
from .utils import send_email_notification



def import_data(request):
    if request.method == 'POST':
        file_path = request.FILES.get('file_path')    # FILES is used to handle file uploads in Django
        model_name = request.POST.get('model_name')

        # store thids file inside the Upload model
        upload = Upload.objects.create(file=file_path, model_name=model_name) 

        # construct the full path
        relative_path = str(upload.file.url)   # upload - upload/<file_name>.csv  
#        print(relative_path)  #  /media/uploads/<file_name>.csv
        base_url = str(settings.BASE_DIR)  # base url 
#        print(base_url)

        file_path = base_url + relative_path
#        print(file_path)

        # check for the csv errors
        try:
            check_csv_errors(file_path, model_name)
        except Exception as e:
            messages.error(request, 'fields do not match with the model') 
            messages.error(request, str(e))  # if there are any errors in the CSV file, show the error message to the user
            return redirect('import_data')  # redirect to the same page if there are errors



    
        # trigger the import data command  ( )
        try:
            call_command('importdatafromcsv', file_path, model_name)
            
        except Exception as e:
            
            messages.error(request, str(e))  # error message if something goes wrong    

        # notify the user by email
        mail_subject = 'Import Data Completed'
        message = 'Your data import has been successful'
        to_email = settings.DEFAULT_TO_EMAIL
        send_email_notification(mail_subject, message, [to_email])
        messages.success(request, 'Data imported successfully!') 


        return redirect('import_data')  # redirect to the same page after uploading the file


    else: 
        custom_models = get_all_custom_models()       #  function call to get all custom models from utils.py
#        print(custom_models)
        context = {
            'custom_models': custom_models,
        }
    return render(request, 'dataentry/importdata.html', context)