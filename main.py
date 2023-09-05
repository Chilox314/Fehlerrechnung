#!\usr\bin\env python3
import sys
import numpy as np
import argparse

def main():
    args = parsecommandline(sys.argv[1:])
    filename = "test.txt"
    #filename = sys.argv[1]
    try:
        stream = open(filename,"r")
    except IOError as err:
        sys.stderr.write("{}: {}\n".format(sys.argv[0], err))
        exit(1)
    if args.statistical_values:
        
        l = analyze(stream)
        save(l)
    stream.close()

def parsecommandline(argv):
    p = argparse.ArgumentParser(description="calculate statistical values of some measurements")
    
    #p.add_argument('inputfile',type=str,help='inputfile with whitespace or tabseparated values')
    p.add_argument('-s','--statistical_values',action="store_true")
    p.add_argument('-l','--linear_regression',action="store_true")
    p.add_argument('-f','--fehlerfortpflanzungsgesetz',action="store_true")

    return p.parse_args(argv)

def analyze(input_stream):
    
    l = list()
    for line in input_stream:
        line.rstrip()
        line_list = line.split()
        var = dict()

        var["name"] = line_list[0]
        var["values"] = np.array([float(x) for x in line_list[1:]])
        var["n"] = len(var["values"])

        print(var)
        var = calculate(var)

        print(var) 
        l.append(var)
    return l

def calculate(d):

    d["mittelwert"] = np.around(1 / d["n"] * np.sum(d["values"]))

    d["standardabweichung_einzel"] = np.around(np.sqrt(1 / (d["n"] - 1) * np.sum((d["values"] - d["mittelwert"])**2)), decimals=4) 

    d["standardabweichung_mittel"] = np.around(d["standardabweichung_einzel"] / np.sqrt(d["n"]), decimals=4)

    return d

def plot():
    return 1

def toLatex():
    return 1

def save(var_list):

    try:
        file = open("result.txt", 'a')
    except IOError as err:
        sys.stderr.write("{}: {}\n".format(sys.argv[0], err))
        exit(1)

    for elem in var_list:
        file.write("{}: Mittelwert = {}, Standardabweichung(einzeln) = {}, Standardabweichung(Mittelwert) = {}\n"\
                   .format(elem["name"],elem["mittelwert"],elem["standardabweichung_einzel"],elem["standardabweichung_mittel"]))
        
    file.close()


if __name__ == "__main__":
    main()