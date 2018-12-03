package main

import (
    "fmt"
    "os"
    "bufio"
    "strings"
)


func intInSlice(a int, list []int) bool {
    for _, b := range list {
        if b == a {
            return true
        }
    }
    return false
}


func main() {
    filename := "/Users/christopherauld/Desktop/AOC2018/data/day2/input.txt"
    b, err := os.Open(filename)
    if err != nil {
        fmt.Println(err)
    }

    scanner := bufio.NewScanner(b)
    twos := 0
    threes := 0

    for scanner.Scan() {
        found_two := false
        found_three := false
        label := scanner.Text()
        for idx := range label{
            if strings.Count(label, string(label[idx])) == 2  && !found_two {
                twos++
                found_two = true
            } 
            if strings.Count(label, string(label[idx])) == 3  && !found_three {
                threes++ 
                found_three = true
            }
        }
    }

    // Part 1
    fmt.Println(twos * threes)
}