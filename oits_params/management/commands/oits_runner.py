from django.core.management.base import BaseCommand
from django.conf import settings
from oits_params.models import OitsParams
from results_viewer.models import TrajectoryResult
from pathlib import Path
from multiprocessing import Process
import json
import os
import sys
import time
import zipfile

class Command(BaseCommand):

    executing_processes = {}

    def handle(self, *args, **options):
        '''
        Always on task that checks for any new runs
        '''

        home = str(Path.home())
        oits_lib_path = settings.OITS_LIBRARY.replace('~', home)

        print('settings: {0}'.format(oits_lib_path))

        # Finds the OITS_optimizer.py in the OITS_AH_Linux folder
        sys.path.insert(0, oits_lib_path)

        print('Starting OitsRunner')

        while True:

            # Ceancel any process that have been requested to be cancelled
            cancelling_runs = OitsParams.objects.filter(status=OitsParams.CANCELLING).order_by('created_at')

            for run in cancelling_runs:
                if run.id in self.executing_processes:
                    self.executing_processes[run.id].terminate()
                    run.status = OitsParams.CANCELLED
                    run.save()
                    self.executing_processes.pop(run.id)


            new_runs = OitsParams.objects.filter(status=OitsParams.NEW).order_by('created_at')

            for run in new_runs:

                if (len(self.executing_processes) < 3):

                    process = Process(target=self.execute_run, args=(run, oits_lib_path))
                    self.executing_processes[run.id] = process
                    process.start()


            time.sleep(10)


    def execute_run(self, run, oits_lib_path):

        print('Processing {0}'.format(run.uid))
        run.status = OitsParams.PROCESSING
        run.save()

        params = json.loads(run.parameters)

        # Append Spice directory to filenames
        bsp = []
        for file in params['BSP']:
            bsp.append(oits_lib_path + "SPICE/" + file)

        try:
            from OITS_optimizer import OITS_optimizer
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

            run.status = OitsParams.COMPLETE
            self.create_archive(run)

            result = TrajectoryResult(oits_params = run)
            result.populate_values_from_output_file()

        except Exception as e:
            result = TrajectoryResult(oits_params = run)
            result.exception = str(e)
            result.save()
            run.status = OitsParams.ERROR


        run.save()
        print('Completed {0}'.format(run.uid))

        self.executing_threads.pop(run.id)


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




