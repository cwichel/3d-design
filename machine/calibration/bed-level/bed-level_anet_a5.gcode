
; Bed leveling Ender 3 by ingenioso3D
; Modified for Anet A5 by cwichel

G90 ; Absolute positioning
G28 ; Home all axis

G1 Z5 ; Raise Z axis
G1 X50 Y173 ; Move to Position 1
G1 Z0 ; Lower Z axis
M0 Click to continue... ; Pause print

G1 Z5 ; Raise Z axis
G1 X50 Y33 ; Move to Position 2
G1 Z0 ; Lower Z axis
M0 Click to continue... ; Pause print

G1 Z5 ; Raise Z axis
G1 X260 Y33 ; Move to Position 3
G1 Z0 ; Lower Z axis
M0 Click to continue... ; Pause print

G1 Z5 ; Raise Z axis
G1 X260 Y173 ; Move to Position 4
G1 Z0 ; Lower Z axis
M0 Click to continue... ; Pause print

G1 Z5 ; Raise Z axis
G1 X155 Y103 ; Move to Position 5
G1 Z0 ; Lower Z axis
M0 Click to continue... ; Pause print

G1 Z5 ; Raise Z axis
G1 X50 Y33 ; Move to Position 2
G1 Z0 ; Lower Z axis
M0 Click to continue... ; Pause print

G1 Z5 ; Raise Z axis
G1 X260 Y33 ; Move to Position 3
G1 Z0 ; Lower Z axis
M0 Click to continue... ; Pause print

G1 Z5 ; Raise Z axis
G1 X260 Y173 ; Move to Position 4
G1 Z0 ; Lower Z axis
M0 Click to continue... ; Pause print

G1 Z5 ; Raise Z axis
G1 X50 Y173 ; Move to Position 1
G1 Z0 ; Lower Z axis
M0 Click to continue... ; Pause print

G28 ; Home all axis
M84 ; disable motors
