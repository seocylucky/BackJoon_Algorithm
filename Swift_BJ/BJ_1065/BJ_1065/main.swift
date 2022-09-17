import Foundation

let num = Int(readLine()!)!

func hansufunc (N : Int) -> Int {
    
    var cnt : Int = 0
    for i in 0...num {
        if i > 0 && i < 100 {
            cnt = cnt + 1
        } else if i > 100 {
            let a : Int = i/100
            let b : Int = (i-a*100)/10
            let c : Int = i-(a*100)-(b*10)
            if (a - b) == (b - c) {
                cnt = cnt + 1
            }
        }
    }
    
    return cnt
}

print(hansufunc(N: num))
