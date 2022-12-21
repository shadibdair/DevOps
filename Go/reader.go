package main

import (
	"bufio"
	"fmt"
	"io/ioutil"
	"os"
	"strings"
)

var (
     company string
     domain string
)

func ReadStats(filename string) {
     file, err := os.Open(filename)
     if err != nil {
          fmt.Println(err.Error())
          return
     }

     defer file.Close()

     stats, err := file.Stat()
     if err != nil {
          fmt.Println(err.Error())
          return
     }
     fmt.Println("File Name: ", stats.Name())
     fmt.Println("Time Modified: ", stats.ModTime().Format("15:04:03"))
}

func ReadWholeFile(filename string) {
     contents, err := ioutil.ReadFile(filename)
     if err != nil {
          fmt.Println(err.Error())
          return
     }

     fmt.Println(string(contents))
}

func ReadByLine(filename string) {
     file, err := os.Open(filename)
     if err != nil {
          fmt.Println(err.Error())
          return
     }

     defer file.Close()

     scanner := bufio.NewScanner(file)
     for scanner.Scan() {
          fmt.Println(scanner.Text())
     }
}

func ReadByWord(filename string) {
     file, err := os.Open(filename)
     if err != nil {
          fmt.Println(err.Error())
          return
     }

     defer file.Close()

     scanner := bufio.NewScanner(file)
     scanner.Split(bufio.ScanWords)
     for scanner.Scan() {
          fmt.Println(scanner.Text())
     }
}

func ReadConfig(filename string) {
     file, err := os.Open(filename)
     if err != nil {
          fmt.Println(err.Error())
          return
     }

     defer file.Close()

     scanner := bufio.NewScanner(file)
     for scanner.Scan() {
          raw := strings.Split(scanner.Text(), ":") // [key, value]
          key := raw[0]
          val := raw[1]

          if key == "company" {
               company = val
          } else if key == "domain" {
               domain = val
          }
     }
}

func main() {
     filename := "file.yaml"
     //ReadStats(filename)
     //ReadWholeFile(filename)
     //ReadByLine(filename)
     //ReadByWord(filename)
     ReadConfig(filename)
     fmt.Println(company)
     fmt.Println(domain)
}