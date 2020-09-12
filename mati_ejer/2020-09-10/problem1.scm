#lang scheme

;; SCHEME
;; Existen una serie de alternativas de procedimientos, algunos ejemplos son
;; null? = empty?
;; car = first
;; cdr = rest
;; aunque se puede usar de forma mas interesante c[ad]r por ejemplo
;; cadr = second, caddr = third, cadddr = fourth, etc
;; o cosas aun mas complicadas
;; cadaar = (lambda (lis) (second (first (first lis)))) = (lambda (lis) (first (rest (first (first lis)))))
;; por lo que podemos ver los a y d entre c y r como first y rest dentro  de una construccion de lambda como la de arriba
;;
;; Ademas otra parte interesante del lenguaje son los quote representados por ' que usualmente son vistos
;; para los simbolos (ej; 'x 'var 'sym) un uso es en la creacion de listas;
;; (list a b c) = '(a b c)
;; (quote a) = 'a
;; otra herramienta relacionada, pero con usos mas especifico es ` (AltGr+}+} en teclado latam)
;; un ejemplo de como funciona:
;; (list a 'b c 'd) = `(,a b ,c d)
;; `((+ 1 1) ,(+ 1 1)) = ?
;; otra herramienta relacionada a estas es el procedimiento eval, pero es aun menos aplicable para el trabajo que la anterior


;; EJEMPLOS
;; Simple visualizacion de como generar un intervalo y como quedaria la estructura de uno.
;; No se devuelve un valor (o mas bien dicho se retorna valor de tipo #<void>) en caso de que sea invalido (end < start)
;; otra opcion seria devolver una lista vacia o un error
;; Interval (-> number number Interval) donde Interval simplemente es una lista con 2 numeros
(define (Interval start end)
  (if (< end start)
      (void)
      (list start end)))

;; demostracion de como se accederia a el start y el end de un intervalo
;; gstart (-> Interval bool)
(define (gstart interval) (first interval))
;; gend (-> Interval bool)
(define (gend interval) (second interval))

;; retorna cierto si existe algun rango de valores en los cuales ambos intervalos existen
;; overlap? (-> Interval Interval bool)
(define (overlap? I1 I2)
  (not (or (< (gend I1) (gstart I2)) (< (gei I2) (gsi I1)))))
;; Para comprobar si es que tienen interseccion se demuestra comprobando la condicion contraria,
;; si un intervalo termina antes que el otro empieze, es imposible que halla interseccion

(define I1 (Interval 0 3))
(define I2 (Interval 2 5))
(define I3 (Interval 4 7))
(display `(overlap? ,I1 ,I2))(display " = ")(display (overlap? I1 I2))(newline)
(display `(overlap? ,I2 ,I1))(display " = ")(display (overlap? I2 I1))(newline)
(display `(overlap? ,I1 ,I1))(display " = ")(display (overlap? I1 I1))(newline)
(display `(overlap? ,I1 ,I3))(display " = ")(display (overlap? I1 I3))(newline)
(display `(overlap? ,I3 ,I1))(display " = ")(display (overlap? I3 I1))(newline)

;; Implementacion de procedimiento filtro, que dado un procedimiento booleano y una lista de inputs validos
;; retorna la lista con los elementos para los cuales el procedimiento retorna verdadero
;; si se quisiera el filtro inverso habria que entregar la funcion logicamente inversa
;; ej: procedure -> (lambda (l) (not (procedure l)))
;; filterNTR (-> (-> any bool) list-any list-any)
(define (filterNTR con lis)
  (if (null? lis)
      '()
      (if (con (car lis))
          (cons (car lis) (filter (cdr lis) con))
          (filter (cdr lis) con))))

;; funcion auxiliar con recursion de cola (Tail Recursion) de la funcion filterTR
;; enpezando nuestra lista guerdada vacia solo le agregamos los elementos que correspondan, este metodo nos
;; devuelve una lista alreves, por lo que hace falta darla vuelta
;; filterNTR (-> (-> any bool) list-any list-any)
(define (auxftr con lis sv)
  (if (null? lis)
      sv
      (if (con (car lis))
          (auxftr (cdr lis) con (cons (car lis) sv))
          (auxftr (cdr lis) con sv))))

;; funcion similar a filterNTR pero con aplicacion de recursion de cola
;; filterNTR (-> (-> any bool) list-any list-any)
(define (filterTR con lis) (reverse (auxftr lis con '())))

;; el procedimiento filter viene predeterminado
;; otra forma de implementarla de forma sencilla es:
;; (define (filterF con lis)
;;   (foldr (lambda (x nl) (if (con x)
;;                             (cons x nl)
;;                             nl))
;;                         '()
;;                         lis))
;; el procedimiento foldl suele ser mas eficiente en memoria pero nos entrega por lo que seria mejor:
;; (define (filterF con lis)
;;   (reverse
;;    (foldl (lambda (x nl) (if (con x)
;;                              (cons x nl)
;;                              nl))
;;                          '()
;;                          lis)))
