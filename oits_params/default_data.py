# JUICE ESA Mission
esa_mission = '''{
    "trajectory_optimization": true,
    "Nbody": 7,
    "ID": ["3","3","2","3","4","3","5"],
    "NIP": 0,
    "rIP": [10.0],
    "thetaIP": [0.1],
    "thiIP": [0.2],
    "thetalb": [0.0],
    "thetaub": [1.0],
    "thilb":[0.0],
    "thiub": [1.0],
    "t01": "2022 Jun 01",
    "tmin1": "2022 May 11",
    "tmax1": "2022 Jun 11",
    "t0": [0.0,363.0,145.0,315.0,163.0,652.0,1094.0],
    "tmin": [0.0,350.0,120.0,300.0,150.0,620.0,1000.0],
    "tmax": [0.0,380.0,150.0,350.0,170.0,660.0,1150.0],
    "Periacon": [200.0,200.0,200.0,200.0,200.0,200.0,200.0],
    "dVcon": [0.0,0.0,0.0,0.0,0.0,0.0,0.0],
    "Perihcon": [0.0,0.0,0.0,0.0,0.0,0.0],
    "Duration": 0.0,
    "PROGRADE_ONLY": true,
    "RENDEZVOUS": true,
    "Ndata": 1000,
    "RUN_TIME": 1,
    "BSP": ["de430.bsp"]
}
'''

# BORISOV / 7 Solar Radii
borisov_7_solar_radii = '''{
    "trajectory_optimization": true,
    "Nbody": 6,
    "ID": ["3","INTERMEDIATE POINT","3","5","INTERMEDIATE POINT","1003639"],
    "NIP": 2,
    "rIP": [3.2,0.03255],
    "thetaIP": [0.0,0.1],
    "thiIP": [0.0,0.0],
    "thetalb": [-3.141952,-3.14952],
    "thetaub": [3.14952,3.14592],
    "thilb":[-1.04719, -1.04719],
    "thiub": [1.04719, 1.04719],
    "t01": "2027 feb 01",
    "tmin1": "2026 Nov 01",
    "tmax1": "2027 Apr 01",
    "t0": [0.0,555,555.0,500.0,500.0,7238.0],
    "tmin": [0.0,500.0,500.0,10.0,10.0,100.0],
    "tmax": [0.0,600.0,600.0,1000.0,1000.0,7238.0],
    "Periacon": [0.0,0.0,200.0,200.0,0.0,0.0],
    "dVcon": [0.0,0.0,0.0,0.0,0.0,0.0,0.0],
    "Perihcon": [0.0,0.0,0.0,0.0325,0.0325],
    "Duration": 0.0,
    "PROGRADE_ONLY": false,
    "RENDEZVOUS": false,
    "Ndata": 1000,
    "RUN_TIME": 20,
    "BSP": ["BORISOV_24-11-2019.bsp","de430.bsp"]
}
'''

# OUMUAMUA / 6 Solar Radii
oumuamua_6_solar_radii = '''{
    "trajectory_optimization": true,
    "Nbody": 6,
    "ID": ["3","INTERMEDIATE POINT","3","5","INTERMEDIATE POINT","3788040"],
    "NIP": 2,
    "rIP": [3.2,0.02795],
    "thetaIP": [0.0,0.1],
    "thiIP": [0.0,0.0],
    "thetalb": [-3.141952,-3.14952],
    "thetaub": [3.14952,3.14592],
    "thilb":[-1.04719, -1.04719],
    "thiub": [1.04719, 1.04719],
    "t01": "2030 jun 01",
    "tmin1": "2030 jan 01",
    "tmax1": "2031 jan 01",
    "t0": [0.0,555.0,555.0,500.0,500.0,6000.0],
    "tmin": [0.0,500.0,500.0,10.0,10.0,100.0],
    "tmax": [0.0,600.0,600.0,1000.0,1000.0,6000.0],
    "Periacon": [0.0,0.0,200.0,200.0,0.0,0.0],
    "dVcon": [0.0,0.0,0.0,0.0,0.0,0.0],
    "Perihcon": [0.0,0.0,0.0,0.0279,0.0279],
    "Duration": 0.0,
    "PROGRADE_ONLY": false,
    "RENDEZVOUS": false,
    "Ndata": 1000,
    "RUN_TIME": 20,
    "BSP": ["extrasolar.bsp","de430.bsp" ]
}
'''

