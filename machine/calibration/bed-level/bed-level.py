from math import ceil


# ===============================================
printers = {
    "Ender 3": {
        "X": {"max": 235, "off": 0, "inv": False},
        "Y": {"max": 235, "off": 9, "inv": False}
    },
    "Anet A5":  {
        "X": {"max": 300, "off": 5, "inv": False},
        "Y": {"max": 200, "off": 3, "inv": True}
    },
    "Anet A8": {
        "X": {"max": 220, "off": 0, "inv": False},
        "Y": {"max": 220, "off": 0, "inv": False}
    }
}

cord_mod = 0.15

cord_seq = [0, 1, 2, 3, 4, 1, 2, 3, 0]


# ===============================================
code_head = """
; Bed leveling Ender 3 by ingenioso3D
; Modified for {} by cwichel

G90 ; Absolute positioning
G28 ; Home all axis
"""

code_foot = """
G28 ; Home all axis
M84 ; disable motors
"""

code_move = """
G1 Z5 ; Raise Z axis
G1 X{} Y{} ; Move to Position {}
G1 Z0 ; Lower Z axis
M0 Click to continue... ; Pause print
"""


# ===============================================
def get_cords(printer):
    if printer in printers:
        cord = dict()
        data = printers[printer]

        for axis in data:
            base = round(cord_mod * data[axis]["max"])
            cord_min = data[axis]["off"] + base
            cord_max = data[axis]["off"] + data[axis]["max"] - base

            if data[axis]["inv"]:
                cord[axis] = {"min": cord_max, "max": cord_min}
            else:
                cord[axis] = {"min": cord_min, "max": cord_max}

            cord[axis]["C"] = ceil((cord_min + cord_max)/2)

        return cord


def get_points(cords):
    x = cords["X"]
    y = cords["Y"]

    return [
        [x["min"], y["min"]],
        [x["min"], y["max"]],
        [x["max"], y["max"]],
        [x["max"], y["min"]],
        [x["C"],   y["C"]]
    ]


def get_move_code(points):
    code = ""
    for point in cord_seq:
        code += code_move.format(points[point][0], points[point][1], (point + 1))

    return code


# ===============================================
def get_full_code(printer):
    # start code
    code = code_head.format(printer)

    # get the movement code
    cords = get_cords(printer)
    points = get_points(cords)
    code += get_move_code(points)

    # Finish
    code += code_foot

    return code


# ===============================================
def execute():
    for printer in printers:
        name = printer.replace(" ", "_")
        code = get_full_code(printer)
        file = open("Bed_Level_{}.gcode".format(name), "w")
        file.write(code)
        file.close()
