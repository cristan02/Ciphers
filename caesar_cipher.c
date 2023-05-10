#include<stdio.h>
#include<string.h>
#include<conio.h>
int main()
{
   char s[100];
   int key;


   printf("Enter some Text : ");
   gets(s);


   printf("Enter key value : ");
   scanf("%d",&key);


   for(int i = 0 ; i < strlen(s) ; i++)
   {
       if(s[i] >= 'a' && s[i] <= 'z')
           s[i] = (s[i] - 'a' + key) % 26 + 'a';
       else if(s[i] >= 'A' && s[i] <= 'Z')
           s[i] = (s[i] - 'A' + key) % 26 + 'A';
       else if(s[i] >= '0' && s[i] <= '9')
           s[i] = (s[i] - '0' + key) % 10 + '0';
   }


   printf("\n\nEncrypted string : %s\n",s);
   getch();


   for(int i = 0 ; i < strlen(s) ; i++)
   {
       if(s[i] >= 'a' && s[i] <= 'z')
           s[i] = (s[i] - 'a' - key + 26) % 26 + 'a';
       else if(s[i] >= 'A' && s[i] <= 'Z')
           s[i] = (s[i] - 'A' - key + 26) % 26 + 'A';
       else if(s[i] >= '0' && s[i] <= '9')
           s[i] = (s[i] - '0' - key + 10) % 10 + '0';
   }


   printf("\n\nDecrypted string : %s",s);
}