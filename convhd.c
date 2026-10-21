#include <stdio.h>
int main(){
int valor , opcao;	
printf("Convertor de Unidades\n");
printf("Escolha uma opcao:\n");
printf("1 - De decimal para hexadecimal\n2- De hexadecimal para decimal\n");
scanf("%i" , &opcao);
getchar();

if (opcao == 1)
{
    printf("\nDigite o Número que queira ser convertido: \n");
    scanf("%d" , &valor);
    printf("%d em hexadecimal eh: %x" , valor , valor );
}
else if(opcao == 2)
{
     printf("\nDigite o Letra que queira ser convertido: \n");
    scanf("%x" , &valor);
    printf("%x em decimal eh: %d" , valor , valor);
}
else printf("ERRO !\nSelecione uma opcao valida");

	
	
}
