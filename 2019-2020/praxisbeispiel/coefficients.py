import numpy as np
from numpy.linalg import lstsq
import pandas as pd


def calculate_coefficient_1_version_1(layers):
    eq_coefficients = [
        [
            layer["Scanparameter Röntgen"].mean()
            + layer["Scanparameter Laser"].mean()
            + layer["Scanparameter Farbkamera"].mean()
        ]
        for layer in layers
    ]

    eq_result = [layer["Ausbeute nach Fehlerkappung [%]"].mean() for layer in layers]

    x, residuals, _, _ = lstsq(eq_coefficients, eq_result, rcond=None)

    print("Coefficient 1 is", x[0], "with residuals", residuals)

    return x[0]


def calculate_coefficient_1_version_2(layers):
    eq_coefficients = []
    eq_result = []

    for layer in layers:
        eq_coefficients.append(
            [
                layer["Scanparameter Röntgen"].mean()
                + layer["Scanparameter Laser"].mean()
                + layer["Scanparameter Farbkamera"].mean()
            ]
        )
        eq_result.append(layer["Ausbeute nach Fehlerkappung [%]"].mean())

    x, residuals, _, _ = lstsq(eq_coefficients, eq_result, rcond=None)

    print("Coefficient 1 is", x[0], "with residuals", residuals)

    return x[0]


def calculate_coefficient_1_version_3(layers):
    equations = [
        {
            "coefficients": [
                layer["Scanparameter Röntgen"].mean()
                + layer["Scanparameter Laser"].mean()
                + layer["Scanparameter Farbkamera"].mean()
            ],
            "result": layer["Ausbeute nach Fehlerkappung [%]"].mean(),
        }
        for layer in layers
    ]
    x, residuals, _, _ = lstsq(
        [eq["coefficients"] for eq in equations],
        [eq["result"] for eq in equations],
        rcond=None,
    )

    print("Coefficient 1 is", x[0], "with residuals", residuals)

    return x[0]


def calculate_coefficients_2_to_6(layers):
    # KE2*LA_m1 + KE3*TE_m1 + KE4*RL_m1 + KE5*LF_m1 + KE6*(HLB_m1+HKB_m1) = de_m1
    coefficients = [
        [
            layer['Lamellenbreite [mm]'].mean(),
            layer['Temperatur [°C]'].mean(),
            layer['rel. Luftfeuchtigkeit [%]'].mean(),
            layer['Leimfaktor'].mean(),
            layer['Hobelmaß Lamellenhobel Breitseite [mm]'].mean()
            + layer['Hobelmaß Keilzinkung Breitseite [mm]'].mean(),
        ]
        for layer in layers
    ]
    results = [
        layer['Delaminierung %'].mean()
        for layer in layers
    ]
    x, residuals, a, b = lstsq(coefficients, results, rcond=None)

    from pprint import pprint
    print("equation for 2-6:")
    pprint(coefficients)
    pprint(results)
    print("Coefficients 2-6 are", x, "with residuals", residuals)
    
    return x


def load_layers():
    layers = [
        pd.read_excel("Produktionsdaten.xlsx", sheet_name=str(sheet_num) + ". Schicht")
        for sheet_num in range(1, 6)
    ]

    column_renamings = {'Lamellenbreite - Fertigmaß [mm]': 'Lamellenbreite [mm]'}
    # NOTE: rename works by copy be default, could also have used in_place=True
    transformed_layers = [
        layer.rename(columns=column_renamings) for layer in layers
    ]
    return transformed_layers


def parse_series_to_bool(series):
    # result as series:
    result = series == 'x'

    # result as list (can be assigned to dataframe as series)
    result = [val == x for val in series]

    # result as series:
    def check_bool(val):
        return val == 'x'

    result = series.map(check_bool)
    

def main():
    layers = load_layers()

    #coefficient_1 = calculate_coefficient_1_version_1(layers=layers)
    #coefficient_1 = calculate_coefficient_1_version_2(layers=layers)
    coefficient_1 = calculate_coefficient_1_version_3(layers=layers)

    coefficients_2_to_6 = calculate_coefficients_2_to_6(layers=layers)
    

main()
