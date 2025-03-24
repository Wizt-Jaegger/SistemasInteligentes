#include <stdio.h>
#include <stdlib.h>
#include <math.h>

float tasaAprendizaje = 0.1;

// Función de activación
int funcionActivacion(int suma) {
    return (suma > 0) ? 1 : 0;
}

// Generar pesos aleatorios
void generarPrimerosPesos(int *px, int *py, int *pz, int *pw, int *pv, int *pu) {
    *px = rand() % 100;
    *py = rand() % 100;
    *pz = rand() % 100;
    *pw = rand() % 100;
    *pv = rand() % 100;
    *pu = rand() % 100;
}

// Entrenamiento del perceptrón
void entrenar() {
    int px, py, pz, pw, pv, pu;
    generarPrimerosPesos(&px, &py, &pz, &pw, &pv, &pu);

    int tablaVerdad[24][7] = {
        {0, 0, 0, 1, 0, 0, 1},
        {0, 0, 1, 0, 0, 0, 1},
        {0, 1, 0, 0, 0, 0, 1},
        {1, 1, 0, 0, 0, 0, 1},
        {1, 0, 1, 0, 0, 0, 0},
        {1, 0, 0, 1, 0, 0, 1},
        {0, 1, 0, 0, 1, 0, 1},
        {0, 0, 1, 0, 1, 0, 1},
        {0, 0, 0, 1, 1, 0, 1},
        {0, 1, 0, 0, 0, 1, 1},
        {0, 0, 1, 0, 0, 1, 1},
        {0, 0, 0, 1, 0, 1, 0},
        {1, 1, 0, 0, 1, 0, 0},
        {1, 0, 1, 0, 1, 0, 1},
        {1, 0, 0, 1, 1, 0, 0},
        {1, 1, 0, 0, 0, 1, 1},
        {1, 0, 1, 0, 0, 1, 1},
        {1, 0, 0, 1, 0, 1, 0},
        {0, 1, 0, 0, 1, 1, 0},
        {0, 0, 1, 0, 1, 1, 1},
        {0, 0, 0, 1, 1, 1, 1},
        {1, 1, 0, 0, 1, 1, 0},
        {1, 0, 1, 0, 1, 1, 0},
        {1, 0, 0, 1, 1, 1, 0}
    };

    int suma, resultado, error, contador = 0, sumErrores = 1;

    while (sumErrores != 0 && contador < 1000) {
        sumErrores = 0;
        for (int i = 0; i < 24; i++) {
            suma = tablaVerdad[i][0] * px + tablaVerdad[i][1] * py + tablaVerdad[i][2] * pz +
                   tablaVerdad[i][3] * pw + tablaVerdad[i][4] * pv + tablaVerdad[i][5] * pu;

            resultado = funcionActivacion(suma);
            error = tablaVerdad[i][6] - resultado;
            sumErrores += abs(error);

            // Ajuste de pesos
            px += tasaAprendizaje * error * tablaVerdad[i][0];
            py += tasaAprendizaje * error * tablaVerdad[i][1];
            pz += tasaAprendizaje * error * tablaVerdad[i][2];
            pw += tasaAprendizaje * error * tablaVerdad[i][3];
            pv += tasaAprendizaje * error * tablaVerdad[i][4];
            pu += tasaAprendizaje * error * tablaVerdad[i][5];
        }

        contador++;
    }

    printf("Entrenamiento finalizado en %d iteraciones. Errores acumulados: %d\n", contador, sumErrores);
    printf("Pesos finales: %d %d %d %d %d %d\n", px, py, pz, pw, pv, pu);

    // Guardar los pesos entrenados en un archivo
    FILE *archivo = fopen("pesos.txt", "w");
    if (archivo != NULL) {
        fprintf(archivo, "%d %d %d %d %d %d\n", px, py, pz, pw, pv, pu);
        fclose(archivo);
    } else {
        printf("Error al guardar los pesos en el archivo.\n");
    }
}
void utilizar() {
    int x, y, z, w, v, u;
    x = y = z = w = v = u = 0;

    int px, py, pz, pw, pv, pu;
    int suma, resultado;
    int ayudante;

    // Leer los pesos desde el archivo
    FILE *archivo = fopen("pesos.txt", "r");
    if (archivo == NULL) {
        printf("No existe el archivo pesos.txt\n");
        exit(0);
    }
    fscanf(archivo, "%d %d %d %d %d %d", &px, &py, &pz, &pw, &pv, &pu);
    fclose(archivo);

    // Obtener datos del usuario
    printf("Escriba el número de años que tiene el celular: ");
    scanf("%d", &ayudante);
    if (ayudante > 10) x = 1;

    ayudante = 0;
    while (ayudante < 1 || ayudante > 3) {
        printf("Seleccione la marca del celular:\n1. Apple\n2. Android\n3. Ninguna de las anteriores\n");
        scanf("%d", &ayudante);
        if (ayudante == 1) y = 1;
        if (ayudante == 2) z = 1;
        if (ayudante == 3) w = 1;
    }

    printf("¿El celular sufrió daños de agua? (1. Sí / 2. No): ");
    scanf("%d", &ayudante);
    v = (ayudante == 1) ? 1 : 0;

    printf("¿Hay que reemplazar piezas? (1. Sí / 2. No): ");
    scanf("%d", &ayudante);
    u = (ayudante == 1) ? 1 : 0;

    // Evaluar resultado con los pesos leídos
    suma = x * px + y * py + z * pz + w * pw + v * pv + u * pu;
    resultado = funcionActivacion(suma);

    if (resultado == 1) {
        printf("El celular es reparable.\n");
    } else {
        printf("El celular no es reparable.\n");
    }
}

void menuVariable(){
    
    int  opt;
    opt = 1;
    while (opt!= 0){
        printf("Este es un perceptron\nSelecciona una opcion:\n\n\t1.Entrenar\n\t2.Utilizar\n\t3.Salir\n");
        scanf("%d",&opt);
        switch(opt){
            case 1:
                entrenar();
                break;
            case 2:
                utilizar();
                break;
            case 3:
                exit(0);
                break;
            default:
                printf("Opcion invalida");
                break;
        }
    }
    

}
int main(){
    
    menuVariable();
}