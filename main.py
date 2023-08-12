import cv2
import mediapipe

class ReconhecimentoImagem():

    def __init__(self):
        self.non_working_ports = []
        self.is_working = True
        self.dev_port = 0
        self.working_ports = []
        self.available_ports = []

    def print_hi(self, name):
        # Use a breakpoint in the code line below to debug your script.
        print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

    def list_ports(self):
        """
        Test the ports and returns a tuple with the available ports and the ones that are working.
        """
        while len(self.non_working_ports) < 6:  # if there are more than 5 non working ports stop the testing.
            camera = cv2.VideoCapture(self.dev_port)
            if not camera.isOpened():
                self.non_working_ports.append(self.dev_port)
                print("Port %s is not working." % self.dev_port)
            else:
                is_reading, img = camera.read()
                w = camera.get(3)
                h = camera.get(4)
                if is_reading:
                    print("Port %s is working and reads images (%s x %s)" % (self.dev_port, h, w))
                    working_ports.append(self.dev_port)
                else:
                    print("Port %s for camera ( %s x %s) is present but does not reads." % (self.dev_port, h, w))
                    self.available_ports.append(self.dev_port)
            self.dev_port += 1
        return self.available_ports, self.working_ports, self.non_working_ports

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ri = ReconhecimentoImagem()
    ap, wp, nwp = ri.list_ports()
    print(ap, wp, nwp)

