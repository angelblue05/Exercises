function repeat(operation, num) {
	repeat(num);
}

module.exports = repeat

// actual solution

function repeat(operation, num) {
	if (num <= 0) return operation()
	return repeat(operation, --num)
}

module.exports = repeat
