//
//  ViewController.swift
//  Click Counter
//
//  Created by Nay Oo on 27/3/16.
//  Copyright © 2016 d03r. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    
    var count = 0
    var label:UILabel!

    override func viewDidLoad() {
        super.viewDidLoad()
        
        // Adding label
        var label = UILabel()
        label.frame = CGRectMake(150, 150, 60, 60)
        label.text = "0"
        self.view.addSubview(label)
        self.label = label
        
        // Adding button
        var button = UIButton()
        button.frame = CGRectMake(150, 250, 60, 60)
        button.setTitle("Up", forState: .Normal)
        button.setTitleColor(UIColor.blueColor(), forState: .Normal)
        self.view.addSubview(button)
        button.addTarget(self, action: "incrementCount", forControlEvents: UIControlEvents.TouchUpInside)
        
        var button2 = UIButton()
        button2.frame = CGRectMake(150, 350, 60, 60)
        button2.setTitle("Down", forState: .Normal)
        button2.setTitleColor(UIColor.blueColor(), forState: .Normal)
        self.view.addSubview(button2)
        button2.addTarget(self, action: "decrementCount", forControlEvents: UIControlEvents.TouchUpInside)
    }
    
    func incrementCount() {
        self.count++
        self.label.text = "\(self.count)"
    }
    
    func decrementCount() {
        self.count--
        self.label.text = "\(self.count)"
    }

}

