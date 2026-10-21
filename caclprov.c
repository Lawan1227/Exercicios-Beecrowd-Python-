#include <stdio.h>
int main()
{
    char nome[20];
    int nn, i, notaas_altas = 0;
    float nota, soma = 0;
    float maior = -1;
    float menor = 11;
    printf("===== RELATORIO DO ALUNO =====\n\n");
    printf("Digite o nome do aluno: ");
    fgets(nome, 20, stdin);
    printf("Quantas notas voce ira usar:  ");
    scanf("%i", &nn);
    for (i = 1; i <= nn; i++)
    {
        printf("Diga o valor da nota:");
        scanf("%g", &nota);
        soma = soma + nota;
        if (nota >= 7)
        {
            notaas_altas = notaas_altas + 1;
        }
        if (nota > maior)
        {
            maior = nota;
        }
        if (nota < menor)
        {
            menor = nota;
        }
    }
    float media = soma / nn;
    printf("\nALuno: %s" , nome);
    printf("Quantidade de notas: %i\n" , nn);
    printf("Media final: %.2g\n" , media);
    printf("Maior nota: %g\n" , maior); 
    printf("Menor nota: %g\n" , menor); 
    printf("Notas 7>= : %i\n" , notaas_altas); 
    if (media >= 7){
        printf("Situacao: Aprovado");
    }
    else printf("Situacao: Reprovado");

}
