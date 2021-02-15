from django.conf import settings
from django.db import models
from pathlib import Path
from zipfile import ZipFile
import os

from oits_params.models import OitsParams

class TrajectoryResult(models.Model):
    '''
    Results record for a mission OitsParams
    '''

    oits_params = models.OneToOneField(
        OitsParams,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    values = models.TextField()
    exception = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.oits_params.uid)

    def populate_values_from_output_file(self):
        uid = str(self.oits_params.uid)
        home = str(Path.home())
        filename = uid + '.zip'
        filename_path = os.path.join(settings.MEDIA_ROOT.replace('~',home), filename)

        zip_results=ZipFile(filename_path)

        results_by_body = {}

        intermediate_point_index = 1

        for file_name in zip_results.namelist():

            if not 'orbparam' in file_name:

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

                    contents_by_time = self._get_contents_by_time(contents_by_time, contents)

                    results_by_body[body] = contents_by_time


        results = []
        for body in results_by_body:
            # Add header
            results.append(body)
            data = results_by_body[body]
            for t in sorted(data):
                results.append(data[t])


        self.values = '\n'.join(results)
        self.save()

        # Keep files for the moment
        #os.remove(filename_path)


    def _get_contents_by_time(self, contents_by_time, contents):

        for r in contents:

            data = r.split(',')
            if len(data) > 1:


                time = data[0].strip()

                output_row = ",".join([
                    time,
                    data[3],
                    data[4],
                    data[5],
                ])

                contents_by_time[float(time)] = output_row

        return contents_by_time

