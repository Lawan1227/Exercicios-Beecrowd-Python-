#include <stdio.h>
int main(){
    char nome[15];
    float n1 , n2;
    printf("Digite o nome do aluno: ");
    fgets(nome , 15 , stdin);
    printf("Digite a primeira nota: ");
    scanf("%g" , &n1 );
    printf("Digite a segunda nota: ");
    scanf("%g" , &n2 );
    float media = (n1 + n2) / 2;
    printf("\nAluno: %s" , nome);
    printf("\nMedia final: %g" , media);
}
