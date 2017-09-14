package main

import (
     "fmt"
     "math"
)

func Sqrt(x float64) float64 {
     z := 1.0
     count := 0
     for {
          if math.Abs((z * z - x)/2 * z) < 0.00001 {
               fmt.Println(count)
               return z
          }
          z = z - (z * z - x)/2 * z
          count ++
     }
}

func main(){
     fmt.Println(Sqrt(2))
}
