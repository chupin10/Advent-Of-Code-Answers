package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Claim struct {
	left   int
	top    int
	width  int
	height int
}

func main() {
	filename := "/Users/christopherauld/Desktop/AOC2018/data/day3/input.txt"
	b, err := os.Open(filename)
	if err != nil {
		fmt.Println(err)
	}

	// Part 1
	scanner := bufio.NewScanner(b)
	claims := make(map[int]Claim)
	claim_num := 0

	for scanner.Scan() {
		line := strings.Split(scanner.Text(), " ")
		claim_num, err = strconv.Atoi(strings.Replace(line[0], "#", "", -1))
		if err != nil {
			fmt.Println(err)
		}
		left, _ := strconv.Atoi(strings.Split(line[2], ",")[0])
		top, _ := strconv.Atoi(strings.Replace(strings.Split(line[2], ",")[1], ":", "", -1))
		width, _ := strconv.Atoi(strings.Split(line[3], "x")[0])
		height, _ := strconv.Atoi(strings.Split(line[3], "x")[1])
		claims[claim_num] = Claim{left, top, width, height}
	}

	var fabric [1000][1000]int
	//overlaps := make(map[int]bool)
	overlaps := []bool{}
	double_claimed := 0

	for i := 0; i <= claim_num; i++ {
		claim := claims[i]
		for w := claim.left; w < (claim.width + claim.left); w++ {
			for h := claim.top; h < (claim.height + claim.top); h++ {
				if fabric[h][w] == 0 {
					if i == 0 {
						fabric[h][w] = -2
					} else {
						fabric[h][w] = i
					}
				} else if fabric[h][w] > 0 || fabric[h][w] == -2 {
					if fabric[h][w] == -2 {
						overlaps[0] = true
					}
					overlaps[fabric[h][w]] = true
					overlaps[i] = true
					fabric[h][w] = -1
					double_claimed++
				} else {
					overlaps[i] = true
				}
			}
		}
	}
	fmt.Println("Part 1 = ", double_claimed)

	for i := 0; i <= claim_num; i++ {
		if !overlaps[i] {
			fmt.Println("Claim ", i, "has no overlap")
		}
	}
}
