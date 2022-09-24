//
//  main.swift
//  BJ_1037
//
//  Created by 서채연 on 2022/09/24.
//

import Foundation

let N = Int(readLine()!)!

let input = readLine()!

var inputArr: [Int] = input.split(separator: " ").map{Int(String($0))!}

var sortArr: [Int] = inputArr.sorted()
let Arrlast = sortArr.last!


print(sortArr[0]*Arrlast)
