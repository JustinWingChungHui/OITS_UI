from django.core.management.base import BaseCommand
from django.conf import settings
from oits_params.models import OitsParams
from pathlib import Path
import json
import os
import sys
import time
import zipfile

class Command(BaseCommand):

    def handle(self, *args, **options):
        '''
        Always on task that checks for any new runs
        '''

        home = str(Path.home())
        oits_lib_path = settings.OITS_LIBRARY.replace('~', home)

        print('settings: {0}'.format(oits_lib_path))

        # Finds the OITS_optimizer.py in the OITS_AH_Linux folder
        sys.path.insert(0, oits_lib_path)
        from OITS_optimizer import OITS_optimizer

        while True:

            print('Starting OitsRunner')
            new_runs = OitsParams.objects.filter(status=OitsParams.NEW).order_by('created_at')

            print('New runs:')
            print(new_runs)

            for run in new_runs:

                print('Processing {0}'.format(run.uid))
                run.status = OitsParams.PROCESSING
                run.save()

                params = json.loads(run.parameters)

                # Append Spice driectory to filenames
                bsp = []
                for file in params['BSP']:
                    bsp.append(oits_lib_path + "SPICE/" + file)

                try:
                    OITS_instance = OITS_optimizer()

                    OITS_instance.set_OITS(
                            0 if params['trajectory_optimization'] else 1,
                            str(run.uid),
                            params['Nbody'],
                            params['ID'],
                            params['NIP'],
                            params['rIP'],
                            params['thetaIP'],
                            params['thiIP'],
                            params['thetalb'],
                            params['thetaub'],
                            params['thilb'],
                            params['thiub'],
                            params['t01'].lower(),
                            params['tmin1'].lower(),
                            params['tmax1'].lower(),
                            params['t0'],
                            params['tmin'],
                            params['tmax'],
                            params['Periacon'],
                            params['dVcon'],
                            params['Perihcon'],
                            0, # Peroflag
                            params['Duration'],
                            1 if params['PROGRADE_ONLY'] else 0,
                            1 if params['RENDEZVOUS'] else 0,
                            params['Ndata'],
                            params['RUN_TIME'],
                            len(bsp), #NBSP
                            bsp, #BSP
                            oits_lib_path + "SPICE/naif0012.tls") #LSF

                    OITS_instance.convert_python_to_C()
                    OITS_instance.OITS()

                    print('Processing {0} finished'.format(run.uid))

                except Exception as e:
                    file = open(str(run.uid) + "_error.txt", "w")
                    file.write(e)
                    file.close()

                self.create_archive(run)

                run.status = OitsParams.COMPLETE
                run.save()

                print('Completed {0}'.format(run.uid))

            time.sleep(10)





    def create_archive(self, run):
        '''
        Gets all the files and stores them as a zip in media directory
        for download
        '''

        print('creating archive')

        home = str(Path.home())
        filename = str(run.uid) + '.zip'

        zip_name = os.path.join(settings.MEDIA_ROOT.replace('~',home), filename)
        print('Writing to {0}'.format(zip_name))

        zf = zipfile.ZipFile(zip_name,'w', zipfile.ZIP_DEFLATED)

        cwd = os.getcwd()
        for f in os.listdir(cwd):
            if str(run.uid) in f:
                print('Adding file {0}'.format(f))
                zf.write(os.path.join(cwd,f), arcname=f)
                os.remove(os.path.join(cwd,f))

        zf.close()




