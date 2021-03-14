machines = ["Maschine A", "Maschine K", "Maschine L"]
thickness = pd.Series([4.3, 1.2, 2.2], index=machines)
speed = pd.Series([100, 50, 80], index=machines)
machines_frame = pd.concat(
    {'speed': speed, 'thickness': thickness},
    axis='columns',
)
