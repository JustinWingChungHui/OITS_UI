from django.core.management.base import BaseCommand
from django.conf import settings
from oits_params.models import OitsParams
from pathlib import Path
import sys

class Command(BaseCommand):

    def handle(self, *args, **options):


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
            OITS_instance = OITS_optimizer()
            OITS_instance.set_OITS(
                    0,
                    "Juice",
                    7,
                    ["3","3","2","3","4","3","5"],
                    0,
                    [10.0],
                    [0.1],
                    [0.2],
                    [0.0],
                    [1.0],
                    [0.0],
                    [1.0],
                    "2022 Jun 01",
                    "2022 May 11",
                    "2022 Jun 11",
                    [0.0,363.0,145.0,315.0,163.0,652.0,1094.0],
                    [0.0,350.0,120.0,300.0,150.0,620.0,1000.0],
                    [0.0,380.0,150.0,350.0,170.0,660.0,1150.0],
                    [200.0,200.0,200.0,200.0,200.0,200.0,200.0],
                    [0.0,0.0,0.0,0.0,0.0,0.0,0.0],
                    [0.0,0.0,0.0,0.0,0.0,0.0],
                    0,
                    0.0,
                    1,
                    0,
                    1000,
                    1.0,
                    1,
                    [oits_lib_path + "SPICE/de430.bsp"],
                    oits_lib_path + "SPICE/naif0012.tls")

            OITS_instance.convert_python_to_C()
            OITS_instance.OITS()

            print('Run {0} complete'.format(run.uid))
            run.status = OitsParams.COMPLETE
            run.save()
