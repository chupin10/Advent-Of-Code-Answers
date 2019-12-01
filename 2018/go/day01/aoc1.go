package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	filename := "/Users/christopherauld/Desktop/AOC2018/data/day1/aoc1.txt"
	b, err := os.Open(filename)
	if err != nil {
		fmt.Println(err)
	}

	delta_freqs := []int{}
	scanner := bufio.NewScanner(b)
	final_freq := 0

	for scanner.Scan() {
		val, err := strconv.Atoi(scanner.Text())
		if err != nil {
			fmt.Println(err)
		}
		final_freq += val
		delta_freqs = append(delta_freqs, val)
	}

	// Part 1
	fmt.Println(final_freq)

	// Part 2
	all_freqs := make(map[int]bool)
	new_freq := 0
	i := 0
	found := false

	for !found {
		if i == len(delta_freqs) {
			i = 0
		}
		new_freq = new_freq + delta_freqs[i]
		_, found = all_freqs[new_freq]
		all_freqs[new_freq] = true
		i++
	}
	fmt.Println(new_freq)
}
