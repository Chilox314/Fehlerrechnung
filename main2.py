#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

def main():
    x = input("Was möchtest du berechnen? (s: statistische Werte, l: lineare Regression, f: Fehlerfortpflanzungsgesetz)\n")
    if x == "s":
        inputarray = np.array([float(x) for x in input("Gib deine Werte mit Leerzeichen separiert ein:\n").split()])
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
        if input("Willst du das Ergebnis plotten?\n") == "y":
            print(1)
            fig, ax = plt.subplots(figsize=(10,6.18))
            ax.set_xlabel(input("X-Achse?\n"))
            ax.set_ylabel(input("Y-Achse?\n"))
            ax.set_ylim(0,(1.1) * np.max(y_array))
            ax.set_xlim(0,1.1 * np.max(x_array))
            ax.scatter(x_array,y_array,color="red")

            x_max = np.ceil(np.max(x_array))
            x_list = np.linspace(0, x_max, 5)
            y_list = b * x_list + a

            ax.plot(x_list,y_list)
            fig.savefig("figure.pdf")

if __name__ == "__main__":
    main()