//Swap two numbers
function swap(a, b){
	a = a + b;
	b = a - b;
	a = a - b;
}

//Swap two elements of an array
function swapArr(arr, i, j){
	let temp = arr[i];
	arr[i] = arr[j];
	arr[j] = temp;
}

//Generate random array
function generateArray(len) {
	let arr = [];
	for (let i = 0; i < len; i++){
		arr.push(Math.floor(Math.random() * 100))
	}
	return arr;
}

//Select sort
function selectSort(arr){
	for(let i = 0; i < arr.length; i ++){
		for(let j = i + 1; j < arr.length; j++){
			if(arr[j] < arr[i]) {
				swapArr(arr, i, j);
			} 
		}
	}
	return arr;
}

//Booble sort
function boobleSort(arr){
	for(let i = 0; i < arr.length; i++){
		for(let j = 0; j < arr.length - i; j++){
			if(arr[j + 1] < arr[j]) swapArr(arr, j + 1, j);
		}
	}
	return arr;
}

//Quick sort
function quickSort(arr){
	if(arr.length <= 1) return arr;
	let pivotInx = Math.floor(arr.length / 2);
	let pivot = arr[pivotInx];
	let left = [];
	let right = [];

	for (let i = 0; i < arr.length; i ++){
		if(i == pivotInx) continue;

		if(arr[i] < pivot) left.push(arr[i]);
		else right.push(arr[i]);
	}

	return [].concat(quickSort(left), [pivot], quickSort(right));
}
