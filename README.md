El presente proyecto, para el envio de imagenes por medio de modulacion e demudulacion, cuenta primeramente con la funcion brindada en el enunciado como fuente_info, la cual funciona para retornar un vector de pixeles a partir de una imagen, en este caso arenal.jpg
seguidamente le de  rgb_a_b para codiciar en binario los pixeles de la imagen.
La función modulador, se aducuó para cumplir con los requerimientos del proyecto, y se hizo que la modulación fuera por QSPK, donde la moduladora, correspondió a dos señales senoidales, una seno y otra coseno, es decir dos portadoras, aplicando principios de linealidad.
Luego mediante condicionales, en la señal, se eparó el proceso de modulación para las dos moduladores y si hizo que en función del bit siendo 1 o 0, se aplicara que por decirlo la señal tomara la forma de estos bits en forma de señal cuadrada (moduladora) y teniendo una señal resultadnte T_x.
Para términos de graficar la portadora y observar y ender los resultados con claridad, se sumaron ambas señales senoidales de poprtadoras, además se calculó la potencia promedio de la señal modeulada.
A partir del resultadod de la señal modulada, se simula el ruido en la transmisión de la imagen por medio de la señal canal_ruidoso.

para la simulacion con la señal moudulada,demodulada y ruido, se utliza frecuancia, muestras por periodo portadora y una relación de la señal de ruido del canal, y se visuzaliza tanto la señal como las gráficas de las señales con las señales que corresponden al envio de la selañal, de como se modulan los bits, por medio del campio de amplitud o valor en y de la señal T_x




En e punto 2 de asignaciones, por medio de la señal T_x, se grafican 5 funciones, se le saca el periodo teororico y ocn los datos para comprobar ergocidad. En este caso de hace un desplazamineto de fase de 180 grados de dos señales para luego graficarlas juntas, donde una se llama como positiva y la otra como negatica. luego se acomodan en dos vectores de datos separados parala totalidad de los datos para sacar el promedio teorioco, de simulacion y graficar, los promedios dse determinan con mean.

Para determinar la densidad espectral de energía, se usa la fución de scipy fft y con los valores en el tiempo hasta la mitad de la totalidad de las muestras, se grafica hasta 15000 puntos.
