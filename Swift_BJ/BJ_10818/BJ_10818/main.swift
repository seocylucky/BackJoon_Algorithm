import Foundation

let N = Int(readLine()!)!

let input = readLine()!.split(separator: " ").map{Int(String($0))!}

print(input.min()!, input.max()!)
