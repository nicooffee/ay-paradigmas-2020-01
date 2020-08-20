
comm = '''
Verificador para el trabajo 2
'''
# Cambiar dummy por el nombre de el trabajo 2
# En caso de hacerlo en archivos distintos, seria necesario importar cada uno
# y cambiar el como se llama a las clases y metodos:
# -> import intervals as t1, intervalSet as t2 | I1, WI1 = t1.Interval, t2.WeightedInterval... Etc
import dummy as t2

def test():
    print('-'*100)
    S1 = t2.IntervalSet()
    I1, I2, I3 = t2.Interval(1, 4), t2.Interval(0, 2), t2.Interval(3, 5)
    S1.add(I1)
    S2 = S1.cover(I2)
    S3 = S1.free(I3)
    Interval_string = "objeto Interval Resultado: {}. tipo: {}".format(str(I1), type(I1))
    IntervalSet_string = "objeto IntervalSet Resultado: {}. tipo: {}".format(str(S1), type(S1))
    cover_string = "IntervalSet.cover Resultado: {}. tipo: {}".format(str(S2), type(S2))
    free_string = "IntervalSet.free Resultado: {}. tipo: {}".format(str(S3), type(S3))
    WS1 = t2.WeightedIntervalSet()
    WI1, WI2, WI3 = t2.WeightedInterval(1, 4), t2.WeightedInterval(0, 2), t2.WeightedInterval(3, 5)
    WS1.add(WI1)
    WS2 = WS1.cover(WI2)
    WS3 = WS1.free(WI3)
    WeightedInterval_string = "objeto WeightedInterval Resultado: {}. tipo: {}".format(str(WI1), type(WI1))
    WeightedIntervalSet_string = "objeto WeightedIntervalSet Resultado: {}. tipo: {}".format(str(WS1), type(WS1))
    Weighted_cover_string = "WeightedIntervalSet.cover Resultado: {}. tipo: {}".format(str(WS2), type(WS2))
    Weighted_free_string = "WeightedIntervalSet.free Resultado: {}. tipo: {}".format(str(WS3), type(WS3))
    print(Interval_string, IntervalSet_string, cover_string, free_string, sep='\n') # Para guardar los resultados en un archivo, este se puede inicializar (EJ: F = open('print.txt', 'a')) y despues se imprime a este (print(..., file=F))
    print('-'*50)
    print(WeightedInterval_string, WeightedIntervalSet_string, Weighted_cover_string, Weighted_free_string, sep='\n')
    # El resultado de este programa (dado que este en el mismo directorio que el programa, y que sea el nombre del archivo el que se importa)
    # sera de los resultados que entrega utilizando las clases y metodos definidos en este
    # para el resultado esperado, se espera que el objeto que se imprima para los intervalos, sea
    # con el formato definido en el trabajo, por lo que se debiese imprimir:
#objeto Interval Resultado: [start, end]. tipo: <class 'dummy.Interval'>
    # start y end numeros reales
    #
    # ***IMPORTANTE***
    # Para los Sets es un poco mas complicado ya que deben ser iterables por lo que para una correcta prueba final
    # habria que cambiar:
    # str(S1), str(S2), str(S3), str(WS1), str(WS2), str(WS3) -> str([str(interval) for interval in S1]), str([....
    # (reemplazar str(SX) con str([str(interval) for interval in SX]) una vez sean iterables los sets, con X = 1, 2, 3)
    # lo que comprobaria que cada set es iterable: con lo que nos daria una impresion algo asi:
#objeto IntervalSet Resultado: [(start1, end1), (start2, end2),...]. tipo: <class 'dummy.IntervalSet'>
    # Lo mismo aplicaria analogamente para los objetos "Weighted"

if __name__ == "__main__":
    for i in range(20):
        test()
