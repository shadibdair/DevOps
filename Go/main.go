package main

import (
    "fmt"
    "io/ioutil"
    "log"
    "gopkg.in/yaml.v3"
)

type myData struct {
    Conf struct {
        Domain string `yaml:"company"`
    }
}

func readConf(filename string) (*myData, error) {
    buf, err := ioutil.ReadFile(filename)
//     if err != nil {
//         return nil, err
//     }

    c := &myData{}
    err = yaml.Unmarshal(buf, c)
//     if err != nil {
//         return nil, fmt.Errorf("in file %q: %w", filename, err)
//     }
    return c, err
}

func main() {
    c, err := readConf("file.yaml")
    if err != nil {
        log.Fatal(err)
    }

    fmt.Printf("%#v", c)
}