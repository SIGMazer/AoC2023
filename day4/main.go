package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
    "strconv"
)


func main() {
    copies := make(map[int]int)

	file, err := os.Open("input")
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
    i := 0
    part1 :=0
	for scanner.Scan() {
		line := scanner.Text()
        copies[i]++
        parts := strings.Split(line,"|")
        first, rest := parts[0], parts[1]
        firstpart := strings.Split(first, ":")
        card := firstpart[1]
        winCard := parseIntSlice(strings.Fields(card))
        myCard := parseIntSlice(strings.Fields(rest))
        value := intersectionSize(winCard, myCard)
        if value > 0 {
            part1 += pow(2,value -1)
        }
        for j:=0; j<value; j++{
            copies[j+i+1] += copies[i]
        }
        i++
        
    }
    part2 := 0 
    for _, v := range copies{
        part2 += v 
    }
    fmt.Println(part1)
    fmt.Println(part2)
}
func intersectionSize(a, b []int) int {
	setA := make(map[int]bool)
	for _, num := range a {
		setA[num] = true
	}
	count := 0
	for _, num := range b {
		if setA[num] {
			count++
			setA[num] = false
		}
	}
	return count
}


func parseIntSlice(strSlice []string) []int{
    intSlice := make([]int,len(strSlice))
	for i, str := range strSlice {
		num, err := strconv.Atoi(str)
		if err != nil {
			panic(err)
		}
		intSlice[i] = num
	}
	return intSlice

}

func pow(base, exponent int) int {
	result := 1
	for i := 0; i < exponent; i++ {
		result *= base
	}
	return result
}