# CASSINI
cassini = '''{
    "trajectory_optimization": true,
    "Nbody": 7,
    "ID": ["3","2","INTERMEDIATE POINT","2","3","5","6"],
    "NIP": 1,
    "rIP": [1.57],
    "thetaIP": [0.0],
    "thiIP": [0.0],
    "thetalb": [-3.141952],
    "thetaub": [3.14952],
    "thilb":[-1.04719],
    "thiub": [1.04719],
    "t01": "1997 nov 01",
    "tmin1": "1997 Sep 01",
    "tmax1": "1998 feb 01",
    "t0": [0.0,162.0,206.0,300.0,10.0,500.0,600.0],
    "tmin": [0.0,100.0,170.0,50.0,10.0,100.0,200.0],
    "tmax": [0.0,190.0,230.0,1000.0,550.0,2000.0,3000.0],
    "Periacon": [0.0,200.0,0.0,200.0,200.0,200.0,0.0],
    "dVcon": [0.0,0.0,0.0,0.0,0.0,0.0,0.0],
    "Perihcon": [0.0,200.0,0.0,200.0,200.0,200.0,0.0],
    "Duration": 213013800,
    "PROGRADE_ONLY": true,
    "RENDEZVOUS": true,
    "Ndata": 1000,
    "RUN_TIME": 20,
    "BSP": ["de430.bsp" ]
}
'''

# BORISOV via Jupiter * 2
borisov_via_jupiter2 = '''{
    "trajectory_optimization": true,
    "Nbody": 6,
    "ID": ["3","3","5","INTERMEDIATE POINT","5","1003639"],
    "NIP": 1,
    "rIP": [5.2],
    "thetaIP": [0.1],
    "thiIP": [0.2],
    "thetalb": [-3.141952],
    "thetaub": [3.14952],
    "thilb":[-1.04719],
    "thiub": [1.04719],
    "t01": "2021 Jun 01",
    "tmin1": "2021 Jan 01",
    "tmax1": "2022 Jan 01",
    "t0": [0.0,363.0,500.0,1087.0,1087,8000.0],
    "tmin": [0.0,320.0,10.0,950.0,950,1000.0],
    "tmax": [0.0,400.0,1000.0,1200,1200.0,8100.0],
    "Periacon": [0.0,200.0,200.0,0.0,200.0,0.0],
    "dVcon": [0.0,0.0,0.0,0.0,0.0,0.0],
    "Perihcon": [0.0,0.0,0.0,0.0,0.0],
    "Duration": 0.0,
    "PROGRADE_ONLY": false,
    "RENDEZVOUS": false,
    "Ndata": 200,
    "RUN_TIME": 20,
    "BSP": ["BORISOV_24-11-2019.bsp","de430.bsp" ]
}
'''

# EARTH TO VENUS (Trajectory Calculation Only)
earth_to_venus = '''{
    "trajectory_optimization": false,
    "Nbody": 2,
    "ID": ["3","2"],
    "NIP": 0,
    "rIP": [10.0],
    "thetaIP": [0.1],
    "thiIP": [0.2],
    "thetalb": [0.0],
    "thetaub": [1.0],
    "thilb": [0.0],
    "thiub": [1.0],
    "t01": "2020 Jun 01",
    "tmin1": "2020 Jan 01",
    "tmax1": "2021 Jan 01",
    "t0": [0.0,50.0],
    "tmin": [0.0,20.0],
    "tmax": [0.0,500.0],
    "Periacon": [0.0,0.0],
    "dVcon": [0.0,0.0],
    "Perihcon": [0.0],
    "Duration": 0.0,
    "PROGRADE_ONLY": true,
    "RENDEZVOUS": true,
    "Ndata": 200,
    "RUN_TIME": 20,
    "BSP": ["de430.bsp" ]
}
'''


example_list = [
    {"name": 'ESA Mission', "value": esa_mission},
    {"name": 'OUMUAMUA / 6 Solar Radii', "value": oumuamua_6_solar_radii},
    {"name": 'Cassini', "value": cassini},
    {"name": 'BORISOV via Jupiter * 2', "value": borisov_via_jupiter2},
    {"name": 'Earth to Venus Trajectory Only', "value": earth_to_venus}
]
