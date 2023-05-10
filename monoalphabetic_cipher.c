#include<stdio.h> 
#include<string.h> 
#include<conio.h> 
#include <stdlib.h> 
#include <time.h> 
#include<ctype.h> 
int main() 
{ 
    char alpha[2][26]; 
    char text[50]; 
    int pos[50] , pos_s=0; 
    srand(time(0)); 
    printf("Enter some Text : "); 
    gets(text); 
    for(int i = 0 ; i < 26 ; i++) 
    { 
        alpha[0][i] = 'a' + i; 
        alpha[1][i] = 'A' + i; 
    } 
    //generating random key 
    for(int i = 0 ; i < 26 ; i++) 
    { 
        int rand_no = (rand() %(0 - 25 + 1)) + 0; 
        int temp = alpha[1][i]; 
        alpha[1][i] = alpha[1][rand_no];
        alpha[1][rand_no] = temp; 
    }

    printf("\nFor : "); 
    for(int i = 0 ; i < 26 ; i++) 
    { 
        printf("%c ",alpha[0][i]); 
    } 

    printf("\nKey : "); 
    for(int i = 0 ; i < 26 ; i++) 
    { 
        printf("%c ",alpha[1][i]); 
    } 

    // Encryption 
    for(int i = 0 ; i < strlen(text) ; i++) { 
        if(isupper(text[i])) 
        { 
            pos[pos_s] = i; 
            text[i] = tolower(text[i]); 
            pos_s++; 
        } 
        if(text[i] >= 'a' && text[i] <= 'z') 
        { 
            text[i] = alpha[1][text[i] - 'a']; 
        } 
    } 
    printf("\n\nEncrypted string : %s\n",text); getch(); 
    
    // Decryption 
    for(int i = 0 ; i < strlen(text) ; i++) 
    { 
        if(text[i] >= 'A' && text[i] <= 'Z') 
        { 
            for(int j = 0 ; j < 26 ; j++) 
            { 
                if(text[i] == alpha[1][j]) 
                {
                    text[i] = alpha[0][j]; 
                    break; 
                } 
            } 
        } 
    } 
    for(int i = 0 ; i < pos_s ; i++) 
    { 
        text[pos[i]] = toupper(text[pos[i]]); 
    } 
    printf("\n\nDecrypted string : %s",text); return 0; 
} 
