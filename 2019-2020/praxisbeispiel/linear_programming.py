from pulp import *


# Man könnte auch direkt Funktionen von vorheriger Lösung aufrufen.
# Dann könnte man bei neuen Daten vollautomatisch alles neu berechnen.
KE1 = 3.05860622
KE2 = 1.76585626
KE3 = 13.69481487
KE4 = -11.28930098
KE5 = 19.86780881
KE6 = -1.24669877
KE7 = 8.53057966
KE8 = 6.3504065
KE9 = 2.42236723
KE10 = 0.09754178
KE11 = -0.79181241


"""
# Weiterführender Tipp: Enum statt Stringkonstanten verwenden
# * Tippfehler ausgeschlossen
# * Klarheit über mögliche Werte

from enum import Enum

class Umgebungsbedingung(Enum):
    UB1 = "UB1"
    UB2 = "UB2"
    UB3 = "UB3"

TE = {
    Umgebungsbedingung.UB1: 45,
    Umgebungsbedingung.UB2: 84,
    Umgebungsbedingung.UB3: 35,
}

"""

TE = {"ub1": 13.0, "ub2": 22.0, "ub3": 31.0}
RL = {"ub1": 45.0, "ub2": 62.0, "ub3": 77.0}
LA = {"bt1": 120.0, "bt2": 100.0, "bt3": 200.0}
MATK = {
    "ft1": {"bt1": 5.00, "bt2": 4.00, "bt3": 6.00},
    "ft2": {"bt1": 3.00, "bt2": 2.00, "bt3": 4.00},
    "ft3": {"bt1": 1.00, "bt2": 0.50, "bt3": 1.50},
    "ft4": {"bt1": 2.00, "bt2": 1.00, "bt3": 3.00},
}
LAMZ = [12, 5, 24]
PRODK = {
    ft_k: {bt_k: 1.0 for bt_k in ["bt1", "bt2", "bt3"]}
    for ft_k in ["ft1", "ft2", "ft3", "ft4"]
}
BH = [480.0, 200.0, 960.0]
BL = [13000, 9000, 18000]
VK = {
    "ub1": {"bt1": 0.09, "bt2": 0.18, "bt3": 0.03,},
    "ub2": {"bt1": 0.15, "bt2": 0.30, "bt3": 0.05,},
    "ub3": {"bt1": 0.06, "bt2": 0.12, "bt3": 0.02,},
}
LFK = [5.00, 4.00, 7.00]
LAMP = 230
# Konstanten werden auch gerne in Datei "constants.py" geschrieben um sie
# deutlich vom restlichen Code zu trennen:
# import constants
# f(constants.LAMP)


umgebungsbedingungen = ["ub" + str(i) for i in range(1, 4)]
bindertypen = ["bt" + str(i) for i in range(1, 4)]


def make_var(name):
    return LpVariable.dicts(name, (umgebungsbedingungen, bindertypen), lowBound=0)


S1 = make_var("S1")
S2 = make_var("S2")
S3 = make_var("S3")
LF = make_var("LF")
HLB = make_var("HLB")
HKB = make_var("HKB")
HBH = make_var("HBH")
HBB = make_var("HBB")
HKS = make_var("HKS")
# LP-Variablen sind hier global. Bei komplexeren Programmen sollten sie immer
# in einem eigenen Bereich definiert nud dann mitgegeben werden, z.b. als Dict:
# lp_variables = { key: make_var(key) for key in ["S1", "S2", "S3", "LF", "HLB"] }


#  aa(ub, bt) = forall(1 in KOE) KE(koe) * (S1(ub, bt) + S2(ub, bt) + S3(ub, bt))
def aa(ub, bt):
    return KE1 * (S1[ub][bt] + S2[ub][bt] + S3[ub][bt])


# de(ub, bt) = forall(2 in KOE) KE(koe) * LA(bt) + forall(3 in KOE) KE(koe) * TE(ub) + forall(4 in KOE) KE(koe) * RL(ub) + forall(5 in KOE) KE(koe) * LF(ub, bt) + forall(6 in KOE) KE(koe) * (HLB(ub, bt) + HKB(ub, bt))
def de(ub, bt):
    return (
        KE2 * LA[bt]
        + KE3 * TE[ub]
        + KE4 * RL[ub]
        + KE5 * LF[ub][bt]
        + KE6 * (HLB[ub][bt] + HKB[ub][bt])
    )


# fe(ub, bt) = forall(7 in KOE) KE(koe) * S1(ub, bt) + forall(8 in KOE) KE(koe) * S2(ub, bt) + forall(9 in KOE) KE(koe) * S3(ub, bt)
def fe(ub, bt):
    return KE7 * S1[ub][bt] + KE8 * S2[ub][bt] + KE9 * S3[ub][bt]


# hm(ub, bt) = forall(10 in KOE) KE(koe) * LA(bt) + forall(11 in KOE) KE(koe) * (HLB(ub, bt) + HBH(ub, bt) + HKB(ub, bt))
def hm(ub, bt):
    return KE10 * LA[bt] + KE11 * (HLB[ub][bt] + HBH[ub][bt] + HKB[ub][bt])


def define_restrictions(prog):
    # forall(ub in UB, bt in BT) de(ub, bt) <= 100
    # forall(ub in UB, bt in BT) fe(ub, bt) >= 100
    for ub in umgebungsbedingungen:
        for bt in bindertypen:
            prog += de(ub, bt) <= 100
            prog += fe(ub, bt) >= 100


def define_objective_function(prog):
    # ZF := sum(ub in UB, bt in BT)
    #     VK(ub, bt) * ((LAMP / (aa(ub, bt)/100)) + (hm(ub, bt) * (MATK(ft, bt | ft = 1)+PRODK(ft, bt | ft = 1))) + (ol(ub, bt) * (MATK(ft, bt | ft = 2)+PRODK(ft, bt | ft = 2))) + (au(ub, bt) * (MATK(ft, bt | ft = 3)+PRODK(ft, bt | ft = 3))) + (sl(ub, bt) * (MATK(ft, bt | ft = 4)+PRODK(ft, bt | ft = 4))) + (LAMP / (aus(ub, bt))) + (LF(ub, bt) * LFK(bt)))
    prog += lpSum(
        [
            VK[ub][bt] * ((1 / LAMP) * (aa(ub, bt) * 0.01))
            + (hm(ub, bt) * (MATK["ft1"][bt] + PRODK["ft1"][bt]))
            for ub in umgebungsbedingungen
            for bt in bindertypen
        ]
    )


def solve_program():
    prog = LpProblem("pulp", LpMinimize)
    define_restrictions(prog)
    define_objective_function(prog)
    status = prog.solve()
    print("Result:", LpStatus[status])
    for var in prog.variables():
        print(var.name, "=", var.varValue)


if __name__ == "__main__":
    solve_program()
