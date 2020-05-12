import numpy as np
import pandas as pd
from numpy.linalg import lstsq


def load_sheets():
    def is_equal_to_x(value):
        return value == 'x'

    sheets = [
        pd.read_excel(
            "Produktionsdaten.xlsx",
            sheet_name=f"{layer}. Schicht",
            index_col=0,
            converters={
                'offene Leimfugen': is_equal_to_x,
                'Hit & Miss': is_equal_to_x,
            },
        )
        for layer in range(1, 6)
    ]
    transformed_sheets = [
        sheet.rename(columns={"Lamellenbreite - Fertigmaß [mm]": "Lamellenbreite [mm]"})
        for sheet in sheets
    ]
    return transformed_sheets


def calculate_coefficient_1(sheets):
    def calculate_scan_parameter_sum(layer):
        return layer['Scanparameter Röntgen'].mean() + layer['Scanparameter Laser'].mean() + layer['Scanparameter Farbkamera'].mean()


    eq_coefficients = [
        [calculate_scan_parameter_sum(layer)]
        for layer in sheets
    ]

    result = [
        layer['Ausbeute nach Fehlerkappung [%]'].mean()
        for layer in sheets
    ]

    print("Coefficient 1")
    print(lstsq(eq_coefficients, result, rcond=None)[0])


def calculate_coefficients_2_to_6(sheets):
    # KE2*LA_m1 + KE3*TE_m1 + KE4*RL_m1 + KE5*LF_m1 + KE6*(HLB_m1+HKB_m1) = de_m1
    eq_coefficients = [
        [
            layer['Lamellenbreite [mm]'].mean(),
            layer['Temperatur [°C]'].mean(),
            layer['rel. Luftfeuchtigkeit [%]'].mean(),
            layer['Leimfaktor'].mean(),
            layer['Hobelmaß Lamellenhobel Breitseite [mm]'].mean() + layer['Hobelmaß Keilzinkung Breitseite [mm]'].mean(),
        ]
        for layer in sheets
    ]
    
    result = [
        layer['Delaminierung %'].mean()
        for layer in sheets
    ]
    x, residuals, _, _ = lstsq(eq_coefficients, result, rcond=None)
    
    print("\nCoefficient 2-6")
    print("solution", x)
    print("residuals", residuals)


def calculate_coefficients_7_to_9(sheets):
    # KE7*S1_m1 + KE8*S2_m1 + KE9*S3_m1 = fe_m1
    eq_coefficients = [
        [
            layer['Scanparameter Röntgen'].mean(),
            layer['Scanparameter Laser'].mean(),
            layer['Scanparameter Farbkamera'].mean(),
        ]
        for layer in sheets
    ]
    result = [
        layer['Festigkeit %'].mean()
        for layer in sheets
    ]
    x, residuals, _, _ = lstsq(eq_coefficients, result, rcond=None)
    
    print("\nCoefficient 7-9")
    print("solution", x)
    print("residuals", residuals)


def calculate_coefficients_10_to_11(sheets):
    #   KE10*LA_m1 + KE11*(HLB_m1+HBH_m1+HKB_m1) = hm_s1
    eq_coefficients = [
        [
            layer['Lamellenbreite [mm]'].mean(),
            layer['Hobelmaß Lamellenhobel Breitseite [mm]'].mean() + layer['Hobelmaß Binderhobel Höhe [mm]'].mean() + layer['Hobelmaß Keilzinkung Breitseite [mm]'].mean(),

        ]
        for layer in sheets
    ]
    result = [
        layer['Hit & Miss'].sum()
        for layer in sheets
    ]
    x, residuals, _, _ = lstsq(eq_coefficients, result, rcond=None)
    print("\nCoefficient 10-11")
    print("solution", x)
    print("residuals", residuals)
    

sheets = load_sheets()
# calculate_coefficient_1(sheets)
# calculate_coefficients_2_to_6(sheets)
# calculate_coefficients_7_to_9(sheets)
calculate_coefficients_10_to_11(sheets)