const arr = [1, 2, 3, 4, 5, 6, 7, 8, 9];

//Linear search
function lSearch(arr, needed){
	for (let i in arr){
		if(arr[i] == needed) return i
	}
	return null;
}

//Binary search using loop

function blSearch(arr, needed){
	let start = 0;
	let end = arr.length;
	let isFound = false;
	let sep;

	while(!isFound && end > start){
		sep = Math.floor((end + start)/2);
		if(arr[sep] == needed){
			isFound = true;
			return arr[sep];
		}
		if(needed > arr[sep]){
			start = sep + 1;
		} else {
			end = sep -1;
		}
	}
	return null;
}

//Binary search using recursion
var count = 0;
function brSearch(arr, needed, start, end){
	count ++ 
	if(!start) start = 0;
	if(!end) end = arr.length;
	if(start > end) return null;
	let middle = Math.floor((start + end)/2);
	if(needed == arr[middle]) return middle;

	if(needed < arr[middle]) return brSearch(arr, needed, 0, middle - 1);
	else return brSearch(arr, needed, middle + 1, arr.length);
}
