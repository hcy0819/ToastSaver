from toast import Toast
import physics
import numpy as np
import animation
import matplotlib.pyplot as plt

def peanut_butter_side_down(toast):
    return np.cos(toast.theta) < 0

def main():
    # User input
    bread_length = float(input("Bread length (cm): ")) / 100
    bread_width = float(input("Bread width (cm): ")) / 100
    bread_thickness = float(input("Bread thickness (cm): ")) / 100

    bread_mass = float(input("Bread mass (g): ")) / 1000

    pb_thickness = float(input("Peanut butter thickness (mm): ")) / 1000
    pb_mass = float(input("Peanut butter mass (g): ")) / 1000

    table_height = float(input("Table height (cm): ")) / 100

    toast = Toast(
        length=bread_length,
        width=bread_width,
        bread_thickness=bread_thickness,
        pb_thickness=pb_thickness,
        mass_bread=bread_mass,
        mass_pb=pb_mass,
        table_height=table_height
    )

    # Temporary values
    toast.vx = 0.5
    toast.omega = 5.0
    dt = 0.001
    time = 0.0
    frame = 0
    fig, ax = plt.subplots()

    while toast.y > toast.bread_thickness / 2:
        physics.update(toast, dt)
        print(toast.y)
        if frame % 20 == 0:
            animation.draw_toast(ax, toast)
        time += dt
        frame += 1
    plt.show()

    print(f"\nFlight time = {time:.3f} s")
    print(f"Final angle = {toast.theta:.3f} rad")
    print(f"Final angle = {np.degrees(toast.theta):.1f}°")

    if peanut_butter_side_down(toast):
        print("🥜 Peanut butter side DOWN!")
    else:
        print("🍞 Peanut butter side UP!")

if __name__ == "__main__":
    main()