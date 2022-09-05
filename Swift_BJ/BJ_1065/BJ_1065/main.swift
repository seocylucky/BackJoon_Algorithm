import Foundation

let num = Int(readLine()!)
let a = num!/100
let b = (num!-a*100)/10
let c = num!%10

if (a-b)==(b-c) {
    print("true")
}
else {
    print("false")
}
