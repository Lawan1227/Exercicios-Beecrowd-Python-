#include <stdio.h>

int main() {
    char nome[100];
    double salario_fixo, total_vendas, total_receber;

    // Leitura dos dados de entrada
    scanf("%s", nome);
    scanf("%lf", &salario_fixo);
    scanf("%lf", &total_vendas);

    // Cálculo do total: salário fixo + 15% de comissão sobre as vendas
    total_receber = salario_fixo + (total_vendas * 0.15);

    // Impressão do resultado conforme o padrão exigido
    printf("TOTAL = R$ %.2lf\n", total_receber);

    return 0;
}
