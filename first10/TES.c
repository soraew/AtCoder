#include <stdio.h>
#include <stdbool.h>
#include <string.h>

// char *rev(char *arr){
//    int l=strlen(arr), i;
//    // printf("l :>> %d\n", l);
//    for (i=0;i<l/2;i++){
//       char temp;
//       // printf("how\n");
//       temp = arr[l-i-1];
//       arr[l-i-1] = arr[i];
//       arr[i] = temp;
//    }
//    return arr;
// }


void rev(char *s){
   int l=strlen(s),i;
   for(i=0;i<l/2;i++){
      char t=s[i];
      s[i]=s[l-1-i];
      s[l-1-i]=t;
   }
}

char T[4][8] = {"dream", "erase", "dreamer", "eraser"};

int main (int argc, char *argv[]) {
   char S[201]="dreameraser";

   // printf("%d\n", S[0]==' ');
   // printf("%c\n", S[188]);

   // if (S[0] == ' '){
   //    printf("to\n");
   // }else{
   //    printf("do\n");
   // }
   // printf("S[-3] :>> %c\n", S[-3]);
   rev(S);
   for (i=0; i<4; i++)rev(T[i]);

   if (S[:5])

   printf("%s", S);
   return 0;

   
}