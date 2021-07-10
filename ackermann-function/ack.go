package main

import "fmt"

func ack(m int,n int) int {
    if m == 0 {
        return n + 1
    }else if m > 0 && n == 0 {
        return ack(m-1, 1)
    }else if m > 0 && n > 0 {
        return ack(m-1, ack(m, n-1))
    }
    return 0
}

func main() {
    for m:=0; m<=5; m++ {
        for n:=0; n<=5; n++ {
            fmt.Println("ack(",m,",",n,")=", ack(m,n))
        }
    }
}
