from django.conf import settings
from django.http import HttpResponse
from pathlib import Path
from zipfile import ZipFile
import collections
import os



def get_results_csv(request, uid):

    home = str(Path.home())
    filename = uid + '.zip'
    zip_results = os.path.join(settings.MEDIA_ROOT.replace('~',home), filename)

    zip_results=ZipFile(zip_results)

    results = []

    for name in zip_results.namelist():
        contents = zip_results.read(name).decode("utf-8").split('\n')

        if len(contents) > 0:
            suffix = name.replace(uid, '')
            suffix = suffix.replace('.txt', '')

            if suffix:
                header = contents[0]
            else:
                header = 'PROBE'

            results.append(header)

            data = process_text(contents)


            results.append(data)

            results.append('#END#')

    response = '\n'.join(results)

    return HttpResponse(response, content_type='text/plain')


def process_text(contents):

    result = []

    for r in contents:

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


# Create your views here.
def get_sorted_results_csv(request, uid):

    home = str(Path.home())
    filename = uid + '.zip'
    zip_results = os.path.join(settings.MEDIA_ROOT.replace('~',home), filename)

    zip_results=ZipFile(zip_results)

    results_by_body = {}

    intermediate_point_index = 1

    for file_name in zip_results.namelist():
        contents = zip_results.read(file_name).decode("utf-8").split('\n')

        if len(contents) > 0:
            suffix = file_name.replace(uid, '')
            suffix = suffix.replace('.txt', '')

            if suffix:
                body = contents[0]
            else:
                body = 'PROBE'

            # append intermediate points with an index
            if 'INTERMEDIATE POINT' in body:
                body = body + ' ' + str(intermediate_point_index)
                intermediate_point_index += 1

            if body in results_by_body:
                contents_by_time = results_by_body[body]
            else:
                contents_by_time = {}

            contents_by_time = get_contents_by_time(contents_by_time, contents)

            results_by_body[body] = contents_by_time


    results = []
    for body in results_by_body:
        # Add header
        results.append(body)
        data = results_by_body[body]
        for t in sorted(data):
            results.append(data[t])




    response = '\n'.join(results)
    return HttpResponse(response, content_type='text/plain')



def get_contents_by_time(contents_by_time, contents):

    for r in contents:

        time = r[0:15].strip()
        # Data row
        if len(r) > 150:
            output_row = ",".join([
                time,
                r[53:68].strip(),
                r[69:84].strip(),
                r[85:100].strip(),
            ])

            contents_by_time[float(time)] = output_row

    return contents_by_time
