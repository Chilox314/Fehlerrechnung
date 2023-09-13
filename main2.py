#!\usr\bin\env python3
import numpy as np
import matplotlib.pyplot as plt

def main():
    x = input("Was möchtest du berechnen? (s: statistische Werte, l: lineare Regression, f: Fehlerfortpflanzungsgesetz)\n")
    if x == "s":
        n = len(inputarray)
        mean = np.mean(inputarray)
        standard_einzel = np.sqrt(1/(n-1) * np.sum((inputarray - mean)**2))
        standard_mittel = standard_einzel/ np.sqrt(n)
        print("Für die Werte {} ergeben sich mit n={}:\n Mittelwert={}\n Standardabweichungen:\n Einzel={}\n Mittel={}\n"\
              .format(inputarray,n,mean,standard_einzel,standard_mittel))
    elif x == "l":
        x_array = np.array([float(x) for x in input("Gib die x-Werte mit Leerzeichen separiert ein:\n").split()])
        y_array = np.array([float(y) for y in input("Gib die y-Werte mit Leerzeichen separiert ein:\n").split()])
        #x_array = np.array([float(x) for x in "8 18 28 38 48".split()])
        #y_array = np.array([float(y) for y in "1000.18 1000.41 1000.64 1000.88 1001.13".split()])

        n = len(x_array)

        x_mean = np.mean(x_array)
        y_mean = np.mean(y_array)

        b = (np.sum(x_array * y_array) - n*x_mean * y_mean) / (np.sum(x_array ** 2) - n * x_mean**2)
        a = y_mean - b*x_mean

        d = y_array - b * x_array - a

        s_b = np.sqrt(1/(n-2) * (np.sum(d**2)) / (np.sum((x_array - x_mean) ** 2)))
        s_a = s_b * np.sqrt(np.sum(x_array ** 2)) / n
        s_y = np.sqrt(np.sum(d ** 2)) / (n-2)
        print("x_mean={:.4f}, y_mean={:.4f}, b={:.8f}, a={:.8f}, s_b={:.4e}, s_a={:.4e}".format(x_mean, y_mean, b, a, s_b, s_a))
        

if __name__ == "__main__":
    main()