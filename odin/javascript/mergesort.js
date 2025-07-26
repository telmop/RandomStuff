function mergeSort(array) {
    if (array.length <= 1) {
        return array;
    }
    let mid = Math.floor(array.length / 2);
    let first = mergeSort(array.slice(0, mid));
    let second = mergeSort(array.slice(mid, array.length));

    let new_array = [];
    let i = 0, j = 0;
    for (let k = 0; k < array.length; k++) {
        if (i < first.length) {
            if (j < second.length) {
                if (first[i] < second[j]) {
                    new_array.push(first[i]);
                    i++;
                } else {
                    new_array.push(second[j]);
                    j++;
                }
            } else {  // Second is empty.
                new_array.push(first[i]);
                i++;
            }
        } else {  // First is empty.
            new_array.push(second[j]);
            j++;
        }
    }
    return new_array;
}
