#lang scheme

;;Funcion de addicion de lista como sum(lista) que implementa recursion de cola
;;TRadd: (-> number-list? number?)
(define (TRadd L)
  (define (iter L S)
    (if (empty? L)
        S
        (iter (rest L) (+ S (first L)))))
  (iter L 0))

;;Funcion que muestra por pasos la estructura del proceso para TRadd
;;este comportamiento ocurre en lenguajes que soportan Tail Recursion
;;Observacion: es una funcion hecha para efectos demostrativos
;;symTRadd: (-> number-list? number?)
(define (symTRadd L)
  (define (iter L S)
    (display (list 'iter L S)) (newline)
    (if (empty? L)
        S
        (iter (rest L) (+ S (first L)))))
  (iter L 0))

;;Una implementacion no optimizada, ya que para n elementos el uso de memoria
;;es del orden n^2 (~= sumatoria_i=0_a_n(a*i)) debido a tener la lista en memoria
;;para cada llamada recursiva e incluyendo la llamada original
;;NTRadd: (-> number-list? number?)
(define (NTRadd L)
  (if (empty? L)
      0
      (+ (first L) (NTRadd (rest L)))))

;;Funcion que muestra por pasos la estructura del proceso para NTRadd
;;Observacion: es una funcion hecha para efectos demostrativos
;;symTRadd: (-> number-list? number?)
(define (symNTRadd L)
  (define (sntaa L)
    (if (empty? L)
        (list 0)
        (list '+ (first L) (list 'NTRadd (rest L)))))
  (define (sntaaa L)
    (if (empty? L)
        (sntaa L)
        (cons (sntaa L) (sntaaa (rest L)))))
  (define (sntaaaa L)
    (if (empty? (rest (rest L)))
        (list (list '+ (second (first L)) (eval (second L))))
        (cons (first L) (sntaaaa (rest L)))))
  (define (sntaaaaa L)
    (if (empty? (rest L))
        (eval (first L))
        (let ((aaaaa (sntaaaa L)))
          (display aaaaa)
          (newline)
          (sntaaaaa aaaaa))))
  (let ((reclis (sntaaa L)))
    (display (sntaaa L))
    (newline)
    (sntaaaaa reclis)))

;;funcion que muestra una aproximacion de la estructura de memoria
;;para la solucion con y sin recursion de cola para la suma para una
;;lista de numeros dados
;;test-em: (-> number-list? symbol?)
(define (test-em L)
  (display "primero la solucion sin recursion de cola")
  (newline)
  (symNTRadd L)
  (newline)
  (display "ahora la solucion con recursion de cola")
  (newline)
  (symTRadd L)
  'done)
(define L '(1 2 3 4 5))

;;implementacion con rest (. L) para que quede como la suma por lo que
;;se puede referir como una reimplementacion circular del procedimiento +
;;(c-add a b c) con a b c siendo cero o mas numeros, tendra el mismo comportamiento
;;que (+ a b c), esto se debe a que + viene predefinido con un comportamiento de fold
;;esto ocurre con multiples procedimientos, por ejemplo cual sera el valor inicial de and?
;;TRadd: (-> . number? number?)
(define (c-add . L) (foldl + 0 L))