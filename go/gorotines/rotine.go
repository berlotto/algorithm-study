package main

import (
	"fmt"
	"runtime"
	"sync"
	"time"
)

var wg sync.WaitGroup

func rotine(id string, max int) {
	for x := 0; x <= max; x += 1 {
		fmt.Println("Rotine", id, x)
		time.Sleep(20)
	}
	wg.Done()
}

func main() {
	fmt.Println(runtime.NumCPU(), "CPUs")
	fmt.Println(runtime.NumGoroutine(), "goroutines")
	wg.Add(5)

	go rotine("A", 20)
	go rotine("B", 40)
	go rotine("C", 10)
	go rotine("D", 5)
	go rotine("E", 17)

	wg.Wait()
	fmt.Println(runtime.NumGoroutine(), "goroutines")
}
