class Toast:

    def __init__(
        self,
        length=0.12,
        width=0.10,
        bread_thickness=0.015,
        pb_thickness=0.003,
        mass_bread=0.033,
        mass_pb=0.010,
        table_height=0.75
    ):

        self.length = length
        self.width = width
        self.bread_thickness = bread_thickness
        self.pb_thickness = pb_thickness

        self.mass_bread = mass_bread
        self.mass_pb = mass_pb

        self.x = 0.0
        self.y = table_height

        self.vx = 0.0
        self.vy = 0.0

        self.theta = 0.0      # PB side initially faces upward
        self.omega = 0.0
    
    def center_of_mass(self):
        y_bread = self.bread_thickness / 2
        y_pb = self.bread_thickness + (self.pb_thickness / 2)
        y_com = ((self.mass_bread * y_bread) + (self.mass_pb * y_pb)) / (self.mass_bread + self.mass_pb)
        return y_com
    
    def moment_of_inertia(self):
        y_bread = self.bread_thickness / 2
        y_pb = self.bread_thickness + self.pb_thickness / 2
        y_com = self.center_of_mass()
        d_bread = abs(y_bread - y_com)
        d_pb = abs(y_pb - y_com)
        I_bread = (self.mass_bread / 12 * (self.length**2 + self.bread_thickness**2))
        I_pb = (self.mass_pb / 12 * (self.length**2 + self.pb_thickness**2))
        I_bread_total = I_bread + self.mass_bread * d_bread**2
        I_pb_total = I_pb + self.mass_pb * d_pb**2
        I_total = I_bread_total + I_pb_total
        return I_total

if __name__ == "__main__":

    my_toast = Toast()

    print(f"Total center of mass = {my_toast.center_of_mass()*1000:.2f} mm")
    print(f"Total Moment of Inertia = {my_toast.moment_of_inertia():.6e} kg·m²")