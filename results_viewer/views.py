from django.conf import settings
from django.http import HttpResponse
from pathlib import Path
from zipfile import ZipFile
import os



# Create your views here.
def get_results_csv(request, uid):

    home = str(Path.home())
    filename = uid + '.zip'
    zip_results = os.path.join(settings.MEDIA_ROOT.replace('~',home), filename)

    zip_results=ZipFile(zip_results)

    results = []

    for name in zip_results.namelist():
        contents = zip_results.read(name)

        header = name.replace(uid, '')
        header = header.replace('.txt', '')
        if not header:
            header = 'MAIN'

        results.append(header)

        data = process_text(contents)


        results.append(data)

        results.append('#END#')

    response = '\n'.join(results)

    return HttpResponse(response, content_type='text/plain')


def process_text(contents):

    result = []

    for r in contents.decode("utf-8").split('\n'):

        # Data row
        if len(r) > 150:
            output_row = ",".join([
                r[0:15].strip(),
                r[53:68].strip(),
                r[69:84].strip(),
                r[85:100].strip(),
            ])

            result.append(output_row)

    return "\n".join(result)
