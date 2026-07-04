g = 9.81  # m/s^2

def update(toast, dt):
    toast.vy -= g * dt

    toast.x += toast.vx * dt
    toast.y += toast.vy * dt

    toast.theta += toast.omega * dt