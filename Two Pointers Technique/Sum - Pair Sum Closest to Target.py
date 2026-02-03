function sumClosest(arr, target) {
    let n = arr.length;

    let res = [];
    let minDiff = Number.MAX_SAFE_INTEGER;

    // Generating all possible pairs
    for (let i = 0; i < n - 1; i++) {
        for (let j = i + 1; j < n; j++) {

            let currSum = arr[i] + arr[j];
            let currDiff = Math.abs(currSum - target);

            // if currDiff is less than minDiff, it indicates
            // that this pair is closer to the target
            if (currDiff < minDiff) {
                minDiff = currDiff;
                res = [Math.min(arr[i], arr[j]), Math.max(arr[i], arr[j])];
            }

            // if currDiff is equal to minDiff, find the one with
            // largest absolute difference
            else if (currDiff === minDiff && 
                     (res[1] - res[0]) < Math.abs(arr[i] - arr[j])) {
                res = [Math.min(arr[i], arr[j]), Math.max(arr[i], arr[j])];
            }
        }
    }
    return res;
}

// Driver Code
let arr = [5, 2, 7, 1, 4];
let target = 10;

let res = sumClosest(arr, target);
if(res.length > 0)
	console.log(res[0] + " " + res[1]);