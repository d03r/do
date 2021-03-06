//
//  ViewController.swift
//  PitchPerfect
//
//  Created by Nay Oo on 26/3/16.
//  Copyright © 2016 Nay Oo. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    @IBOutlet weak var recordingLabel: UILabel!
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }


    @IBAction func recordAudio(sender: UIButton) {
        print("Record button pressed")
        recordingLabel.text = "Recording in progress"
    }
    @IBAction func stopRecording(sender: UIButton) {
        print("Stop recording button pressed")
    }
}

