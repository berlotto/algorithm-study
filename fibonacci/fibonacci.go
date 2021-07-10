package main

import (
	"fmt"
)

func fibonacci(n int) int {
	if n < 2 {
		return n
	}
	return fibonacci(n-1) + fibonacci(n-2)
}

// this script make a fibonacci sequence
func main() {
	fmt.Println(fibonacci(20))
}
