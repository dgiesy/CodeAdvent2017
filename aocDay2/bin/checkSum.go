package main 

import (
	"bufio"
	"log"
    "fmt"
    "strings"
    "strconv"
    "os"
)

	
func check(e error) {
    if e != nil {
        panic(e)
    }
}

func checkSum1(data *os.File){
    checkSum := 0

    scanner := bufio.NewScanner(data)
    for scanner.Scan() {
        elements := strings.Fields(scanner.Text())
        var min int
        var max int
        min, err := strconv.Atoi(elements[0])
        if err != nil {
	        fmt.Println(err)
	        os.Exit(2)
	    }
        max, err2 := strconv.Atoi(elements[0])
        if err2 != nil {
	        fmt.Println(err2)
	        os.Exit(2)
	    }
        j := len(elements)
        for i := 0; i < j; i++ {
        	current, err3 := strconv.Atoi(elements[i])
        	if err3 != nil {
		        fmt.Println(err3)
		        os.Exit(2)
		    }
        	if current < min {
        		min = current
        	}
        	if current > max {
        		max = current 
        	}
        }
        diff := max - min
        checkSum = checkSum + (diff)
    }

    if err := scanner.Err(); err != nil {
        log.Fatal(err)
    }
    
    fmt.Println("Ending checkSum1: " + strconv.Itoa(checkSum))
}

func checkSum2(data *os.File){
	checkSum := 0

    scanner := bufio.NewScanner(data)
    for scanner.Scan() {
    	stringElements := strings.Fields(scanner.Text())
    	var nums = []int{}
	    for _, i := range stringElements {
	        j, err := strconv.Atoi(i)
	        if err != nil {
	            panic(err)
	        }
	        nums = append(nums, j)	        
	    }
	    var tmpCS int	
	    for _, i := range nums {
	    	tmpCS = 0
	    	for _, k := range(nums){
	    		if k != i {
	    			small, big := minMax(i, k)
	    			if big%small == 0{
	    				tmpCS = (big/small)
	    				checkSum = checkSum + tmpCS
	    				break
	    			}
	    		}
	    	}
	    	if tmpCS != 0{
	    		break
	    	}
	    }
    }
    fmt.Println("Ending checkSum2: " + strconv.Itoa(checkSum))
}

func main() {

//  Uncomment and comment out next line to run on sample data
//	file, err := os.Open("../unitTest1.txt")	
	file, err := os.Open("../spreadsheetData.txt")
    if err != nil {
        log.Fatal(err)
    }
    defer file.Close()
    
//  Uncomment and comment out next line to run on sample data    
//    file2, err2 := os.Open("../unitTest2.txt")
    file2, err2 := os.Open("../spreadsheetData.txt")
    if err2 != nil {
        log.Fatal(err2)
    }
    defer file2.Close()
    
    checkSum1(file)
    checkSum2(file2)
}

func minMax(x int, y int)(min, max int){
	if x > y {
		max = x
		min = y
	}else{
		max = y
		min = x
	}
	return
}
