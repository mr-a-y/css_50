#include <cs50.h>
#include <stdio.h>

int credit_checker(long n,int a);
int card_veri(long n, int cnt);

int main(void)
{

    long card = get_long("Number : ");
    int ln = credit_checker(  card, 0);   // checks the lenght of the credit cart
    int chk = credit_checker( card, 1);  //  checks the first degit unless its 5 or 3 then first 2 digits
    printf("what veri after running the function %i \n ",chk);
    int veri = card_veri( card, ln);    //   checks whats the last degit when ran through the algo
    printf("what is veri for algo = %i\n",veri);

    if ( veri == 0 )
    {
        if ( ln == 15 )
        {
            if ( chk == 34 || chk == 37 )
            {
                printf("AMEX\n");
            }
            else
            {
                printf("INVALID\n");
            }
        }
        else if ( ln == 16 || ln == 13 )
        {
            if ( 50 < chk && chk < 56 )
            {
                printf("MASTERCARD\n");
            }
            else if ( chk == 4)
            {
                printf("VISA\n");
            }
            else
            {
                printf("INVALID\n");
            }
        }
        else
        {
            printf("INVALID\n");
        }

    }
    else
    {
        printf("INVALID\n");
    }
}

int credit_checker(long n, int a)
{
    int cnt = 0;
    long chk = 10;
    long veri;

    do
    {
        cnt++;
        veri = n-(n % chk);
        chk *= 10;
    }
    while (veri !=0);

    if(a == 0 )
    {
      return cnt;
    }
    else
    {
        chk /= 100;
        veri = ( n - ( n % chk ) ) / chk ;

        printf("veri is %li  before the if \n",veri);

        if ( veri == 5 || veri == 3)
        {
            chk /= 10;
            veri = ( n - ( n % chk ) ) / chk ;
        printf("veri is %li  in the  if \n",veri);

            return veri;
        }
        else {
            return veri;
        }

    }

}

int card_veri(long n, int cnt)
{
    int ans = 0;

    for ( int i = 0; i < cnt; i++ )
    {
        int veri = n % 10;

        if ( i % 2 == 1)
        {
            veri *= 2;

            if ( veri > 9)
            {

                ans = ans + veri - 9 ;
            }
            else
            {

                ans = ans + veri ;
            }
        }
        else
        {
            ans += veri;
        }

        n /= 10;

    }

    ans %= 10;

    return ans;
}





