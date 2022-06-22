#include<iostream>
using namespace std;

int method1(){
	cout << "First method";
    for(int i=0; i<15; i += 1){
        cout << i;
    }

    return i;
}

void method2(){
	cout << "Second method";
	int k = 0;
	while(k < 3){
		cout << "Hi";
		k = k + 1;
	}
}

int main(){
	method1();
	method2();
	cout << "For loop";
    for(int j = 1; j < 5; j += 1){
		cout << j;
        if(j == 3){
            cout << "j is 3";
        } else {
            cout << "j is smaller than 5";
        }
    }

    string waitForInput;
    cin >> waitForInput;
    return 0;
};
