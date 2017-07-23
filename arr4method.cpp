#include"iostream"

int main()
{
	int arr[] = {10, 20, 30, 40};
	int* ptr = arr;
//	for (int i = 0; i < 4; i++){
//		std::cout << arr[i] << std::endl;
//	}
	
//	for (int i = 0; i < 4; i++){
//		std::cout << *(arr + i) << std::endl;
//	}

//	for (int i = 0; i < 4; i++){
//		std::cout << *(ptr + i) << std::endl;
//	}
	
	for (int i = 0; i < 4; i++){
		std::cout << ptr[i] << std::endl;
	}
}
