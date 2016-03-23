#include <iostream>
#include <math.h>
#define PI 3.14159265

int main ()
{
    int weight = 50;
    int angle_1 = 30 ;
    int angle_2 = 30 ;
    int steel_kind;

    std::cout << "Hello Engineer! \n";
    std::cout << "Please specify the weight of the tube in Newtons\n";
    std::cin >> weight; 

    std::cout << "Please specify the angle of tensor 1 \n";
    std::cin >> angle_1;

    std::cout << "Please specify the angle of tensor 2 \n";
    std::cin >> angle_2;


    //validate angle
    if (angle_1 > 90 or angle_2 > 90 ) {
        std::cout << "Wrong angle , must me < 90 ";
        return -1;
    }


    std::cout << "Please specify the material of the tensioners \n";
    std::cout << "1 ) steel \n";
    std::cout << "2 ) steel 2 \n";
    std::cout << "3 ) steel 3 \n";
    std::cin >> steel_kind;

    //create ecuations
    double matrix[2][3];

    // sum F in x
    matrix[0][0] =  sin(angle_1*PI/180);
    matrix[0][1] =  sin(angle_2*PI/180);
    matrix[0][2] =  weight * -1;

    // sum F in y
    matrix[1][0] = cos(angle_1*PI/180);
    matrix[1][1] = cos(angle_2*PI/180);
    matrix[1][2] = 0;

    //print matrix
    for (int i = 0 ; i < 2 ; i ++){
        for ( int j = 0 ; j < 3 ; j++){
            std::cout << matrix[i][j] << " "; 
        }
        std::cout << std::endl;
    }
    return 0;
}
