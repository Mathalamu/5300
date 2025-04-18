from manim import *
import numpy as np

class StringWave(ThreeDScene):
    def construct(self):
        L = 10 # length of string
        A_z = 0.75    # amplitude in x
        A_y = 2     # amplitude in y
        n_z = 2     # normal mode in z
        n_y = 5        # normal mode in y
        k_z = np.pi*n_z/L      # spatial frequency
        k_y = np.pi*n_y/L      # spatial frequency
        c = 5       # wave speed
        omega_y =  c*np.pi*n_y/L   # angular frequency for y
        omega_z =  c*np.pi*n_z/L   # angular frequency for z
        a = .2         #decay constant
        d1 = 0         # phase constant for y
        d2 = 0         # phase constant for z
        
        # Axes setup
        axes = ThreeDAxes(
            x_range=[-L,L, 1],
            y_range=[-2*A_y, 2*A_y, 1],
            z_range=[-2*A_z, 2*A_z, 1],
            x_length=2*L,
            y_length=4*A_y,
            z_length=4*A_z,
            
        )
        self.set_camera_orientation(phi= 80* DEGREES, theta=-60 * DEGREES,frame_center = [0, 0, 0])
        self.add(axes)
        # Labels
        x_label = axes.get_x_axis_label(Text("x"))
        y_label = axes.get_y_axis_label(Text("y"))
        z_label = axes.get_z_axis_label(Text("z")) 
        self.add(x_label, y_label, z_label)
        #Parameters
        
        #time tracker
        self.t_tracker = ValueTracker(0)  # Renamed from self.time to self.t_tracker

        #string path
        def wave_string(t):
            return ParametricFunction(
                lambda x: np.array([
                    x,  # x
                    np.e**(-a*t)*A_y * np.sin(k_y * x) * np.cos(omega_y * t-d2),  # y
                    np.e**(-a*t)*A_z * np.sin(k_z * x) * np.cos(omega_z * t-d1)  # z
                ]),
                t_range=[0, L],
                color=BLUE
            )
        #update with time
        string = always_redraw(lambda: wave_string(self.t_tracker.get_value()))
        self.add(string)
       

        self.begin_ambient_camera_rotation(rate=0.125)
        #Animate wave
        self.play(self.t_tracker.animate.set_value(2 * PI), run_time=12, rate_func=linear)
        self.wait(1)