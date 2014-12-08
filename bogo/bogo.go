/**
 * bogosort - Given a scrambled string N and another string M. You must
 * sort N so that it matches M. After it has been sorted, it must output
 * how many iterations it took to complete the sorting.
 *
 * For a bit of fun, the LEAST efficient algorithm wins. Check out the bogo-bogo sort,
 * an algorithm that's designed not to succeed before the heat death of the universe
 * http://www.dangermouse.net/esoteric/bogobogosort.html[2]
 *
 *
 */
package main

import (
	"fmt"
	"log"
	"math/rand"
	"os"
	"strings"
	"time"
)

func main() {
	rand.Seed(time.Now().UTC().UnixNano())

	if len(os.Args) != 3 {
		log.Fatal("Usage: bogo helol hello")
	}

	firstWord := os.Args[1]
	secondWord := os.Args[2]

	bogoSortAndReturnIterations(firstWord, secondWord)
}

func bogoSortAndReturnIterations(scrambled string, unscrambled string) int {
	letters := strings.Split(scrambled, "")

	var iterations int

	for {
		shuffledStringSlice := ShuffleStringSlice(letters)
		word := strings.Join(shuffledStringSlice, "")

		iterations++

		// Compare word to original input
		if word == unscrambled {
			log.Print(fmt.Sprintf("Shuffled word with %d iterations.", iterations))

			break
		} else {
			log.Print(fmt.Sprintf("Iteration #%d: %s", iterations, word))
		}
	}

	return iterations
}

func ShuffleStringSlice(input []string) []string {
	for i := range input {
		j := rand.Intn(i + 1)
		input[i], input[j] = input[j], input[i]
	}

	return input
}
