#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <conio.h>

int main()
{
    char key[5][5];
    char txt[] = "hello world";
    char tempkey[25];
    char temp[] = "command";
    char disable = 'j';
    int k = 0;

    if (strstr(txt, "j") && strstr(txt, "i") == 0)
        disable = 'i';
    else if (strstr(txt, "j") && strstr(txt, "i"))
    {
        printf("Plain text contains both i and j\n");
        return 0;
    }
    // converting plaintext to lower case
    for (int i = 0; i < strlen(txt); i++)
        txt[i] = tolower(txt[i]);

    // converting key to lower case
    for (int i = 0; i < strlen(temp); i++)
        temp[i] = tolower(temp[i]);

    // removing spaces from key
    for (int i = 0; i < strlen(txt); i++)
    {
        if (txt[i] == ' ')
        {
            for (int j = i; j < strlen(txt); j++)
            {
                txt[j] = txt[j + 1];
            }

            txt[strlen(txt)] = ' ';
        }
    }

    // pairing plain text test
    for (int i = 0; i < strlen(txt); i += 2)
    {
        if (txt[i] == txt[i + 1])
        {
            for (int j = strlen(txt); j > i; j--)
            {
                txt[j] = txt[j - 1];
            }
            txt[i + 1] = 'x';
        }
    }
    for (int i = 0, cnt = 0; i < strlen(txt) + 1; i++)
    {
        if (i < strlen(txt))
        {
            if (isalpha(txt[i]))
                cnt++;
        }
        else
        {

            if (cnt % 2 != 0)
                txt[cnt] = 'z';
        }
    }

    // generating key in a string
    for (int i = 0; i < strlen(temp); i++)
    {
        int flag = 0;
        for (int j = 0; j < strlen(tempkey); j++)
        {
            if (temp[i] == tempkey[j])
            {
                flag = 1;
                break;
            }
        }
        if (flag == 0)
        {
            tempkey[k] = temp[i];
            k++;
        }
    }
    for (char i = 'a'; i <= 'z'; i++)
    {

        int flag = 0;
        if (i == disable)
            continue;
        for (int j = 0; j < strlen(tempkey); j++)
        {
            if (i == tempkey[j])
            {
                flag = 1;
                break;
            }
        }
        if (flag == 0)
        {
            tempkey[k] = i;
            k++;
        }
    }

    // putting generated string key in 5X5 matrix
    for (int i = 0, k = 0; i < 5; i++)
    {
        for (int j = 0; j < 5; j++)
        {
            key[i][j] = tempkey[k];
            k++;
        }
    }

    // displaying key
    printf("\nKey : \n");
    for (int i = 0, k = 0; i < 5; i++)
    {
        for (int j = 0; j < 5; j++)
        {
            printf(" %c ", key[i][j]);
        }
        printf("\n");
    }

    printf("\nPlain text : ");
    for (int i = 0; i < strlen(txt); i += 2)
        printf("%c%c ", txt[i], txt[i + 1]);

    // encryption
    for (int i = 0; i < strlen(txt); i += 2)
    {
        int a, b, c, d;
        for (int j = 0; j < 5; j++)
        {
            for (int k = 0; k < 5; k++)

            {
                if (txt[i] == key[j][k])
                {
                    a = j;
                    b = k;
                    break;
                }
            }
        }
        for (int j = 0; j < 5; j++)
        {
            for (int k = 0; k < 5; k++)
            {
                if (txt[i + 1] == key[j][k])
                {
                    c = j;
                    d = k;
                    break;
                }
            }
        }

        if (a == c)
        {
            txt[i] = key[a][(b + 1) % 5];

            txt[i + 1] = key[c][(d + 1) % 5];
        }
        else if (b == d)
        {
            txt[i] = key[(a + 1) % 5][b];
            txt[i + 1] = key[(c + 1) % 5][d];
        }
        else
        {
            txt[i] = key[a][d];
            txt[i + 1] = key[c][b];
        }
    }

    printf("\nEncrypted text : ");
    for (int i = 0; i < strlen(txt); i += 2)
        printf("%c%c ", txt[i], txt[i + 1]);
}