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
    layer = layers[0]
    layer['Lamellenbreite [mm]']
    layer['Temperatur [°C]']
    layer['rel. Luftfeuchtigkeit [%]']
    layer['Leimfaktor']
    layer['Hobelmaß Lamellenhobel Breitseite [mm]']
    layer['Hobelmaß Keilzinkung Breitseite [mm]']
    layer['Delaminierung %']


def load_layers():
    layers = [
        pd.read_excel("Produktionsdaten.xlsx", sheet_name=str(sheet_num) + ". Schicht")
        for sheet_num in range(1, 6)
    ]
    
    column_renamings = {'Lamellenbreite - Fertigmaß [mm]': 'Lamellenbreite [mm]'}
    transformed_layers = [
        layer.rename(columns=column_renamings) for layer in layers
    ]
    return transformed_layers
    

def main():
    layers = load_layers()
    

    coefficient_1 = calculate_coefficient_1_version_1(layers=layers)
    coefficient_1 = calculate_coefficient_1_version_2(layers=layers)
    coefficient_1 = calculate_coefficient_1_version_3(layers=layers)

    calculate_coefficients_2_to_6(layers=layers)
    
    return layers


main()
