#include <iostream> 
#include <math.h> 
using namespace std;  

long long int power(long long int a, long long int b,long long int P) 
{  
    if (b == 1) 
        return a;  
    else
        return (((long long int)pow(a, b)) % P); 
} 
  

int main() 
{ 
    long long int P, alpha, x, a, y, b, ka, kb;  
   
    P = 5; 		// A prime number P is taken 
    cout<<"\nThe value of P : "<<P;
    alpha = 3; 		// A primitve root for P, G is taken 
    cout<<"\nThe value of Alpha : "<<alpha;
  
    			// Alice will choose the private key a  
    a = 11; 		// a is the chosen private key  
    cout<<"\nThe private key a for Alice :"<<a;
    x = power(alpha, a, P); // gets the generated key 
      
    			// Bob will choose the private key b 
    b = 13; 		// b is the chosen private key 
    cout<<"\nThe private key b for Bob : "<<b;
    y = power(alpha, b, P); // gets the generated key 
  
    // Generating the secret key after the exchange 
        // of keys 
    ka = power(y, a, P);	 // Secret key for Alice 
    kb = power(x, b, P); 	 // Secret key for Bob 
      
    cout<<"\nSecret key for the Alice is :"<<ka; 
    cout<<"\nSecret Key for the Bob is : "<< kb<<endl; 
      
    if(ka == kb)
       cout<<"\nThe keys Exchanged are Same :) \n"<<endl;  
      
    return 0; 
} 
