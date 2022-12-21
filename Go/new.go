package main

import (
	"fmt"
	"log"
	"os"
	"gopkg.in/yaml.v3"
   )

  type ReadYaml struct {
	Company       string   `yaml:"company"`
	Author        string   `yaml:"author"`
	// Tutorial.Yaml []string `yaml:"tutorial.yaml"`
}

func main() {
	// Load the file; returns []byte
	f, err := os.ReadFile("file.yaml")
	if err != nil {
		log.Fatal(err)
	}

	// Create an empty Car to be are target of unmarshalling
	var c ReadYaml

	// Unmarshal our input YAML file into empty Car (var c)
	if err := yaml.Unmarshal(f, &c); err != nil {
		log.Fatal(err)
	}

	// Print out the new struct
	fmt.Printf("%+v\n", c)
}