package main

import(
     "fmt"
     "math"
)

const SERIES_LEN = 6

func main(){
     series := [6]float64{5,3,1,3,4,3}

     var maxv float64 = -2000000
     minv := series[0]

     for i:=0; i < SERIES_LEN; i++{
          maxv = math.Max(maxv, series[i] - minv)
          minv = math.Min(minv, series[i])
     }
     fmt.Println(maxv)
}
