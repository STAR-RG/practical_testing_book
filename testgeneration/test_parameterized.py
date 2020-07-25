import pytest
from covertable import make

def important_function(pressure, volume, velocity, low_fuel):
    if pressure < 10:
        if volume > 300:
            if velocity == 5:
                do_something_bad()
        elif low_fuel:
            do_something_good()
    else:
        do_something_good()
 
def do_something_good():
    pass
 
def do_something_bad():
    raise Exception("A bug happened!")

@pytest.mark.parametrize(["pressure", "volume", "velocity", "low_fuel"],
    make([[5,10,15],
        [200, 300, 400],
        [1, 2, 3, 4, 5],
        [True, False]], length=3)
)
def test_important_function(pressure, volume, velocity, low_fuel):
    important_function(pressure, volume, velocity, low_fuel)