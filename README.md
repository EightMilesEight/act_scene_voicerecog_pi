<div id="top"></div>

  <h3 align="center">Scene Recognizer</h3>

  <p align="center">
    <a href="https://https://github.com/EightMilesEight/act_scene_voicerecog_pi/issues">Report Bug</a>
    ·
    <a href="https://github.com/EightMilesEight/act_scene_voicerecog_pi/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>\
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This project was created by 8Miles8 because I do a lot of theater work, and most of the time in rehearsals half the cast and most of the crew has no idea where in the show we are, so I created this project that uses speech recognition to match what's being said onstage to the scene, and broadcasts it to a satelite device (the server).

* Note- I'm completely self-taught and made this project learning how to do each thing as I went, so the code is a mess, but I did my best to comment it in a way that makes it understandable

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Python](https://python.org/)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

* Place the client device in front of the stage or in another place where it will be able to hear the actors (the closer the better- you might want to hook up an external mic for better audio quality)
* Place the satellite device (server) whereever you need it (this project was originally created because the hair & makeup team was far away from the stage and kept needing to send someone to run over and see where we were during rehearsals, so my satellite device is there)
    * Note- the server also has support for displaying the act & scene number on Adafruit's 12C 7-Segment display when being run on a Raspberry Pi, to remove the need for a full computer & screen. It's commented out, but you can just remove the quotation marks and it should work.
* Start up the server script
* Start up the client script
* Enter lines, with "act x scene x" (referred to as "scene markers") before the start of each scene (these markers should appear automatically. It is very important not to delete any. If your production does not use every scene marker, just leave the spaces empty. The program will error out if it cannot find every scene marker.)
* Press "save lines" and the script will start recognizing lines
* When a scene is recognized, the server script will open a window and update it every time a new scene is recognized
* Your server script will need to be restarted anytime your client disconnects, and vice versa


### Dependencies & Prerequisites

Client: 

* Any version of Python 3 (Windows systems)

* Python 3.6 or lower for non-widows systems (updated compatibility coming, until then use a virtual environment or older Python version. PyAudio doesn't have non-Windows wheels for newer vesions.)

* speechrecognition
  ```sh
  pip install speechrecognition
  ```

* pyaudio
  ```sh
  pip install pipwin
  pipwin install pyaudio
  ```
  
* tkinter
  ```sh
  pip install tk
  ```

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- ROADMAP -->
## Roadmap

- [x] Add GUI
- [x] Improve README
- [ ] Improve error handling & reporting
- [ ] Optimize & reorganize client script
- [ ] Improve server connection process
    - [ ] Allow server IP to be saved across sessions
    - [ ] Add auto-reconnect
- [ ] Add song recognition for musicals
- [ ] Add Python 3.7+ support

See the [open issues](https://github.com/EightMilesEight/act_scene_voicerecog_pi/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* Some people who made this project possible (only giving initials for sake of privacy)
    * LS
    * TJ
    * JG
* RealPython's socket API & threading guides


<p align="right">(<a href="#top">back to top</a>)</p>
