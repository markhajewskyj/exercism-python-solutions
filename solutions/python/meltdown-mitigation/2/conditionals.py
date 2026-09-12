# Ex004 conditionals
# Project: define six tasks to manage currency exchange and count value and number of notes (bills)
# # Created: 2026-06-16
# Revision History:
# v1: Initial setup and basic logic.
# v2: Simplified logic for is_critically_balanced. Corrected logic for reactor_efficiency.
# v3: Corrected condition for fail_safe (>= instead of > =). 


"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):
    """Verify criticality is balanced.

    Parameters:
        temperature (int or float): The temperature value in kelvin.
        neutrons_emitted (int or float): The number of neutrons emitted per second.

    Returns:
        bool: Is criticality balanced?

    Note:
        A reactor is said to be balanced in criticality if it satisfies the following conditions:
            - The temperature is less than 800 K.
            - The number of neutrons emitted per second is greater than 500.
            - The product of temperature and neutrons emitted per second is less than 500000.

    """

    return temperature < 800 and neutrons_emitted > 500 and (temperature * neutrons_emitted < 500000)

def reactor_efficiency(voltage, current, theoretical_max_power):
    """Assess reactor efficiency zone.

    Parameters:
        voltage (int or float): Voltage value.
        current (int or float): Current value.
        theoretical_max_power (int or float): The power level that corresponds to a 100% efficiency.

    Returns:
        str: One of ('green', 'orange', 'red', or 'black').

    Note:
        Efficiency can be grouped into 4 bands:
            1. green -> efficiency of 80% or more,
            2. orange -> efficiency of less than 80% but at least 60%,
            3. red -> efficiency below 60%, but still 30% or more,
            4. black ->  less than 30% efficient.

        The percentage value is calculated as
        (generated power/ theoretical max power)*100
        where generated power = voltage * current
    """

    reactor_efficiency_calculation = ((voltage * current) / theoretical_max_power) * 100

    if reactor_efficiency_calculation < 30:
        efficiency_status = 'black'
    elif reactor_efficiency_calculation < 60:
        efficiency_status = 'red'
    elif reactor_efficiency_calculation < 80:
        efficiency_status = 'orange'
    else:
        efficiency_status = 'green'
    return efficiency_status

def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Assess and return status code for the reactor.

    Parameters:
        temperature (int or float): The value of the temperature in kelvin.
        neutrons_produced_per_second (int or float): The neutron flux.
        threshold (int or float): The threshold for the category.

    Returns:
        str: One of ('LOW', 'NORMAL', 'DANGER').

    Note:
        1. 'LOW' -> `temperature * neutrons per second` < 90% of `threshold`
        2. 'NORMAL' -> `temperature * neutrons per second` +/- 10% of `threshold`
        3. 'DANGER' -> `temperature * neutrons per second` is not in the above-stated ranges
    """

    reactor_status = (temperature * neutrons_produced_per_second) / threshold

    if reactor_status < 0.9:
        safety_level = 'LOW'
    elif 0.9 <= reactor_status <= 1.1:
        safety_level = 'NORMAL'
    else:
        safety_level = 'DANGER'
    print(f'Temp: {temperature} and n.p.sL {neutrons_produced_per_second} and thresh: {threshold}.')
    print(reactor_status)
    print(safety_level)
    return safety_level