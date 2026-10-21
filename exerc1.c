#include <stdio.h>
int main()
{

    int a = 0;
    float saldo = 1000;
    float depo, saque;
    while (a != 4)
    {
        printf("=========CAIXA ELETRONICO=========\n");
        printf("1 - Consultar saldo\n2 - Depositar dinheiro\n3 - Sacar dinheiro\n4 - Sair\nEscolha uma opcao:\n");
        scanf("%i", &a);
        switch (a)
        {
        case 1:
            printf("Saldo atual é R$ %.2f\n\n", saldo);
            break;
        case 2:
            printf("Quanto voce gostaria de depositar ?\n\n");
            scanf("%f", &depo);
            if (depo > 0)
            {
                saldo = saldo + depo;
            }
            else
                printf("Deposito nao pode ser concluido, por favor escolhe um saldo positivo\n\n");
            break;
        case 3:
            printf("Quanto voce gostaria de sacar ?\n\n");
            scanf("%f", &saque);
            if (saldo < saque)
            {
                printf("Saque nao pode ser concluido pois falta saldo\n\n");
            }
            else if (saque < 0)
            {
                printf("Saque nao pode ser concluido pois é negativo\n\n ");
            }
            else if (saldo >= saque)
            {
                saldo = saldo - saque;
                printf("Saque concluido com sucesso\n\n");
            }
            break;
        case 4:
            printf("Voce saiu do programa\n\n");
            break;
        default:
            printf("Voce digitou uma opcao invalida !! Escolha outra\n\n");
        }
    }
}
