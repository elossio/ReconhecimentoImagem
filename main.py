import cv2
import mediapipe as mp

class ReconhecimentoImagem():

    def __init__(self):
        self.non_working_ports = []
        self.is_working = True
        self.dev_port = 0
        self.working_ports = []
        self.available_ports = []

    def list_ports(self):
        """
        Testa as portas do computador e retorna uma tupla com as portas disponiveis e as portas que estao funcionando.
        """
        while len(self.non_working_ports) < 6:  # Se houver mais do que 5 portas que nao funcionam "non working ports", para o teste!
            webcam = cv2.VideoCapture(self.dev_port)
            if not webcam.isOpened():
                self.non_working_ports.append(self.dev_port)
                print(f"Porta {self.dev_port} nao funciona.")
            else:
                is_reading, img = webcam.read()
                w = webcam.get(3)
                h = webcam.get(4)
                if is_reading:
                    print(f"Porta {self.dev_port} está funcionando e lê imagens ({h} x {w})")
                    self.working_ports.append(self.dev_port)
                else:
                    print(f"Porta {self.dev_port} para camera ({h} x {w}) está presente mas não lê.")
                    self.available_ports.append(self.dev_port)
            self.dev_port += 1
        return self.available_ports, self.working_ports, self.non_working_ports
    
    def selecionar_webcam(self, porta):
        self.dev_port = porta

    def testar_webcam(self):
        webcam = cv2.VideoCapture(self.dev_port)
        if webcam.isOpened():
            self.is_working, image = webcam.read()
            while self.is_working:
                self.is_working, image = webcam.read()
                cv2.imshow("Tela da Camera", image)
                key = cv2.waitKey(2)
                if key == 27: # tecla ESC
                    self.is_working = False
        else:
            print("Não funcionou!")
        webcam.release()
        cv2.destroyAllWindows()

    def reconhecer_maos(self):
        webcam = cv2.VideoCapture(self.dev_port)
        reconhecimento_maos = mp.solutions.hands
        desenho_mp = mp.solutions.drawing_utils
        maos = reconhecimento_maos.Hands()
        if webcam.isOpened():
            self.is_working, image = webcam.read()
            while self.is_working:
                self.is_working, image = webcam.read()
                frameRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                lista_maos = maos.process(frameRGB)
                if lista_maos.multi_hand_landmarks:
                    for mao in lista_maos.multi_hand_landmarks:
                        desenho_mp.draw_landmarks(image, mao, reconhecimento_maos.HAND_CONNECTIONS)
                cv2.imshow("Tela da Camera", image)
                tecla = cv2.waitKey(2)
                if tecla == 27:
                    self.is_working = False
        webcam.release()
        cv2.destroyAllWindows


if __name__ == '__main__':
    ri = ReconhecimentoImagem()
    # ap, wp, nwp = ri.list_ports()
    # print(ap, wp, nwp)
    # ri.testar_webcam()
    ri.reconhecer_maos()




