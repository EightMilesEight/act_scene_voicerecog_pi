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

This project was created by 8Miles8 because I do a lot of theater work, and most of the time in rehearsals half the cast and most of the crew has no idea where in the show we are, so I created this project that uses speech recognition to match what's going on onstage to the scene, and broadcasts it to a satelite device
<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Python](https://python.org/)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

* Start up the server
* Start up the client
* Enter lines, with "act x scene x" (referred to as "scene markers") before the start of each scene (these markers should appear automatically. It is very important not to delete any. If your production does not use every scene marker, just leave the spaces empty. The program will error out if it cannot find every scene marker.)

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

Coming soon...

<p align="right">(<a href="#top">back to top</a>)</p>
