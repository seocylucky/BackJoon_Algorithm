//
//  main.swift
//  BJ_1145
//
//  Created by 서채연 on 2022/10/27.
//

import Foundation

let input = readLine()!.split(separator: " ").map{Int($0) ?? 0 };

var minN = input.min() ?? 0;

while true {
    var cnt = 0;
    for i in 0...4 {
        if minN % input[i] == 0 {
            cnt += 1;
        }
    }
    if cnt >= 3 {
        print(minN);
        break;
    }
    minN += 1;
}

