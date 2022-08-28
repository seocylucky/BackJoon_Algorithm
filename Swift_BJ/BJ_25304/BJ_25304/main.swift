import Foundation

let totalprice = Int(readLine()!)
let things = Int(readLine()!)
var thingsSum : Int = 0

for _ in 0...(things!-1) {
    let onethings = readLine()!.split(separator: " ").map { Int(String($0))! }
    thingsSum = thingsSum + onethings[0]*onethings[1]
}

if totalprice == thingsSum {
    print("Yes")
} else {
    print("No")
}

