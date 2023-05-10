#include<stdio.h>
#include<string.h>
#include<conio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
    char text[100];
    char key[100];
    srand(time(0));

    printf("Enter some Text : ");
    gets(text);

    //to generate the key
    for(int i = 0 ; i < strlen(text) ; i++)
    {
        if(text[i] == ' ')
            key[i] = ' ';
        else if(text[i] >= 'a' && text[i] <= 'z')
            key[i] = (rand() %('z' - 'a' + 1)) + 'a';
        else if(text[i] >= 'A' && text[i] <= 'Z')
            key[i] = (rand() %('Z' - 'A' + 1)) + 'A';
        else if(text[i] >= '0' && text[i] <= '9')
            key[i] = (rand() %('9' - '0' + 1)) + '0';
    }

    printf("\nKey : %s",key);

    //Encryption

    for(int i = 0 ; i < strlen(text) ; i++)
    {
        if(text[i] >= 'a' && text[i] <= 'z')
            text[i] = (text[i] - 'a' + key[i] - 'a') % 26 + 'a';
        else if(text[i] >= 'A' && text[i] <= 'Z')
            text[i] = (text[i] - 'A' + key[i] - 'A') % 26 + 'A';
        else if(text[i] >= '0' && text[i] <= '9')
            text[i] = (text[i] -'0' + key[i] -'0') % 10 + '0';
    }

    printf("\n\nEncrypted string : %s\n",text);
    getch();

    //Decryption
    for(int i = 0 ; i < strlen(text) ; i++)
    {
        if(text[i] >= 'a' && text[i] <= 'z')
            text[i] = ((text[i] - 'a') - (key[i] - 'a') + 26 ) % 26 + 'a';
        else if(text[i] >= 'A' && text[i] <= 'Z')
            text[i] = ((text[i] - 'A') - (key[i] - 'A') + 26 ) % 26 + 'A';
        else if(text[i] >= '0' && text[i] <= '9')
            text[i] = ((text[i] - '0') - (key[i] - '0') + 10 ) % 10 + '0';
    }

    printf("\n\nDecrypted string : %s",text);
}