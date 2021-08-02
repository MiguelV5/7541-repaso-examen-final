
///////////////////////////////////////////////////////////////////////////////////
Del 2020 - 1C - 3er Final:

//==============================================================================//

[1] Version 1:

    {1}
    El hardware en el que se ejecuta un algoritmo es uno de los factores que puede afectar en la eficiencia de su ejecución, con lo cuál lo que se hace es tomar un modelo matemático que permita hacer el análisis asintótico del comportamiento de un algoritmo sin tener en cuenta el entorno en
    el que se ejecuta, es decir, se abstraen esos factores para llegar a una estimación de lo que sucede en el peor de los casos para determinada implementación usando la notación big O.
    Para llegar a dicha estimación se sigue con una serie de reglas que hacen parte de dicho análisis:
    Reglas:
        Para iteraciones:
            El tiempo de ejecución de las mismas es a lo sumo:
            (cantidad de iteraciones)*(tiempo de ejecución de las intrucciones que contenga la iteración)

        Iter anidadas:
            ... a lo sumo: 
            [Tiempo para iteraciones de dentro hacia afuera multiplicadas entre si]

        Instrucciones consecutivas:
            ... : 
            max(instruccion1 , instruccion2, ... , instruccion n-1 , instruccion n)
        
        Condicionales:
            ... :
            [if(CONDICION){ACCIONES 1} else{ACCIONES 2}]
            (tiempo de ejec. de la CONDICION) + max(ACCIONES 1 , ACCIONES 2)

    Para funciones recursivas que ADEMÁS tengan permanentemente la misma cantidad de llamados recursivos (a) y dividan el problema en partes iguales cada vez (b) se puede usar el teorema maestro:
        T(n) = a*T(n/b) + f(n)


    {2}
    Los tres pueden ser comparados si se los analiza por medio del teorema maestro.
    T(n) = 4*T(n/4) + n²
        log_b(a) = log_4(4) = 1
        n^log_4(4) = n
        f(n) = n²
        f(n) mayor polinomicamente 
        => O(n²)

    G(n) = 16*T(n/4) + n
        log_b(a) = log_4(16) = 2
        n^log_4(16) = n²
        f(n) = n
        f(n) menor polinomicamente 
        => O(n²)

    F(n) = 3*T(n/2) + n²
        log_b(a) = log_2(3) =~ 1.585
        n^log_2(3) =~ n^1.585
        f(n) = n²
        f(n) mayor polinomicamente 
        => O(n²)

    => Todos los algoritmos tienen el la misma complejidad O(n²)

//==============================================================================//

[2] Version 2:

typedef struct lista{
    struct lista* siguiente
    struct lista* anterior
    void* elemento
}lista_t;

//Asumo que el nodo ANTERIOR al 1er nodo de la lista es NULL y que el nodo SIGUIENTE al ultimo nodo de la lista es NULL.
//Tambien asumo que en el 1er llamado a la función se recibe el 1er nodo de la lista.
lista_t* lista_eliminar(lista_t* lista, void* elemento, int (*comparador)(void*, void*)){

    if(!lista){
        return NULL;
    }
    
    int resultado_comparacion = comparador(lista->elemento, elemento);
    if(resultado_comparacion == 0){
        lista_t* nodo_a_eliminar = lista;
        lista_t* siguiente_a_reacomodar = lista->siguiente; //No importa que sea NULL
        if(lista->anterior && lista->siguiente){ //SE ELIMINA POSICION INTERMEDIA DE LA LISTA (MÁS DE DOS ELEMENTOS)
            lista->siguiente->anterior = lista->anterior;
        }
        else if(!lista->anterior && lista->siguiente){ //SE ELIMINA PRIMERA POS. DE LISTA (CON MÁS DE UN ELEMENTO)
            lista->siguiente->anterior = NULL;
        }
        //Si la lista tenía un solo elemento se elimina a sí mismo y no necesita reasignar punteros. En tal caso el "siguiente_a_reacomodar" es NULL.
        //A su vez, si se elimina la última pos. de la lista (con más de un elemento), se libera a si mismo y devuelve NULL como siguiente a reacomodar.
        
        free(nodo_a_eliminar);
        return siguiente_a_reacomodar;
    }

    lista->siguiente = lista_eliminar(lista->siguiente);

    return lista;

}