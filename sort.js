const swap = (list, n1, n2) => {
	[list[n1], list[n2]] = [list[n2], list[n1]];
};

const bubbleSort = (list) => {
	for (let i = 0; i < list.length; i++) {
		for (let l = 0; l < list.length - i - 1; l++) {
			if (list[l] > list[l + 1])
				swap(list, l, l + 1);
		}
	}
	return list;
};

const selectionSort = (list) => {
	for (let i = 0; i < list.length; i++) {
		let min_idx = i;
		for (let l = i; l < list.length; l++) {
			if (list[l] < list[min_idx])
				min_idx = l;
		}
		swap(list, i, min_idx);
	}
	return list;
};

const quickSort = (list) => {
	const rec = (list) => {
		if (list.length > 1) {
			let pivot = list[0];
			let left = [];
			let right = [];
			for (let i = 1; i < list.length; i++) {
				if (list[i] < pivot)
					left.push(list[i]);
				else
					right.push(list[i]);
			}
			return rec(left).concat(pivot, rec(right));
		}
		return list;
	};
	list = rec(list);
	return list;
};

const insertionSort = (list) => {
	for (let i = 1; i < list.length; i++) {
		let key = list[i];
		let j = i-1;
		for (j; j >= 0 && list[j] > key; j--) {
			list[j+1] = list[j];
		}
		list[j+1] = key;
	}
	return list;
};

const mergeSort = (list) => {

};


const generateList = (size) => {
	let list = Array.from({length: size}, () => Math.floor(Math.random() * 40));
	return list;
};