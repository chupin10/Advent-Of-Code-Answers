package main

import (
    "fmt"
    "os"
    "bufio"
    "strings"
)

func IsOffByOne(a string, b string) bool {
    num_wrong := 0
    for i := range a {
        a_char := string(a[i])
        b_char := string(b[i])
        if a_char != b_char {
            num_wrong++
        }
        if num_wrong > 1 {
            return false
        }
    }
    if num_wrong == 1 {
        return true
    } else {
        return false
    }
}

func main() {
    filename := "/Users/christopherauld/Desktop/AOC2018/data/day2/input.txt"
    b, err := os.Open(filename)
    if err != nil {
        fmt.Println(err)
    }

    // Part 1
    scanner := bufio.NewScanner(b)
    twos := 0
    threes := 0
    labels := make(map[int]string)
    i := 0

    for scanner.Scan() {
        found_two := false
        found_three := false
        label := scanner.Text()
        labels[i] = label
        i++
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
    fmt.Println(twos * threes)

    // Part 2
    for i = range labels {
        for j := range labels {
            if IsOffByOne(labels[i], labels[j]) {
                fmt.Println(labels[i], labels[j])
            }
        }
    }
}