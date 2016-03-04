#include<iostream>
#include<cstdlib>
#include<string>
#include<ctime>
#include<math.h>


using namespace std;

double* createMatrix(int filas, int columnas);
double* sumMatrix(int filas, int columnas, double* matriz1, double* matriz2);
double* prodMatrix(int filas1, int columnas1, int filas2, int columnas2, double* matriz1, double* matriz2);
string matrixToString(int filas, int columnas, double* matriz);
void printMatrix(string cadena, int filas, int columnas, double* matriz);

int main()
{
	int filas, columnas;
	double *matriz1, *matriz2, *suma, *producto;
	filas = 3;
	columnas = 3;
	srand((unsigned int)time(NULL));
	matriz1 = createMatrix(filas, columnas);
	matriz2 = createMatrix(filas, columnas);
	suma = sumMatrix(filas, columnas, matriz1, matriz2);
	producto = prodMatrix(filas, columnas, filas, columnas, matriz1, matriz2);
	printMatrix("Matrix A", filas, columnas, matriz1);
	printMatrix("Matrix B", filas, columnas, matriz2);
	printMatrix("Matrix C = A+B", filas, columnas, suma);
	printMatrix("Matrix D = A*B", filas, columnas, producto);


	return 0;
}

double* createMatrix(int filas, int columnas)
{
	double* nuevamatriz = new double[filas*columnas];
	for (int i = 0; i < (filas*columnas); i++)
	{
		nuevamatriz[i] = fmod(rand(), 10.);
	}
	return nuevamatriz;
}

double* sumMatrix(int filas, int columnas, double* matriz1, double* matriz2)
{
	double *resultado = new double[filas*columnas];
	for (int i = 0; i < (filas*columnas); i++)
	{
			resultado[i] = matriz1[i] + matriz2[i];
	}
	return resultado;
}

double* prodMatrix(int filas1, int columnas1, int filas2, int columnas2, double* matriz1, double* matriz2)
{
	double *resultado = createMatrix(filas1, columnas2);
	for (int i = 0; i < filas1; i++)
	{
		for (int k = 0; k < columnas2; k++)
		{
			double sum = 0.;
			for (int j = 0; j < columnas1; j++)
			{
			// resultado[(i*columnas2)+k]+=matriz1[i*columnas1+j]+matriz2[j*columnas2+k];
				sum += (matriz1[(i*columnas1) + j]) * (matriz2[(j*columnas2) + k]);
			}
			resultado[i*columnas2 + k]=sum;
		}
	}
	return resultado;
}
string matrixToString(int filas, int columnas, double* matriz)
{
	string str = "";
	for (int i = 0; i < filas*columnas; i++)
	{
		str = str + to_string(matriz[i])+" ";
		if ((i + 1) % columnas == 0)
		{
			str = str + "\n";
		}
	}
	return str;
}
void printMatrix(string title, int filas, int columnas, double* matriz)
{
	cout << title << endl << matrixToString(filas, columnas, matriz) << endl;
}








