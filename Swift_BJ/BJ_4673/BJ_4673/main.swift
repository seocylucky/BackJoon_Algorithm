//
//  main.swift
//  BJ_4673
//
//  Created by 서채연 on 2022/09/17.
//

import Foundation

var selfNumset:Set<Int> = []

func d( n: Int) -> Int {
    var sum = n
    var num = n
    while n != 0 {
        sum = sum + num % 10
        num = num / 10
        
        if num == 0 {
            break
        }
    }
    return sum
}

for i in 1...10000 {
    selfNumset.insert(d(n: i))
}
for j in 1...10000 {
    if !selfNumset.contains(j) {
        print(j)
    }
}
