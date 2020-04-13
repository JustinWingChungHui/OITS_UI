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

        while True:
            home = str(Path.home())
            oits_lib_path = settings.OITS_LIBRARY.replace('~', home)

            print('settings: {0}'.format(oits_lib_path))

            sys.path.insert(0, oits_lib_path)

            from OITS_optimizer import OITS_optimizer

            print('Starting OitsRunner')

            new_runs = OitsParams.objects.filter(status=OitsParams.NEW).order_by('created_at')

            print('New runs:')
            print(new_runs)

            for run in new_runs:

                print('Processing {0}'.format(run.uid))
                run.status = OitsParams.PROCESSING
                run.save()

                params = json.loads(run.parameters)

                OITS_instance = OITS_optimizer()

                OITS_instance.set_OITS(
                        1 if params['trajectory_optimization'] else 0,
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
                        params['t01'],
                        params['tmin1'],
                        params['tmax1'],
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
                        1, #NBSP
                        [oits_lib_path + "SPICE/de430.bsp"], #BSP
                        oits_lib_path + "SPICE/naif0012.tls") #LSF

                OITS_instance.convert_python_to_C()
                OITS_instance.OITS()

                print('Processing {0} finished'.format(run.uid))

                self.create_archive(run)

                run.status = OitsParams.COMPLETE
                run.save()

                print('Completed {0}'.format(run.uid))

            time.sleep(30)





    def create_archive(self, run):

        print('creating archive')

        home = str(Path.home())
        zip_name = settings.MEDIA_ROOT.replace('~',home) +  str(run.uid) + '.zip'
        print('Writing to {0}'.format(zip_name))

        zf = zipfile.ZipFile(zip_name, mode='w')

        cwd = os.getcwd()
        for f in os.listdir(cwd):
            if str(run.uid) in f:
                print('Adding file {0}'.format(f))
                zf.write(os.path.join(cwd,f), arcname=f)
                os.remove(os.path.join(cwd,f))

        zf.close()




