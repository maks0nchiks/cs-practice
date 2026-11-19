import numpy as np


def make_hours() -> list[int]:
    massive = np.arange(0, 22, 3).tolist()
    return massive

def vector_report(values: list[float]) -> dict:
    array_values = np.asarray(values)
    slovar = {}
    
    slovar["third"] = float(array_values[2])
    slovar["last"] = float(array_values[-1])
    slovar["midle"] = list(map(float, array_values[2:6].tolist()))
    slovar["every_second"] = list(map(float, array_values[::2].tolist()))
    slovar["reversed"] = list(map(float, array_values[::-1].tolist()))
    return slovar


def change_vector(values: list[float]) -> list[float]:
    values_inward = np.asarray(values).copy()
    
    values_inward[1:4] = 99
    values_inward[::2] = -1
    return values_inward.tolist()


def cap_above(values: list[float], limit: float) -> list[float]:
    array_values = np.asarray(values)
    array_values[array_values > limit] = limit
    return array_values.tolist()


def celsius_to_fahrenheit(values: list[float]) -> list[float]:
    rr_vls = np.asarray(values)
    
    nw_rr_vls = rr_vls * 9 / 5 + 32
    return nw_rr_vls.tolist()